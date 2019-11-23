#! /usr/bin/env python3
# coding: utf-8

from api.api import Here


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
                                "type":"urn:nlp-types:place",
                                "href": "https://places.cit.api.here.com/pes/",
                                "id":"loc-dmVyc2lvbj0xO3RpdGxlPUxhK0QlQzMlQDS",
                                "authoritative":"true",
                            }
                        ]
                    },
                    "search": {
                        "context": {"urn": "nlp-types:place"},
                        "ranking": "default",
                        }
                }

        monkeypatch.setattr("requests.get", MockGet)

        here_instance = Here('la defense')
        
        assert here_instance.getting_sorted_informations()[0] == 'La Défense'
        assert here_instance.getting_sorted_informations()[1] == [
            48.85824,
            2.2945
            ]
        assert here_instance.getting_sorted_informations()[2] == "https://" \
            "places.cit.api.here.com/pes/"
