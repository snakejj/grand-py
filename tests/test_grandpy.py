#! /usr/bin/env python3
# coding: utf-8

#! /usr/bin/env python3
# coding: utf-8

from grandpy.grandpy import Grandpy


class TestGrandpy:
    def test_grandpy_getting_all_informations_in_a_list(self, monkeypatch):
        def mock_clean_input(raw_question):
            return "Tour Eiffel"

        def mock_getting_sorted_informations(clean_input):
            return [
                "Tour Eiffel",
                [48.85824, 2.2945],
                None,
                "adresse de la Tour Eiffel"
            ]

        def mock_article_id_from_sorted_raw_info(gps_coordinate):
            return 4641538

        def mock_getting_extract_and_url_from_closest_wiki_page(
            gps_coordinate, pageid
        ):
            return [
                "Le Jules Verne est un restaurant parisien situé au deuxième "
                "étage de la tour Eiffel et spécialisé en cuisine française "
                "classique. Le chef Frédéric Anton est aux manettes depuis "
                "juillet 2019. Il succède à Louis Grondard (1983), Alain Reix "
                "(1992) et Alain Ducasse avec Sodexo (2007).\nLe décor a été "
                "réalisé…",
                "https://fr.wikipedia.org/wiki/Le_Jules_Verne"
            ]

        def mock_choice(answer):
            return answer[0]

        monkeypatch.setattr(
            "grandpy.parser.Parser.clean_input",
            mock_clean_input
        )
        monkeypatch.setattr(
            "grandpy.api.api.Here.getting_sorted_informations",
            mock_getting_sorted_informations
        )
        monkeypatch.setattr(
            "grandpy.api.api.Wiki.article_id_from_sorted_raw_info",
            mock_article_id_from_sorted_raw_info
        )

        monkeypatch.setattr(
            "grandpy.api.api."
            "Wiki.getting_extract_and_url_from_closest_wiki_page",
            mock_getting_extract_and_url_from_closest_wiki_page
        )

        monkeypatch.setattr(
            "random.choice",
            mock_choice
        )

        test_return = Grandpy("Bonjour papy, ou se trouve la Tour Eiffel ?")

        assert test_return.grandpy() == {
            "address": "adresse de la Tour Eiffel",
            "title": "Tour Eiffel",
            "latitude": 48.85824,
            "longitude": 2.2945,
            "mapapi": None,
            "articleextract": "Le Jules Verne est un restaurant parisien "
            "situé au deuxième étage de la tour Eiffel et spécialisé en "
            "cuisine française classique. Le chef Frédéric Anton est aux "
            "manettes depuis juillet 2019. Il succède à Louis Grondard (1983),"
            " Alain Reix (1992) et Alain Ducasse avec Sodexo (2007).\nLe décor"
            " a été réalisé…",
            "urlarticle": "https://fr.wikipedia.org/wiki/Le_Jules_Verne",
            "grandpyanecdote": "Tiens d'ailleurs, j'ai une anecdote "
            "interessante:",
            "grandpyanswer": "Tour Eiffel? Bien sur mon enfant, "
            "voici l'adresse: adresse de la Tour Eiffel",
        }
