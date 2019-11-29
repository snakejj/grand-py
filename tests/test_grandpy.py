#! /usr/bin/env python3
# coding: utf-8

from grandpy.grandpy import Grandpy


class TestGrandpy:
    def test_grandpy_getting_all_informations_in_a_list(self, monkeypatch):
        def mock_choice(answer):
            return answer[0]

        monkeypatch.setattr("random.choice", mock_choice)

        test_return = Grandpy("Bonjour papy, ou se trouve la Tour Eiffel ?")
        print(test_return)
        assert test_return == {
            "title": "Tour Eiffel",
            "gps": {
                "latitude": 48.85824,
                "longitude": 2.2945
            },
            "article_extract": "Le Jules Verne est un restaurant parisien situé au deuxième étage de la tour Eiffel et spécialisé en cuisine française classique. Le chef Frédéric Anton est aux manettes depuis juillet 2019. Il succède à Louis Grondard (1983), Alain Reix (1992) et Alain Ducasse avec Sodexo (2007).\nLe décor a été réalisé…",
            "url_article": "https://fr.wikipedia.org/wiki/Le_Jules_Verne",
            "error": "Je suis un peu dur de la feuille, peux tu reformuler ?",
            "grandpy-answer": "Tour Eiffel? Bien sur, je te montre une carte, c'est plus parlant."
        }

