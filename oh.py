# -*- coding: utf-8 -*-
__author__ = 'essepuntato'

from xml.sax import SAXParseException
import web
import rdflib
import os
import re


class OntologyHandler(object):
    __extensions = (".rdf", ".ttl", ".json", ".html")
    __rdfxml = ("application/rdf+xml",)
    __turtle = ("text/turtle", "text/n3")
    __jsonld = ("application/ld+json", "application/json")

    def __init__(self, baseurl, src, doc_basepath, ontomap):
        self.baseurl = baseurl
        self.src = src
        self.doc_basepath = doc_basepath
        self.ontomap = ontomap

    def log(self):
        if self.logger is not None:
            self.logger.mes()

    def get_render(self):
        return self.render

    def redirect(self, url):
        if url.endswith(self.__extensions):
            return self.get_representation(url)
        else:
            content_type = web.ctx.env.get("HTTP_ACCEPT")
            if content_type:
                for accept_block in content_type.split(";")[::2]:
                    accept_types = accept_block.split(",")

                    if any(mime in accept_types for mime in self.__rdfxml):
                        raise web.seeother(url + ".rdf")
                    elif any(mime in accept_types for mime in self.__turtle):
                        raise web.seeother(url + ".ttl")
                    elif any(mime in accept_types for mime in self.__jsonld):
                        raise web.seeother(url + ".json")
                    else:  # HTML
                        raise web.seeother(url + ".html")

    def get_representation(self, url):
        # URL = [base]/[acronym]/[src]
        ontology_acronym = re.sub("^%s/?(.+)/?%s.+$" % (self.baseurl, self.src), "\\1", url)
        if ontology_acronym is not None:
            if url.endswith(".html"):
                doc_file = self.doc_basepath + os.sep + ontology_acronym + ".html"
                if os.path.exists(doc_file):
                    with open(doc_file) as f:
                        return f.read()
            elif ontology_acronym in self.ontomap:
                ontology_url = self.ontomap[ontology_acronym]
                cur_graph = OntologyHandler.load_graph(ontology_url)
                if len(cur_graph):
                    if url.endswith(".rdf"):
                        return cur_graph.serialize(format="xml")
                    elif url.endswith(".ttl"):
                        return cur_graph.serialize(format="turtle")
                    elif url.endswith(".json"):
                        return cur_graph.serialize(format="json-ld")

    @staticmethod
    def load_graph(ontology_url):
        current_graph = rdflib.Graph()

        try:
            current_graph.load(ontology_url)
        except SAXParseException:
            try:
                current_graph.load(ontology_url, format="turtle")
            except Exception as e:
                raise e
        except Exception as e:
            raise e

        return current_graph