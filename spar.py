# -*- coding: utf-8 -*-
__author__ = 'essepuntato'
import web
import os
from hashformat import process_hashformat
from ldd import LinkedDataDirector
from operator import itemgetter
from wl import WebLogger
from oh import OntologyHandler

# Vars
base_path = "spar" + os.sep
ontology_base_path = base_path + os.sep + "ontology_descriptions" + os.sep
documentation_base_path = base_path + os.sep + "ontology_documentations" + os.sep
example_base_path = base_path + os.sep + "ontology_examples" + os.sep
publications_base_path = base_path + os.sep + "ontology_publications" + os.sep
publication_list_path = publications_base_path + "publication_list.txt"
citing_paper_list_path = publications_base_path + "citing_list.txt"
projects_list_path = publications_base_path + "projects.txt"
acronyms_path = publications_base_path + "acronyms.txt"
mediatype_base_path = "mediatype" + os.sep
mediatype_base_url = "https://w3id.org/spar/mediatype/"
ontologies_base_url = "http://www.sparontologies.net/ontologies/"
# ontologies_base_url = "http://localhost:8181/ontologies/"
# mediatype_base_url = "http://localhost:8080/mediatype/"
tmp_dir_for_copying_rdf = os.path.expanduser("~")
src_fragment = "/source"

# For redirecting
urls = (
    "/", "Home",
    "/robots.txt", "Robots",
    "/ontologies/?(.*)", "Ontologies",
    "/examples/?", "Examples",
    "/publications/?", "Publications",
    "/uptake/?", "Uptake",
    "/contacts/?", "Contacts",
    "/about/?", "About",
    "/mediatype/(.+)", "MediaType",
    "/mediatype/?", "MediaType"
)

# For rendering
render = web.template.render(base_path)

# Page URLs and their name
pages = [
    {
        "url": "/ontologies",
        "title": "Ontologies"
    },
    {
        "url": "/examples",
        "title": "Examples"
    },
    {
        "url": "/publications",
        "title": "Publications"
    },
    {
        "url": "/uptake",
        "title": "Communities Uptake"
    },
    {
        "url": "/contacts",
        "title": "Contacts"
    },
    {
        "url": "/about",
        "title": "About"
    }
]

web_logger = WebLogger("sparontologies.net", "sparontologies_log.txt", [
    "REMOTE_ADDR",      # The IP address of the visitor
    "HTTP_USER_AGENT",  # The browser type of the visitor
    "HTTP_REFERER",     # The URL of the page that called your program
    "HTTP_HOST",        # The hostname of the page being attempted
    "REQUEST_URI"       # The interpreted pathname of the requested document
                        # or CGI (relative to the document root)
    ],
    {"REMOTE_ADDR": ["212.47.249.17"]}  # uncomment this for real app
    # {"REMOTE_ADDR": ["127.0.0.1"]}  # uncomment this for test
)


class Home:
    def GET(self):
        web_logger.mes()
        return render.home("SPAR Ontologies - Home", pages)

class Robots:
    def GET(self):
        raise web.seeother('/static/robots.txt')

class Publications:
    def GET(self):
        spar_acronym = "spar"
        spar_title = "Semantic Publishing and Referencing (SPAR) Ontologies"
        acronyms_dict = process_hashformat(acronyms_path)[0]
        acron_list = sorted(acronyms_dict.keys())
        acron_list.insert(0, "spar")
        acronyms_dict[spar_acronym] = spar_title
        web_logger.mes()
        return render.publications(
            "SPAR Ontologies - Publications", pages,
            acron_list,
            acronyms_dict,
            process_hashformat(publication_list_path))


class Uptake:
    def GET(self):
        web_logger.mes()
        return render.uptake(
            "SPAR Ontologies - Publications", pages,
            sorted(process_hashformat(projects_list_path), key=itemgetter('name')),
            sorted(process_hashformat(citing_paper_list_path), key=itemgetter('title')))


class Contacts:
    def GET(self):
        web_logger.mes()
        return render.contacts("SPAR Ontologies - Contacts", pages)


class About:
    def GET(self):
        web_logger.mes()
        return render.about("SPAR Ontologies - About", pages)


class Examples:
    def GET(self):
        all_examples = []
        for cur_dir, cur_subdir, cur_files in os.walk(example_base_path):
            for cur_file in cur_files:
                if cur_file.endswith(".txt"):
                    cur_example_list = process_hashformat(cur_dir + cur_file)
                    all_examples += cur_example_list
        web_logger.mes()
        return render.examples("SPAR Ontologies - Examples", pages, all_examples)


class Ontologies:
    def get_ontology_url(self):
        result = {}

        for cur_dir, cur_subdir, cur_files in os.walk(ontology_base_path):
            for cur_file in cur_files:
                if cur_file.endswith(".txt"):
                    cur_hash = process_hashformat(cur_dir + os.sep + cur_file)[0]
                    result[cur_file.replace(".txt", "")] = cur_hash["source"]

        result["bido-research-career-category"] = \
            "http://svn.code.sf.net/p/sempublishing/code/BiDO/bido-rcc.owl"

        result["bido-standard-bibliometric-measures"] = \
            "http://svn.code.sf.net/p/sempublishing/code/BiDO/bido-sbm.owl"

        result["bido-review-measures"] = "http://svn.code.sf.net/p/sempublishing/code/BiDO/bido-rm.owl"

        result["bido-core"] = "http://svn.code.sf.net/p/sempublishing/code/BiDO/bido-core.owl"

        result["pwo-alignment"] = "http://svn.code.sf.net/p/sempublishing/code/PWO/pwo-alignment.owl"

        result["pattern"] = "http://svn.code.sf.net/p/dwellonit/code/StructuralPattern/pattern.owl"

        return result

    def GET(self, onto_acronym):
        if onto_acronym is not None and onto_acronym.strip() != "":
            ontology_path = ontology_base_path + onto_acronym + ".txt"
            example_path = example_base_path + onto_acronym + ".txt"
            if os.path.exists(ontology_path) and os.path.exists(example_path):
                cur_ontology_dict = process_hashformat(ontology_path)[0]
                cur_example_list = process_hashformat(example_path)
                web_logger.mes()
                return render.ontology("SPAR Ontologies - ", pages,
                                       cur_ontology_dict["name"],
                                       cur_ontology_dict["acronym"],
                                       cur_ontology_dict["url"],
                                       cur_ontology_dict["documentation"],
                                       cur_ontology_dict["repository"],
                                       cur_ontology_dict["description"],
                                       cur_example_list,
                                       process_hashformat(publication_list_path),
                                       onto_acronym)
            else:
                raise web.notfound()
        else:  # Load home
            web_logger.mes()
            return render.ontologies(
                "SPAR Ontologies - Ontologies", pages,
                process_hashformat(publication_list_path),
                "spar")


class MediaType:
    def GET(self, file_path=None):
        director = LinkedDataDirector(
            mediatype_base_path, mediatype_base_url,
            label_conf={
                "http://purl.org/spar/pso/holdsStatusInTime": "status in time",
                "http://purl.org/spar/cito/isDescribedBy": "described",
                "http://purl.org/spar/cito/isDocumentedBy": "rfc",
                "http://purl.org/dc/terms/relation": "related",
                "http://purl.org/dc/terms/MediaType": "media type",
                "http://purl.org/dc/terms/contributor": "contributor",
                "http://xmlns.com/foaf/0.1/Agent": "agent",
                "http://xmlns.com/foaf/0.1/name": "name",
                "http://xmlns.com/foaf/0.1/homepage": "homepage",
                "http://purl.org/spar/pso/withStatus": "status",
                "http://purl.org/spar/pso/Status": "status",
                "http://purl.org/spar/pso/StatusInTime": "status in time",
                "http://purl.org/dc/terms/title": "title",
                "http://purl.org/spar/fabio/Expression": "expression",
                "http://purl.org/dc/terms/license": "license",
                "http://creativecommons.org/licenses/by/4.0/":
                    "Creative Commons Attribution 4.0 International License (CC BY 4.0)"},
            tmp_dir=tmp_dir_for_copying_rdf)
        if file_path is None:
            web_logger.mes()
            return director.get_render().index()
        else:
            cur_page = director.redirect(file_path)
            if cur_page is None:
                raise web.notfound()
            else:
                web_logger.mes()
                return cur_page


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
