import random

from grandpy.parser import Parser
from grandpy.api.api import Here, Wiki


class Grandpy:

    def __init__(self, raw_question):
        self.raw_question = raw_question

    def grandpy(self):
        # Parser
        parser = Parser(self.raw_question)
        clean_question = parser.clean_input()

        # Here
        here = Here(clean_question)
        sorted_informations = here.getting_sorted_informations()

        title = sorted_informations[0]
        latitude = sorted_informations[1][0]
        longitude = sorted_informations[1][1]

        # Wiki
        wiki = Wiki(latitude, longitude)
        page_id = wiki.article_id_from_sorted_raw_info()
        full_extract = wiki.getting_extract_and_url_from_closest_wiki_page(
            page_id
        )

        article_extract = full_extract[0]
        url = full_extract[1]

        # error list
        liste_error = [
            "Je suis un peu dur de la feuille, peux tu reformuler ?",
            "Je ne suis pas sur de comprendre, peux tu le dire autrement ?",
            "Argh, Alzheimer quand tu nous tiens.. reformules veux tu ?"
        ]

        # Answer list
        liste_answer = [
            f"{title}? Bien sur, je te montre une carte, c'est plus parlant.",
            "Et si je te montrait la carte plutot ?",
            "Il n'y a pas de probleme mon enfant, tiens la carte."
        ]

        return {
            "title": title,
            "gps": {
                "latitude": latitude,
                "longitude": longitude
            },
            "article_extract": article_extract,
            "url_article": url,
            "error": random.choice(liste_error),
            "grandpy-answer": random.choice(liste_answer)
        }


if __name__ == "__main__":

    grandpy_instance = Grandpy("Bonjour, ou se situe la tour eiffel?")
    print(grandpy_instance.grandpy())
