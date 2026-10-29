# scripts/test_ontology.py

import subprocess
import tomllib
import warnings
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import requests
from owlrl import OWLRL_Semantics
from rdflib import OWL, Graph

ROOT = Path.cwd()

_pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
ACRONYM = _pyproject["project"]["name"]
_config = _pyproject.get("tool", {}).get("validate", {})
ONTOLOGY_FILE = ROOT / _config.get("ontology_file", f"docs/current/{ACRONYM}.ttl")
NAMESPACE = _config.get("namespace", f"http://purl.org/spar/{ACRONYM}/")

def _urls(key, default):
    value = _config.get(key, default)
    return [value] if isinstance(value, str) else value


# Each may be a single URL or a list tried in order (e.g. public instance, then a self-hosted one).
FOOPS_API_URLS = _urls("foops_api_url", "https://foops.linkeddata.es/assessOntologyFile")
MIN_FAIR_SCORE = _config.get("min_fair_score", 0.85)
OOPS_API_URLS = _urls("oops_api_url", "https://oops.linkeddata.es/rest")
OOPS_NS = "{http://www.oeg-upm.net/oops}"

PREFIXES = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

DL_CHECKS = {
    "IRI declared as both object and datatype property": """
        SELECT DISTINCT ?x WHERE { ?x a owl:ObjectProperty, owl:DatatypeProperty . }
    """,
    "IRI declared as both object and annotation property": """
        SELECT DISTINCT ?x WHERE { ?x a owl:ObjectProperty, owl:AnnotationProperty . }
    """,
    "IRI declared as both datatype and annotation property": """
        SELECT DISTINCT ?x WHERE { ?x a owl:DatatypeProperty, owl:AnnotationProperty . }
    """,
    "Transitive property used in a cardinality restriction": """
        SELECT DISTINCT ?x WHERE {
            ?x a owl:TransitiveProperty .
            ?r owl:onProperty ?x .
            { ?r owl:cardinality ?n } UNION { ?r owl:minCardinality ?n }
            UNION { ?r owl:maxCardinality ?n } UNION { ?r owl:qualifiedCardinality ?n }
            UNION { ?r owl:minQualifiedCardinality ?n } UNION { ?r owl:maxQualifiedCardinality ?n }
        }
    """,
    "Datatype property declared transitive, symmetric or inverse": """
        SELECT DISTINCT ?x WHERE {
            ?x a owl:DatatypeProperty .
            { ?x a owl:TransitiveProperty } UNION { ?x a owl:SymmetricProperty }
            UNION { ?x owl:inverseOf ?y } UNION { ?y owl:inverseOf ?x }
        }
    """,
    "Ontology term used but not declared": f"""
        SELECT DISTINCT ?x WHERE {{
            {{ ?s ?x ?o }} UNION {{ ?s rdf:type ?x }} UNION {{ ?s rdfs:subClassOf ?x }}
            UNION {{ ?s rdfs:domain ?x }} UNION {{ ?s rdfs:range ?x }}
            UNION {{ ?s owl:onProperty ?x }} UNION {{ ?s owl:someValuesFrom ?x }}
            UNION {{ ?s owl:allValuesFrom ?x }} UNION {{ ?s rdfs:subPropertyOf ?x }}
            FILTER(isIRI(?x) && STRSTARTS(STR(?x), "{NAMESPACE}"))
            FILTER NOT EXISTS {{ ?x a ?t }}
        }}
    """,
}


@pytest.fixture(scope="session")
def graph():
    assert ONTOLOGY_FILE.exists(), f"File not found: {ONTOLOGY_FILE}"
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def test_syntax(graph):
    assert len(graph) > 0, "Ontology file contains no triples."


def test_spelling():
    result = subprocess.run(["codespell", str(ONTOLOGY_FILE)], capture_output=True, text=True)
    if result.returncode != 0:
        warnings.warn(
            "Possible spelling errors found: check them manually, they may be correct terms.\n"
            + result.stdout.replace(str(ROOT) + "/", "").rstrip()
        )


@pytest.mark.parametrize("title", DL_CHECKS)
def test_dl(graph, title):
    violations = [str(row.x) for row in graph.query(PREFIXES + DL_CHECKS[title])]
    assert not violations, f"{title}: {violations}"


def test_consistency(graph):
    closure = Graph()
    for triple in graph:
        closure.add(triple)
    semantics = OWLRL_Semantics(closure, False, False, False)
    semantics.closure()
    assert not semantics.error_messages, "Inconsistencies found:\n" + "\n".join(semantics.error_messages)


def post_or_skip(service, urls, **kwargs):
    errors = []
    for url in urls:
        try:
            response = requests.post(url, **kwargs)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            errors.append(f"{url}: unreachable ({e})")
            continue
        if response.status_code < 500:
            return response
        errors.append(f"{url}: unavailable ({response.status_code})")
    pytest.skip(f"{service} API unavailable:\n" + "\n".join(errors))


def test_oops_pitfalls(graph):
    local = Graph()
    for prefix, namespace in graph.namespaces():
        local.bind(prefix, namespace)
    for triple in graph:
        if triple[1] != OWL.imports:
            local.add(triple)
    content = local.serialize(format="xml").replace("]]>", "]]]]><![CDATA[>")
    request = (
        '<?xml version="1.0" encoding="UTF-8"?><OOPSRequest><OntologyUrl></OntologyUrl>'
        f"<OntologyContent><![CDATA[{content}]]></OntologyContent>"
        "<Pitfalls></Pitfalls><OutputFormat>XML</OutputFormat></OOPSRequest>"
    )
    response = post_or_skip(
        "OOPS!",
        OOPS_API_URLS,
        data=request.encode("utf-8"),
        headers={"Content-Type": "application/xml"},
        timeout=(15, 120),
    )
    assert response.ok, f"OOPS! API request failed ({response.status_code}): {response.text[:500]}"
    try:
        root = ET.fromstring(response.content)
    except ET.ParseError:
        pytest.fail(f"OOPS! API returned a non-XML response: {response.text[:500]}")
    assert root.tag == f"{OOPS_NS}OOPSResponse", f"Unexpected OOPS! response format: {response.text[:500]}"

    counts = {}
    lines = []
    for pitfall in root.iter(f"{OOPS_NS}Pitfall"):
        importance = pitfall.findtext(f"{OOPS_NS}Importance", "Unknown")
        counts[importance] = counts.get(importance, 0) + 1
        lines.append(f"[{importance}] {pitfall.findtext(f'{OOPS_NS}Code')} {pitfall.findtext(f'{OOPS_NS}Name')}")
        for element in pitfall.iter(f"{OOPS_NS}AffectedElement"):
            lines.append(f"    - {element.text}")

    if not counts:
        return
    summary = ", ".join(f"{n} {importance.lower()}" for importance, n in counts.items())
    details = "\n".join(lines)
    assert "Critical" not in counts, f"Critical pitfalls found ({summary}):\n{details}"
    warnings.warn(f"Pitfalls found ({summary}): none critical, review them manually.\n{details}")


def test_fair_score():
    response = post_or_skip(
        "FOOPS!",
        FOOPS_API_URLS,
        files={"file": (ONTOLOGY_FILE.name, ONTOLOGY_FILE.read_bytes(), "text/turtle")},
        headers={"Accept": "application/json"},
        timeout=(15, 60),
    )
    assert response.ok, f"FOOPS! API request failed ({response.status_code}): {response.text[:500]}"
    try:
        data = response.json()
    except ValueError:
        pytest.fail(f"FOOPS! API returned a non-JSON response: {response.text[:500]}")
    assert "overall_score" in data, f"Unexpected FOOPS! response format: {str(data)[:500]}"

    overall_score = data["overall_score"]
    failed_checks = [
        f"[{check.get('principle_id', 'FAIR')}] {check.get('title', check.get('id', 'Check'))}: {check.get('explanation', '')}"
        for check in data.get("checks", [])
        if check.get("total_passed_tests", 0) != check.get("total_tests_run", -1)
    ]
    assert overall_score >= MIN_FAIR_SCORE, (
        f"FAIR score ({overall_score * 100:.1f}%) is below the minimum threshold ({MIN_FAIR_SCORE * 100:.1f}%).\n"
        + "\n".join(failed_checks)
    )
