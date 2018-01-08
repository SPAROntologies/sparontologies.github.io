# SPAR Ontologies community guidelines

This document introduce the aforementioned guidelines:

* [participation guidelines](#participation-guidelines), i.e. the rules with which an ontology must be compliant to be included in the SPAR Ontologies;

* [GitHub guidelines](#github-guidelines), i.e. the process to follow for making the ontology available in the SPAR Ontology GitHub repository;

* [website guidelines](#website-guidelines), i.e. the additional material necessary to be added in the [SPAR Ontologies official website](http://www.sparontologies.net).

Please read these guidelines **carefully** before proposing a new ontology to be included within the SPAR Ontologies.

To propose a new ontology (or an existing one) to be included within the family of SPAR Ontologies, you have to open a new issue at the [sparontologies.github.io repository](https://github.com/sparontologies/sparontologies.github.io/issues), specifying "NEW" plus the name of the ontology as title of the issue, assigning the label *new ontology*, and filling up the content of the issue using the following template:

```
**Name:** <full name of the ontology>

**Acronym:** <ontology acronym>

**Proponent(s):** [<proponent full name>](<GitHub user URL>), ...

<free text description of the ontology, where you specify
 precisely its purpose and scope, the ontology development process adopted, and any other useful information 
 for assessing it>
```

All the fields between angle brackets included in the aforementioned template must be substituted with the appropriate text. All the fields are mandatory.

All the requests will be evaluated by the [owners](https://github.com/orgs/SPAROntologies/people?utf8=%E2%9C%93&query=+role%3Aowner) of the SPAR Ontologies GitHub organisation. It is possible for a new proposal to have a few iterative responses before being given a final response on whether or not the proposed ontology is accepted into SPAR. If the response is positive, then a new GitHub repository within the SPAR Ontologies organisation will be created using the ontology acronym, and a new purl.org URL will be made available for that ontology.


## Participation rules

There are the rules that a candidate ontology (*CO* from now on) must follow in order to be eligible to be part of the SPAR Ontologies:

1. CO should cover a specific and limited area of interest within the domain of scholarly publishing and referencing (widely interpreted);
1. CO must be orthogonal, non-overlapping, complementary and interoperable with existing SPAR Ontologies;
1. CO should acts primarily as a structured defined vocabulary, and should thus be extensive enough to cover vocabulary terms in common and professional usage;
1. CO must be well-developed, accurate and explicit, and must have unambiguous explanatory English-language definitions for all classes, properties, and individuals it describes;
1. CO must be given a name ("The *** Ontology") appropriate to its purpose, and a clear short acronym based on that name. The acronym must contain no spaces or special characters - only English alphabetic characters, numerals, and the character "-" are admissible;
1. CO must be written in OWL 2 DL;
1. CO IRI must be composed by `http://purl.org/spar/` plus the lowercase string of its acronym (additional characters at the end, e.g. `/`, are not permitted);
1. CO Version IRI (`owl:versionIRI`) must be composed by the CO IRI plus `/` plus the [ISO date](https://en.wikipedia.org/wiki/ISO_8601) `yyyy-mm-dd` referring to the publication date of that particular version;
1. CO must include an explicit reference (via `owl:priorVersion`) to its previous version, if any;
1. CO entity IRI of each entity defined in CO (not any imported ones) must be composed by the CO IRI plus `/` plus the entity local IRI (only English alphabetic characters and numberals are admissible) defined as prescribed in the [SAMOD methodology](https://w3id.org/people/essepuntato/papers/samod-owled2016.html):
    >Class names local to the ontology (i.e. not imported) must be capitalised (e.g. *Justification*) and adopt camel-case notation if composed of more than one word (e.g. *DescriptionOfVagueness*).  Property names local to the ontology (i.e. not imported) must start with a non-capitalised verb and adopt camel-case notation if composed of more than one word (e.g. *wasAttributedTo*).  Local names of Individuals must be non-capitalised (e.g. *ceo*) and dash-separated if composed by more than one word (e.g. *quantitative-vagueness*). 
1. CO must have a minimal use of domain and range constraints when possible, to permit unanticipated uses;
1. CO may import and reuse, or should complement, well-known and well-used third party vocabularies, e.g. DC Elements, FOAF, SKOS, FRBR;
1. CO must be released according to an open access license compatible with the [Creative Commons Free Cultural Works guidelines](https://creativecommons.org/share-your-work/public-domain/freeworks);
1. CO must be rendered human-readable in HTML (e.g. produced by means of [LODE](http://www.essepuntato.it/lode) or [Widoco](https://github.com/dgarijo/Widoco));
1. CO should be accompanied by one or more explanatory diagrams (e.g. in [Graffoo](http://www.essepuntato.it/graffoo) or [VOWL](http://vowl.visualdataweb.org/))
1. CO must be available in at least four RDF formats, i.e. Turtle, N-triples, RDF/XML, and JSON-LD;
1. CO must be stored in the SPAR Ontology GitHub repository, following a precise structure so as to keep track also of its versions and evolution – see the [GitHub guidelines](#github-guidelines).
1. CO must be described by a specific page on the SPAR Ontology website that should also include Turtle examples of usage – see the [website guidelines](#website-guidelines);
1. The authorship of CO must be specified within the ontology itself, and the names and contact details of the authors of CO must be clearly stated on the ontology in proper annotations (e.g. in comments or descriptions associated to the ontology).

## GitHub guidelines

The GitHub repository for CO must contain a README.md file that will include the following template.

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

This readme file must be completed appropriately with all the information required. It is desirable (and requested) that it be updated in a timely manner when necessary. Some fields between angular brackets are optional, since some of the information might be not relevant or available. These are the "contributors" row (if no contributors in addition to the ontology creators are present), "cite as" row (if no document/article describing the ontology has yet been published), and the "additional information" block.  The "additional information" block can contain additional explanatory text about the ontology, and may be structured in subsections.

Additionally, a directory `docs` will be created in the master root of the repository. The directory `docs` must contain all the files related to the ontology, its versions in time, and the related documentations. In particular, it must must include:

* the `current` directory, where the files of the current version of the ontology are stored;
* one `yyyy-mm-dd` version directory for each of the versions of the ontology developed.

The `current` directory must contain a `.owl` file named after the lowercase ontology acronym, which is the source of the ontology in a particular format. The choice of format used for this file must be between RDF/XML, Turtle, N-triples, or JSON-LD. In addition to this file, the directory must include five other files, named in the same way and with the following extensions specifying each of five different formats: `.xml` (RDF/XML), `.ttl` (Turtle), `.nt` (Ntriple), `.json` (JSON-LD), `.html` (HTML, i.e. the human readable documentation of the ontology). All the images used in the documentation should additionally be included in this `.html` directory.

The version directories (i.e. `yyyy-mm-dd`) must contains the same kinds of files as those included in the `current` directory, but specific for that particular version.  However, the `.owl` file should be present only in the `current` directory.

In order to facilitate the creation of all these other files starting from the master `.owl` file, some Python scripts have been made available at https://github.com/SPAROntologies/spar-script. In particular:

* `gerfo.py` allows one to create the various formats (i.e. RDF/XML, Turtle, N-triples, and JSON-LD) for the input ontology (that must be stored in one of these formats as well);
* `sl.py` allows one to create the natural language HTML documentation by using [LODE](http://www.essepuntato.it/lode) – it is necessary to be connected to the Internet, the ontology must be already available on the Web, and the directory `imports` (available at https://github.com/sparontologies/spar-script/tree/master/imports) must be first be copied into the directory `docs`.

Note that the rest of the repository can be organised as preferred. The important thing is that it contains the `README.md` and the `docs` directory in the master root of the repository, as indicated above. For an example of the mandatory organisation of the repository, please see one of the existing SPAR Ontologies repositories, e.g. the [one for CiTO](https://github.com/sparontologies/cito/). 

## Website guidelines

Once the ontology is ready and published on GitHub, it is necessary to add the appropriate information in the [website repository](https://github.com/sparontologies/sparontologies.github.io), so that the new ontology is made available online. In particular, there are some files that should be added, as illustrated as follows.

### Add a new description

A new `.txt` file must be added (via a Git pull request) in the [`spar/ontology_descriptions` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_descriptions). This file must be named after the lowercase acronym of the ontology (which corresponds to the assigned GitHub repository).

This file must be structured according to the following template:

```
#name <ontology name>

#acronym <ontology acronym>

#url http://purl.org/spar/<lowercase ontology acronym>

#source https://sparontologies.github.io/<lowercase ontology acronym>/current/<lowercase ontology acronym>.owl

#documentation http://purl.org/spar/<lowercase ontology acronym>.html

#repository https://github.com/sparontologies/<lowercase ontology acronym>

#description <textual/markdown description of the ontology>
```

All the fields between angle brackets must be filled in appropriately. If the description includes some images, such as explanatory diagrams (recommended), they should be added in the [`static/img/spar` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/static/img/spar) (via pull requests).

This file will be used as the body of the related page for the new ontology in the SPAR website. 

In addition, in order to be actually included in the list of the ontologies available at http://www.sparontologies.net/ontologies, it is mandatory to add a particular issue at the [sparontologies.github.io repository](https://github.com/sparontologies/sparontologies.github.io/issues), specifying "DESC" plus the name of the ontology as title of the issue, assigning the label *new description*, and specify a one-sentence description as content of the message. This one sentence description will be added in the last list of the http://www.sparontologies.net/ontologies page.

### Add new examples

A new `.txt` file must be added (via a Git pull request) in the [`spar/ontology_examples` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_examples). This file must be named after the lowercase acronym of the ontology (which corresponds to the assigned GitHub repository).

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

All the fields between angle brackets must be filled in appropriately.  It is possible to add one, two or more examples in the same file. If the description includes some images, they should be added in the [`static/img/spar` directory](https://github.com/sparontologies/sparontologies.github.io/tree/master/static/img/spar) (via pull requests).

This file will be used to populate the [example page](http://www.sparontologies.net/examples) as well as the the final part of the related page describing the ontology in the website. 

### Add the new acronym

The [`acronyms.txt` file](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_publications/acronyms.txt) must be modified (via a Git pull request) so as to include a simple acronym identifier that can be used to refer to the ontology in the website. The new row in the file must be compliant with the following template:

```
#<lowercase ontology acronym> <ontology acronym>: <ontology name>
```

All the fields between angle brackets must in filled in appropriately.

### Add publications (if any)

The [`publication_list.txt` file](https://github.com/sparontologies/sparontologies.github.io/tree/master/spar/ontology_publications/publication_list.txt) must be modified (via a Git pull request) so as to add references to one or more publications related to the ontology. Each publication should be specified by using the following template:

```
#bibref <bibliographic reference of the publication>

#oa <URL of the open access version of the publication>

#main <lowercase ontology acronym>

#secondary <lowercase ontology acronym>

#description <textual/markdown description of the publication>
```

All the fields between angle brackets must be filled in appropriately. In particular, the bibliographic reference should include a link (e.g. a DOI link) to the publication. In case that link points to a closed access version of the publication, the URL of the open access version of the same publication should be specified (field `#oa`). If this field is missing, the bibliographic reference specified is assumed to be an open access article, and an appropriate label will be added in the website automatically. At least one of the fields `#main` and `#secondary` must be specified, so as to indicate if the publication is the main one describing the ontology in consideration, or only a secondary one. Finally, the description is always a mandatory field.

