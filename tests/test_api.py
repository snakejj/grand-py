#! /usr/bin/env python3
# coding: utf-8

from grandpy.api.api import Here, Wiki


class TestHere:
    def test_here_getting_sorted_informations(self, monkeypatch):
        class MockGet:
            def __init__(self, url, params):
                pass

            def json(self):
                return {
                    "results": {
                        "items": [
                            {
                                "position": [48.85824, 2.2945],
                                "bbox": 846,
                                "distance": 8252,
                                "title": "La Défense",
                                "category": "{Ville ou village}",
                                "icon": "https://download.vcdn.cit.data.com"
                                "om/p/d/places2_stg/icons/categories/35.icon",
                                "vicinity": "Hauts-de-Seine, Île-de-France",
                                "having": [],
                                "type": "urn:nlp-types:place",
                                "href": "https://places.cit.api.here.com/pes/",
                                "id": "loc-dmVyc2lvbj0xO3RpdGxlPUxhK0QlMlQDS",
                                "authoritative": "true",
                            }
                        ]
                    },
                    "search": {
                        "context": {"urn": "nlp-types:place"},
                        "ranking": "default",
                    },
                }

        monkeypatch.setattr("requests.get", MockGet)

        here_instance = Here("la defense")

        assert here_instance.getting_sorted_informations()[0] == "La Défense"
        assert here_instance.getting_sorted_informations()[1] == [
            48.85824,
            2.2945,
        ]
        assert (
            here_instance.getting_sorted_informations()[2] == "https://"
            "places.cit.api.here.com/pes/"
        )


class TestWiki:
    def test_wiki_getting_article_id(self, monkeypatch):
        class MockGet:
            def __init__(self, url, params):
                pass

            def json(self):
                return {
                    "batchcomplete": "",
                    "query": {
                        "geosearch": [
                            {
                                "pageid": 6422233,
                                "ns": 0,
                                "title": "Academy of Art University",
                                "lat": 37.78785,
                                "lon": -122.40065,
                                "dist": 129.9,
                                "primary": "",
                            },
                            {
                                "pageid": 5105544,
                                "ns": 0,
                                "title": "101 Second Street",
                                "lat": 37.788139,
                                "lon": -122.399056,
                                "dist": 140.9,
                                "primary": "",
                            },
                        ]
                    },
                }
        monkeypatch.setattr("requests.get", MockGet)

        wiki_instance = Wiki(37.786971, -122.399677)

        assert wiki_instance.article_id_from_sorted_raw_info() == 6422233

    def test_wiki_getting_extract_and_url_from_wiki_page(self, monkeypatch):
        class MockGet:
            def __init__(self, url, params):
                pass

            def json(self):
                return {
                    "batchcomplete": "",
                    "warnings": {
                        "extracts": {
                            "*": '"exlimit" was too large for a whole articl'
                            "e extracts request, lowered to 1."
                        }
                    },
                    "query": {
                        "pages": {
                            "6422233": {
                                "pageid": 6422233,
                                "ns": 0,
                                "title": "Academy of Art University",
                                "extract": "L\u2019Academy of Art University",
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2019-11-23T20:08:34Z",
                                "lastrevid": 144038875,
                                "length": 2115,
                                "fullurl": "https://fr.wikipedia.org/wiki/Acad"
                                "emy_of_Art_University",
                                "editurl": "https://fr.wikipedia.org/w/index.p"
                                "hp?title=Academy_of_Art_University&action=edi"
                                "t",
                                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Academy_of_Art_University",
                            }
                        }
                    },
                }

        monkeypatch.setattr("requests.get", MockGet)

        wiki_instance = Wiki(37.786971, -122.399677)

        assert (
            wiki_instance.getting_extract_and_url_from_closest_wiki_page(
                6422233) == (
                "L\u2019Academy of Art University",
                "https://fr.wikipedia.org/wiki/Academy_of_Art_University"
            )
        )
