# Contributing to the SPAR Ontologies

Thank you for your interest in the [SPAR Ontologies](http://www.sparontologies.net). This document applies to every ontology of the SPAR family and to the repositories of the [SPAR Ontologies GitHub organisation](https://github.com/sparontologies). It contains:

* [how to contribute](#how-to-contribute), i.e. the process to follow for changing an existing ontology or for proposing and developing a new one;

* [participation guidelines](#participation-guidelines), i.e. the rules with which an ontology must be compliant to be included in the SPAR Ontologies;

* [documentation guidelines](#documentation-guidelines), i.e. the metadata that must be used to describe a SPAR ontology and each of its terms;

* [GitHub guidelines](#github-guidelines), i.e. the process to follow for making the ontology available in the SPAR Ontologies GitHub repository;

* [website guidelines](#website-guidelines), i.e. the additional material that must be added to the [SPAR Ontologies official website](http://www.sparontologies.net).

It also explains where to [ask questions](#questions-and-support), the [code of conduct](#code-of-conduct) and the [license of contributions](#license-of-contributions).

Please read these guidelines **carefully** before proposing a change to an existing ontology or a new ontology to be included within the SPAR Ontologies.

### Questions and support

See [SUPPORT.md](SUPPORT.md).

### Code of conduct

All contributors must follow the [code of conduct](CODE_OF_CONDUCT.md).

### License of contributions

By contributing to a SPAR ontology, you agree that your contribution is released under the same license as the ontology, i.e. the license stated by its `dcterms:license` annotation and in its `README.md`.

## How to contribute

There are two ways of contributing: improving an ontology that is already part of SPAR, or proposing a new ontology (or an existing external one) for inclusion in SPAR.

### Contributing to an existing ontology

Every SPAR ontology has its own repository, named after the lowercase acronym of the ontology, i.e. `https://github.com/SPAROntologies/<lowercase ontology acronym>`. All the contributions to an ontology go through that repository.

#### 1. Open an issue

Before changing anything, open an issue in the repository of the ontology. This applies to bug reports (e.g. a wrong definition, an inconsistency, a broken link), to requests for new terms, and to proposals for changing or deprecating existing terms. The issue should specify:

* the terms involved (using their IRIs) or the new terms proposed, with a draft label and definition;
* the motivation, i.e. the scenario that the current version of the ontology cannot describe, possibly expressed as one or more competency questions;
* a short example in Turtle showing how the change would be used;
* whether the change is backward compatible with the current version of the ontology.

Wait for a response from the maintainers before working on changes that affect the model, since a proposal may need a few iterations before being accepted. Small corrections that do not change the model (typos, broken links, formatting of the documentation) can be submitted directly as pull requests.

Issues that concern the website, or more than one ontology at once, should be opened in the [sparontologies.github.io repository](https://github.com/sparontologies/sparontologies.github.io/issues) instead.

#### 2. Make the change

Once the proposal has been agreed in the issue:

1. fork the repository of the ontology and create a branch for your change;
1. edit the source file of the ontology, i.e. the `.ttl` file in the `docs/current` directory – do not edit the other serialisations by hand, since they are generated from the source file;
1. make sure that every term added or modified follows the naming conventions and the other [participation guidelines](#participation-guidelines), in particular the minimal use of domain and range constraints, and that it carries all the REQUIRED annotations listed in the [term metadata checklist](#spar-term-metadata-checklist);
1. never delete or rename a term that has already been published: mark it as deprecated instead (`owl:deprecated true`, plus the appropriate `vs:term_status`) and point to its replacement, if any.

You do not need to validate the ontology locally: when you open the pull request, the `validation.yml` workflow checks that the ontology is well written, still consistent and still in OWL 2 DL, as well as its FAIRness compliance (see [GitHub guidelines](#github-guidelines)).

#### 3. Prepare the new version

A change to the ontology results in a new version of it. In the same branch:

1. update the ontology metadata as described in the [ontology metadata checklist](#spar-ontology-metadata-checklist): update `owl:versionIRI`, `owl:priorVersion`, `owl:versionInfo` and `dcterms:modified`. The value of `dcterms:modified` must be the same `yyyy-mm-dd` date used in `owl:versionIRI`, since it is used to name the new version directory;
1. add an entry for the new version at the top of the `CHANGELOG.md` file in the root of the repository, as described for [`vann:changes`](#spar-ontology-metadata-checklist);
1. add yourself to the contributors of the ontology (`dc:contributor`), if you are not already listed among its creators or contributors;
1. update the `README.md` of the repository if the change affects it (e.g. the list of contributors).

Do not regenerate the other serialisations, the HTML documentation or the `yyyy-mm-dd` version directory by hand: once the pull request is merged, the `release.yml` workflow creates them and publishes a new release (see [GitHub guidelines](#github-guidelines)).

#### 4. Open a pull request

Open a pull request against the main/master branch of the repository of the ontology. The pull request must reference the issue it addresses and summarise the changes made to the ontology, listing the terms added, modified and deprecated. Check the report of the `validation.yml` workflow run on the pull request, and fix the errors it reports. If an error is unclear, or you think it is a false positive, report it in the pull request and ask the maintainers. The [owners](https://github.com/orgs/SPAROntologies/people?utf8=%E2%9C%93&query=+role%3Aowner) of the SPAR Ontologies GitHub organisation review the pull request, and may ask for changes before merging it.

If the change makes the description or the examples published on the website out of date, or adds something worth showing there, open a second pull request on the [website repository](https://github.com/sparontologies/sparontologies.github.io), following the [website guidelines](#website-guidelines).

### Proposing a new ontology

To propose a new ontology (or an existing one) to be included within the family of SPAR Ontologies, you have to open a new issue at the [sparontologies.github.io repository](https://github.com/sparontologies/sparontologies.github.io/issues), specifying "NEW" plus the name of the ontology as title of the issue, assigning the label *new ontology*, and filling in the content of the issue using the following template:

```
**Name:** <full name of the ontology>

**Acronym:** <ontology acronym>

**Proponent(s):** [<proponent full name>](<GitHub user URL>), ...

<free text description of the ontology, where you specify
precisely its purpose and scope, the ontology development process adopted, and any other useful information for assessing it>
```

All the fields between angle brackets included in the aforementioned template must be substituted with the appropriate text. All the fields are mandatory.

All the requests will be evaluated by the owners of the SPAR Ontologies GitHub organisation. It is possible for a new proposal to have a few iterative responses before being given a final response on whether or not the proposed ontology is accepted into SPAR. If the response is positive, then a new GitHub repository within the SPAR Ontologies organisation will be created using the ontology acronym, and a new `purl.org` URL will be made available for that ontology.

### Developing a new ontology after its acceptance

Once the proposal has been accepted and the repository has been created, the proponents are expected to:

1. develop the ontology according to a structured, well-documented methodology that testifies the soundness of the ontology development process, such as [SAMOD](https://essepuntato.github.io/samod);
1. make the ontology compliant with all the [participation guidelines](#participation-guidelines), in particular those concerning the ontology IRI, the version IRI and the entity IRIs, which depend on the acronym and on the `purl.org` URL assigned;
1. describe the ontology and all its terms according to the [documentation guidelines](#documentation-guidelines);
1. populate the repository – the `README.md`, `CHANGELOG.md`, `CITATION.cff` and `pyproject.toml` files, the `.ttl` file in the `docs/current` directory, and the `validation.yml` and `release.yml` workflows, which generate the rest of the `docs` directory – as described in the [GitHub guidelines](#github-guidelines);
1. add the description, the examples, the acronym and the publications (if any) of the ontology to the website repository via pull requests, and open the "DESC" issue, as described in the [website guidelines](#website-guidelines).

From that moment on, any further change to the ontology follows the process described in [Contributing to an existing ontology](#contributing-to-an-existing-ontology).

## Participation guidelines

These are the rules that a candidate ontology must follow in order to be eligible to be part of the SPAR Ontologies. They keep applying to the ontology, and to every contribution to it, after its inclusion:

1. it should cover a specific and limited area of interest within the domain of scholarly publishing and referencing (widely interpreted);
1. it must be orthogonal, non-overlapping, complementary and interoperable with existing SPAR Ontologies;
1. it should act primarily as a structured defined vocabulary, and should thus be extensive enough to cover vocabulary terms in common and professional usage;
1. it must be well-developed, accurate and explicit, and must have unambiguous explanatory English-language definitions for all classes, properties, and individuals it describes;
1. it must be given a name ("The *** Ontology") appropriate to its purpose, and a clear short acronym based on that name. The acronym must contain no spaces or special characters - only English alphabetic characters, numerals, and the character "-" are admissible;
1. it must be written in OWL 2 DL;
1. its IRI must be composed by `http://purl.org/spar/` plus the lowercase string of its acronym (additional characters at the end, e.g. `/`, are not permitted);
1. its version IRI (`owl:versionIRI`) must be composed by its IRI plus `/` plus the [ISO date](https://en.wikipedia.org/wiki/ISO_8601) `yyyy-mm-dd` referring to the publication date of that particular version;
1. it must include an explicit reference (via `owl:priorVersion`) to its previous version, if any;
1. the entity IRI of each entity defined in it (not any imported ones) must be composed by its IRI plus `/` plus the entity local IRI (only English alphabetic characters and numerals are admissible) defined as prescribed in the [SAMOD methodology](https://w3id.org/people/essepuntato/papers/samod-owled2016.html):
   > Class names local to the ontology (i.e. not imported) must be capitalised (e.g. *Justification*) and adopt camel-case notation if composed of more than one word (e.g. *DescriptionOfVagueness*).  Property names local to the ontology (i.e. not imported) must start with a non-capitalised verb and adopt camel-case notation if composed of more than one word (e.g. *wasAttributedTo*).  Local names of Individuals must be non-capitalised (e.g. *ceo*) and dash-separated if composed by more than one word (e.g. *quantitative-vagueness*).
1. it must have a minimal use of domain and range constraints when possible, to permit unanticipated uses;
1. it may import and reuse, or should complement, well-known and well-used third party vocabularies, e.g. DC Elements, FOAF, SKOS, FRBR;
1. it must be released according to an open access license compatible with the [Creative Commons Free Cultural Works guidelines](https://creativecommons.org/share-your-work/public-domain/freeworks);
1. it must be rendered human-readable in HTML (e.g. produced by means of [LODE 2.0](https://lode.opencitations.net) or [Widoco](https://github.com/dgarijo/Widoco));
1. it should be accompanied by one or more explanatory diagrams (e.g. in [Graffoo](http://www.essepuntato.it/graffoo) or [VOWL](http://vowl.visualdataweb.org/));
1. it must be available in at least four RDF formats, i.e. Turtle, N-triples, RDF/XML, and JSON-LD;
1. it must be stored in the SPAR Ontologies GitHub repository, following a precise structure so as to keep track also of its versions and evolution – see the [GitHub guidelines](#github-guidelines);
1. it must be described by a specific page on the SPAR Ontologies website that should also include Turtle examples of usage – see the [website guidelines](#website-guidelines);
1. its authors must be stated in the ontology itself – see the [documentation guidelines](#documentation-guidelines).

## Documentation guidelines

This section describes the properties reused from existing vocabularies to describe the SPAR ontologies and their terms, along with a rationale explaining their relevance.

Guidelines like [Vandenbussche and Vatant 2012] (*Metadata recommendations for linked open data vocabularies*) and [Garijo and Poveda-Villalón] (*A checklist for complete vocabulary metadata*, https://w3id.org/widoco/bestPractices) describe concrete recommendations of metadata properties that are typically used to describe specific aspects of a vocabulary (e.g. its creators and its license). These guidelines build on those recommendations to create an expanded list of the metadata terms used to describe SPAR ontologies.

For each metadata term, we list the property used to represent it, and we state whether adding the property is required, recommended, or advisable but optional when describing a SPAR ontology.

### Namespaces

| Prefix | URI |
| --- | --- |
| `vann` | `http://purl.org/vocab/vann/` |
| `dc` | `http://purl.org/dc/elements/1.1/` |
| `dcterms` | `http://purl.org/dc/terms/` |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `bibo` | `http://purl.org/ontology/bibo/` |
| `schema` | `https://schema.org/` |
| `owl` | `http://www.w3.org/2002/07/owl#` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `vs` | `http://www.w3.org/2003/06/sw-vocab-status/ns#` |
| `vaem` | `http://www.linkedmodel.org/schema/vaem#` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |
| `cito` | `http://purl.org/spar/cito/` |
| `datacite` | `http://purl.org/spar/datacite/` |
| `fabio` | `http://purl.org/spar/fabio/` |
| `reg` | `http://purl.org/linked-data/registry#` |

### Conventions

The key words "REQUIRED", "RECOMMENDED" and "OPTIONAL" in this section are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

The examples below use [CiTO](http://purl.org/spar/cito), [DataCite](http://purl.org/spar/datacite) and other existing third-party vocabularies, and assume the prefixes listed in the [namespaces](#namespaces) table. The IRIs of a SPAR ontology, of its versions and of its terms must always follow the [participation guidelines](#participation-guidelines).

### SPAR ontology metadata checklist

#### Identification

**`vann:preferredNamespaceUri`** – REQUIRED

A literal containing the main URI of the vocabulary. This becomes important in cases when you use permanent URLs: the vocabulary local URI hosting the file may not be the main URI you want people to access when resolving it. The value must be a literal, not a resource (URL).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   vann:preferredNamespaceUri "http://purl.org/spar/cito/" .
```

**`vann:preferredNamespacePrefix`** – REQUIRED

A literal containing the preferred prefix used to refer to the ontology. This is important to let potential reusers know how you expect your ontology to be abbreviated, so that everyone refers to it in the same way. It is also recommended to register your prefix at the [prefix.cc](http://prefix.cc) service.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   vann:preferredNamespacePrefix "cito" .
```

#### Description

**`rdfs:label`** – REQUIRED

A literal containing the full name plus the short acronym of your ontology.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   rdfs:label "Citation Typing Ontology (CiTO)"@en .
```

**`dcterms:title`** – RECOMMENDED

A literal containing the title of the ontology.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:title "The Citation Typing Ontology (CiTO)"@en .
```

**`dc:description`** – RECOMMENDED

A literal containing what the ontology does and why someone should use it. It is written following the Markdown syntax and is structured in the following sections:

* a brief description, containing text formatted in Markdown and possibly including diagrams of the ontology;
* examples of use, with at least one concrete example written in Turtle;
* Competency Questions, with at least one Competency Question accompanied by its corresponding SPARQL query.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dc:description """
The **_Citation Typing Ontology (CiTO)_** is an ontology written in OWL 2 DL to enable characterization of the nature or type of citations, both factually and rhetorically, and to permit these descriptions to be published on the Web.

## Examples of use

### Defining citation links and their functions

   :paper-a cito:extends :paper-b .

## Competency Questions

### CQ1

Which papers directly extend other papers?

   SELECT ?citingPaper ?citedPaper
   WHERE {
       ?citingPaper cito:extends ?citedPaper .
   }
"""@en .
```

For a complete description, see the documentation of [CiTO](http://purl.org/spar/cito).

**`bibo:status`** – RECOMMENDED

A link to the status of the vocabulary (recommendation, draft, etc.). The range of `bibo:status` is a `bibo:DocumentStatus` instance. Common statuses include `bibo:status/accepted`, `bibo:status/draft`, `bibo:status/published`, `bibo:status/rejected` and `bibo:status/peerReviewed`. For more information, please see the [BIBO vocabulary](http://purl.org/ontology/bibo/).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   bibo:status <http://purl.org/ontology/bibo/status/accepted> .
```

**`schema:keywords`** – OPTIONAL

One or more literals containing terms describing the ontology and its domain, uses and overall context. Each keyword is a separate string.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   schema:keywords 
      "SPAR Ontologies"@en ,
      "Semantic Publishing and Referencing Ontologies"@en ,
      "bibliometrics"@en ,
      "citation networks"@en ,
      "scholarly publishing"@en ,
      "scientometrics"@en ,
      "semantic publishing"@en .
```

#### Version and provenance

**`owl:versionIRI`** – REQUIRED

A link to the current version of the vocabulary. Its form is defined in the [participation guidelines](#participation-guidelines).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:versionIRI <http://purl.org/spar/cito/2026-09-03> .
```

**`owl:versionInfo`** – REQUIRED

A literal containing the version number being handled. We recommend using [semantic versioning](https://semver.org).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:versionInfo "2.9.0" .
```

**`owl:priorVersion`** – REQUIRED if a previous version exists

A link to the previous version. It helps to see how the vocabulary has changed from one version to the other.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:priorVersion <http://purl.org/spar/cito/2026-06-22> .
```

**`owl:backwardCompatibleWith`** – OPTIONAL

A link to a previous version of the vocabulary which is compatible with the current one.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:backwardCompatibleWith <http://purl.org/spar/cito/2026-06-22> .
```

**`owl:incompatibleWith`** – OPTIONAL

A link to a previous version of the vocabulary which is incompatible with the current one.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:incompatibleWith <http://purl.org/spar/cito/2017-10-30> .
```

**`dcterms:created`** – RECOMMENDED

A literal containing the date when the vocabulary was created. There are different ways in which the date may be represented, but typically it is an `xsd:date` or `xsd:dateTime` literal.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:created "2017-10-30"^^xsd:date .
```

**`dcterms:modified`** – RECOMMENDED

A literal containing the date when the vocabulary was last modified.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:modified "2026-09-03"^^xsd:date .
```

**`dcterms:issued`** – RECOMMENDED

A literal containing the date of formal issuance of the vocabulary, such as its publication.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:issued "2017-10-30"^^xsd:date .
```

**`dcterms:source`** – RECOMMENDED

A link to a document where the terms of the vocabulary come from. In the case of the SPAR Ontologies, the source is usually a document containing the Competency Questions used to develop and test the ontology.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:source <https://github.com/SPAROntologies/cito/blob/master/docs/cq.md> .
```

**`vann:changes`** – REQUIRED

A link to the `CHANGELOG.md` file in the root of the repository of the ontology, which describes the changes between each version of the vocabulary and the previous one. Each version is registered in the file as an element of a Markdown bulleted list introduced by `**v<VERSION_NUMBER>**:`, with the most recent version first:

```markdown
# Changelog

* **v2.9.0**:
Added new documentation, including annotation properties (e.g., `bibo:doi`, `schema:codeRepository`, etc.), term properties (e.g., `vann:example`, `vs:term_status`, etc.), exemplary competency questions with their respective SPARQL queries, and a Grafoo diagram.
```

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   vann:changes <https://github.com/SPAROntologies/cito/blob/master/CHANGELOG.md> .
```

#### License

**`dcterms:license`** – REQUIRED

A link to a document which tells potential reusers under which terms the ontology may be used, how they should provide attribution to the original authors, and under which terms they have to license their own work as well. The license must follow the [participation guidelines](#participation-guidelines).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:license <https://creativecommons.org/licenses/by/4.0/> .
```

#### Attribution

**`dc:creator`** – REQUIRED

One or more literals containing the names of the people who created the vocabulary. Whenever possible, each person should be represented as a separate string following the pattern "<Name> <Surname> (<ORCID>)".

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dc:creator "David Shotton (http://orcid.org/0000-0001-5506-523X)",
       "Silvio Peroni (http://orcid.org/0000-0003-0530-4305)" .
```

**`dc:contributor`** – RECOMMENDED

One or more literals containing the names of the people who contributed to the development of the vocabulary. Whenever possible, each person should be represented as a separate string following the pattern "<Name> <Surname> (<ORCID>)".

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dc:contributor "Paolo Ciccarese (https://orcid.org/0000-0002-5156-2703)",
       "Sebastian Barzaghi (https://orcid.org/0000-0002-0799-1527)",
       "Tim Clark (https://orcid.org/0000-0003-4060-7360)" .
```

**`dcterms:publisher`** – RECOMMENDED

AA link to the organisation responsible for publishing the vocabulary. For the SPAR Ontologies, the publisher is **OpenCitations**, referenced using its Research Organization Registry ID (ROR), i.e. `https://ror.org/00wb4mk85`.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:publisher <https://ror.org/00wb4mk85> .
```

#### Citation

**`bibo:doi`** – RECOMMENDED

A literal containing the Digital Object Identifier (DOI) associated to the vocabulary. Most of the SPAR Ontologies' DOIs have been registered via the [FAIRsharing repository](https://fairsharing.org/).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   bibo:doi "https://doi.org/10.25504/FAIRsharing.b220d4" .
```

**`dcterms:bibliographicCitation`** – RECOMMENDED

A literal containing the text of the citation to either the ontology main scholarly publication, or the ontology itself (if no main scholarly publication is available).

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   dcterms:bibliographicCitation "Peroni, S., Shotton, D. (2012). FaBiO and CiTO: ontologies for describing bibliographic resources and citations. In Journal of Web Semantics, 17: 33-43. https://doi.org/10.1016/j.websem.2012.08.001. Open Access at: https://doi.org/10.2139/ssrn.3198992"@en .
```

#### Visualization

**`foaf:logo`** – OPTIONAL

A link to a logo that represents the vocabulary and helps people quickly identify it.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   foaf:logo <https://github.com/SPAROntologies/cito/blob/master/spar.png> .
```

**`schema:image`** – OPTIONAL

A link to a diagram that visualises the ontology.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   schema:image <https://github.com/SPAROntologies/cito/blob/master/docs/current/cito.png> .
```

#### Related resources

**`owl:imports`** – OPTIONAL

A link to another ontology imported by the ontology.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   owl:imports <http://www.ontologydesignpatterns.org/cp/owl/situation.owl> .
```

**`rdfs:seeAlso`** – RECOMMENDED

A link to related resources. For the SPAR Ontologies, the related resource is usually the HTML page of the ontology on the http://sparontologies.net website.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   rdfs:seeAlso <http://www.sparontologies.net/ontologies/cito> .
```

**`schema:codeRepository`** – OPTIONAL

A link to the public code repository where the vocabulary is maintained. For the SPAR Ontologies, the code repository is the respective GitHub repository in which the documentation of the specific ontology lives.

```turtle
<http://purl.org/spar/cito> a owl:Ontology ;
   schema:codeRepository <https://github.com/SPAROntologies/cito> .
```

### SPAR term metadata checklist

The following annotations describe each class, property and individual defined in a SPAR ontology.

#### Identification

**`rdfs:label`** – REQUIRED

A literal containing a human-readable label of the term. No matter the type of entity identified by the term, the label should _always_ be written in lower case.

```turtle
cito:Citation a owl:Class ;
   rdfs:label "citation"@en .
```

#### Definition

**`rdfs:comment`** – REQUIRED

A literal containing a definition of the term. If the definition has been taken from a specific source (e.g., a dictionary, a website, etc.) that can be reached online, the link to such resource should be provided using the property `rdfs:seeAlso`.

```turtle
cito:Citation a owl:Class ;
   rdfs:comment """
A citation is a conceptual directional link from a citing entity to a cited entity, created by a human performative act of making a citation, typically instantiated by the inclusion of a bibliographic reference (`biro:BibliographicReference`) in the reference list of the citing entity, or by the inclusion within the citing entity of a link, in the form of an HTTP Uniform Resource Locator (URL), to a resource on the World Wide Web.
   """@en .
```

**`skos:note`** – OPTIONAL

A literal containing additional information about the context and/or the usage of the term.

```turtle
cito:Citation a owl:Class ;
   skos:note """
The time span of a citation, i.e. the interval between the publication year of the citing entity and the publication year of the cited entity, can be recorded using the data property `cito:hasCitationTimeSpan`.

The nature or type of a citation can be characterized by using CiTO object properties, e.g. http://purl.org/spar/cito/citesAsDataSource (definition: 'The citing entity cites the cited entity as a source of data').

This CiTO class `cito:Citation` and its accompanying object properties `cito:hasCitingEntity`, `cito:hasCitedEntity` and `cito:hasCitationCharacterization` can be employed to reify direct citation statements made using the CiTO citation object property `cito:cites` or one of its sub-properties.

This usage involved [OWL2 punning](http://www.w3.org/TR/2009/WD-owl2-new-features-20090611/#F12:_Punning), whereby a CiTO object property, such as the aforementioned `cito:extends`, is used as the object of the OWL assertion.

Using punning, the CiTO object property is considered as a proper named individual of the class `owl:Thing`.

Such reification of citation acts can be very useful, since it permits one to combine these CiTO properties with other vocabularies, or to handle situations in which none of the citation characterizations available in CiTO are applicable.

Such situations can be resolved by the creation of a user-defined citation characterization, for example by using the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), as explained at http://semanticpublishing.wordpress.com/2013/07/03/extending-cito-for-open-annotations/.
   """@en .
```

#### Source

**`rdfs:isDefinedBy`** – REQUIRED

A link to the source vocabulary used to define the ontology term.

```turtle
cito:Citation a owl:Class ;
   rdfs:isDefinedBy <http://purl.org/spar/cito> .
```

#### Usage

**`vann:example`** – RECOMMENDED

A literal containing examples of the intended usage of the term. Examples are written following the Turtle syntax and considering Markdown formatting.

```turtle
cito:Citation a owl:Class ;
   vann:example """
   # The following RDF statement

   :paper-a cito:extends :paper-b .

   # can be alternatively described as follows

   :my-citation a cito:Citation ;
       cito:hasCitingEntity :paper-a ;
       cito:hasCitationCharacterization cito:extends ;
       cito:hasCitedEntity :paper-b .
   """ .
```

**`vs:term_status`** – RECOMMENDED

A link to the usage status of the term, e.g. whether the term is mature enough, or whether it has been deprecated, curated, etc. The [Registry Vocabulary](http://purl.org/linked-data/registry) proposes a hierarchy of statuses that may be used for terms as well (`reg:statusStable`, `reg:statusValid`, `reg:statusDeprecated`, etc.).

```turtle
cito:Citation a owl:Class ;
   vs:term_status reg:statusStable .
```

**`vaem:rationale`** – OPTIONAL

A literal containing an explanation of why the term was added to the vocabulary. It considers Markdown formatting.

```turtle
datacite:usesMetadataScheme a owl:ObjectProperty ;
   vaem:rationale """
This is used to represent the particular scheme followed for creating the resource  metadata exemplified in the metadata document, via the property  `datacite:hasMetadataScheme` and the class `datacite:MetadataScheme`.
  
This is also used when the relation type between two resources involves the association of metadata to one by the other.

It is possible to specify a metadata scheme used by the particular metadata document under consideration to describe the metadata of the subject resource or of the related resource.

In addition to specifying a metadata scheme, in this case the metadata document can also be characterised by means of the class `fabio:MetatadaDocument`.

Each metadata scheme is an individual of the class `datacite:MetadataScheme`.  
           """@en .
```

## GitHub guidelines

The GitHub repository of a SPAR ontology must contain a `README.md` file that will include the following template.

```
# <ontology full name> (<ontology acronym>)

<one paragraph description of ontology>

**URL:** http://purl.org/spar/<lowercase ontology acronym>

**Creators**: [<creator full name>](<creator URL - pref. ORCID>), ...

**Contributors:** [<contributor full name>](<contributor URL - pref. ORCID>), ...

**License:** [<license name>](license url)

**Website:** http://www.sparontologies.net/ontologies/<lowercase ontology acronym>

**Cite as:** <bibliographic reference entry, including a DOI link + OA link>

<additional information>
```

This README file must be completed appropriately with all the information required. It is desirable (and requested) that it be updated in a timely manner when necessary.

Some fields between angular brackets are **optional**, since some of the information might be not relevant or available. These are the `Contributors` row (if no contributors in addition to the ontology creators are present), `Cite as` row (if no document/article describing the ontology has yet been published), and the `Additional information` block.  The "additional information" block can contain additional explanatory text about the ontology, and may be structured in subsections.

The repository must also contain a `CHANGELOG.md` file in its root, linked from the ontology via `vann:changes` and structured as described in the [ontology metadata checklist](#spar-ontology-metadata-checklist).

This `CONTRIBUTING.md` file, together with `SUPPORT.md`, `CODE_OF_CONDUCT.md` and the issue and pull request templates, is provided to every repository of the organisation by the [SPAROntologies/.github](https://github.com/sparontologies/.github) repository, and does not need to be copied into the repository of the ontology.

Additionally, a directory `docs` will be created in the master root of the repository. The directory `docs` must contain all the files related to the ontology, its versions in time, and the related documentation. In particular, it must include:

* the `current` directory, where the files of the current version of the ontology are stored;
* one `yyyy-mm-dd` version directory for each of the versions of the ontology developed.

The `current` directory contains five files, named after the lowercase ontology acronym, with the following extensions specifying different formats: `.xml` (RDF/XML), `.ttl` (Turtle), `.nt` (N-Triples), `.jsonld` (JSON-LD), `.html` (HTML, i.e. the human readable documentation of the ontology). All the images used in the documentation should additionally be included in this directory.

The version directories (i.e. `yyyy-mm-dd`) contains the same kinds of files as those included in the `current` directory, but specific for that particular version.

Only the `.ttl` file in the `current` directory is edited by hand. All the other files, and the version directories, are created by two GitHub Actions workflows that every repository must contain in its `.github/workflows` directory. Both call reusable workflows of the [website repository](https://github.com/sparontologies/sparontologies.github.io/tree/master/.github/workflows):

* `validation.yml` runs on every push and pull request to the master branch. It checks that the ontology is well written, consistent, in OWL 2 DL and FAIR compliant;
* `release.yml` runs on every push to the master branch that changes the `.ttl` file in the `current` directory. It generates the other serialisations and the HTML documentation in the `current` directory using [LODE 2.0](https://lode.opencitations.net/), copies the `current` directory into a new version directory named after the value of `dcterms:modified`, updates the version in `CITATION.cff` and `pyproject.toml` according to `owl:versionInfo`, and creates a GitHub release named `v<owl:versionInfo>`. For this reason, the repository must also contain a `CITATION.cff` file and a `pyproject.toml` file.

To add these workflows to a new repository, copy them from an existing SPAR Ontologies repository, e.g. the [one for FaBiO](https://github.com/sparontologies/fabio/tree/master/.github/workflows), and replace the path of the ontology file in `release.yml`.

Note that the rest of the repository can be organised as preferred. The important thing is that it contains the `README.md` and the `docs` directory in the master root of the repository, as indicated above. For an example of the mandatory organisation of the repository, please see one of the existing SPAR Ontologies repositories, e.g. the [one for CiTO](https://github.com/sparontologies/cito/).

## Website guidelines

Once the ontology is ready and published on GitHub, it is necessary to add the appropriate information in the [website repository](https://github.com/sparontologies/sparontologies.github.io), so that the new ontology is made available online. In particular, there are some files that should be added, as illustrated as follows. The same files must be kept up to date when a new version of the ontology changes what they describe.

All the files must be added or modified via Git pull requests, and all the fields between angle brackets in the templates below must be filled in appropriately. Images used in descriptions, such as explanatory diagrams (recommended), should be added in the [`static/img/spar` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/static/img/spar).

### Add a new description

A new `.txt` file must be added in the [`spar/ontology_descriptions` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_descriptions). This file must be named after the lowercase acronym of the ontology (which corresponds to the assigned GitHub repository).

This file must be structured according to the following template:

```
#name <ontology name>

#acronym <ontology acronym>

#url http://purl.org/spar/<lowercase ontology acronym>

#source https://sparontologies.github.io/<lowercase ontology acronym>/current/<lowercase ontology acronym>.ttl

#documentation http://purl.org/spar/<lowercase ontology acronym>.html

#repository https://github.com/sparontologies/<lowercase ontology acronym>

#description <textual/markdown description of the ontology>
```

This file will be used as the body of the related page for the new ontology in the SPAR website.

In addition, in order to be actually included in the list of the ontologies available at http://www.sparontologies.net/ontologies, it is mandatory to add a particular issue at the [sparontologies.github.io repository](https://github.com/sparontologies/sparontologies.github.io/issues), specifying "DESC" plus the name of the ontology as title of the issue, assigning the label *new description*, and specifying a one-sentence description as content of the message. This one-sentence description will be added in the last list of the http://www.sparontologies.net/ontologies page.

### Add new examples

A new `.txt` file must be added in the [`spar/ontology_examples` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_examples). This file must be named after the lowercase acronym of the ontology (which corresponds to the assigned GitHub repository).

This file must be structured according to the following template:

```
#id <short id of the first example>

#title <title of the first example>

#description <textual/markdown description of the first example>

#code <Turtle code of the first example>

#id <short id of the second example>

#title <title of the second example>

#description <textual/markdown description of the second example>

#code <Turtle code of the second example>

...
```

It is possible to add one, two or more examples in the same file.

This file will be used to populate the [example page](http://www.sparontologies.net/examples) as well as the final part of the related page describing the ontology in the website.

### Add the new acronym

The [`acronyms.txt` file](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_publications/acronyms.txt) must be modified so as to include a simple acronym identifier that can be used to refer to the ontology in the website. The new row in the file must be compliant with the following template:

```
#<lowercase ontology acronym> <ontology acronym>: <ontology name>
```

### Add publications (if any)

The [`publication_list.txt` file](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_publications/publication_list.txt) must be modified so as to add references to one or more publications related to the ontology. Each publication should be specified by using the following template:

```
#bibref <bibliographic reference of the publication>

#oa <URL of the open access version of the publication>

#main <lowercase ontology acronym>

#secondary <lowercase ontology acronym>

#description <textual/markdown description of the publication>
```

The bibliographic reference should include a link (e.g. a DOI link) to the publication. In case that link points to a closed access version of the publication, the URL of the open access version of the same publication should be specified (field `#oa`). If this field is missing, the bibliographic reference specified is assumed to be an open access article, and an appropriate label will be added in the website automatically. At least one of the fields `#main` and `#secondary` must be specified, so as to indicate if the publication is the main one describing the ontology in consideration, or only a secondary one. Finally, the description is always a mandatory field.
