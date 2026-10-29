# SPAR Ontologies

The Semantic Publishing and Referencing Ontologies, a.k.a. [SPAR Ontologies](http://www.sparontologies.net), form a suite of orthogonal and complementary OWL 2 DL ontology modules for the creation of comprehensive machine-readable RDF metadata for every aspect of semantic publishing and referencing: document description, bibliographic resource identifiers, types of citations and related contexts, bibliographic references, document parts and status, agents' roles and contributions, bibliometric data and workflow processes.

Each ontology is developed in its own repository of the [SPAR Ontologies GitHub organisation](https://github.com/sparontologies), and is identified by an IRI of the form `http://purl.org/spar/<lowercase ontology acronym>`.

## This repository

This repository contains:

* the source of the [SPAR Ontologies website](http://www.sparontologies.net), a [web.py](https://webpy.org) application (`spar.py`) whose pages are in `spar/` and whose static files are in `static/`. The descriptions, examples, publications and news of each ontology are in the `spar/ontology_*` directories;
* the media type descriptions served at <https://w3id.org/spar/mediatype/>, in `mediatype/`;
* the reusable GitHub Actions workflows called by the ontology repositories: [`validation.yml`](.github/workflows/validation.yml), which runs the ontology tests in [`scripts/test_ontology.py`](scripts/test_ontology.py), and [`lode.yml`](.github/workflows/lode.yml), which generates the documentation and the serialisations of an ontology with [LODE 2.0](https://lode.opencitations.net);
* the files to build and deploy the website, i.e. the `Dockerfile` and `docs/k8s.yaml`.

To run the website locally, on port 8080:

```
uv sync
uv run gunicorn -c gunicorn.conf.py spar:application
```

## Documentation

* [Contributing guidelines](https://github.com/SPAROntologies/.github/blob/main/CONTRIBUTING.md): how to change an existing ontology, how to propose a new one, and the participation, documentation, GitHub and website guidelines.
* [Support](https://github.com/SPAROntologies/.github/blob/main/SUPPORT.md): where to ask questions.
* [Code of conduct](https://github.com/SPAROntologies/.github/blob/main/CODE_OF_CONDUCT.md).
* [Ontologies](http://www.sparontologies.net/ontologies), [examples](http://www.sparontologies.net/examples), [publications](http://www.sparontologies.net/publications) and [uptake](http://www.sparontologies.net/uptake) of the SPAR Ontologies, on the website.
* [About](http://www.sparontologies.net/about) and [contacts](http://www.sparontologies.net/contacts).
