import random

from grandpy.parser import Parser
from grandpy.api.api import Here, Wiki
from grandpy.api.configapi import HERE_JS_MAP


class Grandpy:

    def __init__(self, raw_question):
        self.raw_question = raw_question

    def grandpy(self):
        # error list
        list_error = [
            "Je suis un peu dur de la feuille, peux tu reformuler ?",
            "Je ne suis pas sur de comprendre, peux tu le dire autrement ?",
            "Argh, Alzheimer quand tu nous tiens.. reformules veux tu ?"
        ]

        # Answer list
        list_answer = [
            "Bien sur mon enfant, voici l'adresse:",
            "Pas de souci, je te donne l'adresse mon enfant:",
            "Il n'y a pas de probleme mon enfant, voila l'adresse:"
        ]

        # Anecdote list
        list_anecdote = [
            "Tiens d'ailleurs, j'ai une anecdote interessante:",
            "A ce propos, j'ai une petite info pour toi:",
            "Le savais-tu ?"
        ]

        # Parser
        parser = Parser(self.raw_question)
        clean_question = parser.clean_input()

        # Here
        here = Here(clean_question)
        sorted_informations = here.getting_sorted_informations()
        if here.error:
            return {
                "grandpyerror": random.choice(list_error)
            }
        else:
            title = sorted_informations[0]
            latitude = sorted_informations[1][0]
            longitude = sorted_informations[1][1]
            address = sorted_informations[3]

        # Wiki
        wiki = Wiki(latitude, longitude)
        page_id = wiki.article_id_from_sorted_raw_info()
        full_extract = wiki.getting_extract_and_url_from_closest_wiki_page(
            page_id
        )

        article_extract = full_extract[0]
        url = full_extract[1]

        return {
            "title": title,
            "latitude": latitude,
            "longitude": longitude,
            "address": address.replace('<br/>', ', '),
            "mapapi": HERE_JS_MAP,
            "articleextract": article_extract,
            "urlarticle": url,
            "grandpyanecdote": random.choice(list_anecdote),
            "grandpyanswer": (
                f"{title}? "
                f"{random.choice(list_answer)} "
                f"{address.replace('<br/>', ', ')}"
            )

        }
