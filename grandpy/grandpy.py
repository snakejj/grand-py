

def grandpy(raw_question):
    # Parser
    parser = Parser(raw_question)
    clean_question = parser.clean_input()

    # here
    here = Here(clean_question)
    sorted_informations = here.getting_sorted_informations()
    
    name = sorted_informations[0]
    latitude = sorted_informations[1][0]
    longitude = sorted_informations[1][1]


    # wiki
    wiki = Wiki(latitude, longitude)


    # liste de phrases d'erreur
    liste_erreur = [
        "Je suis un peu dur de la feuille, peux tu reformuler ?",
        "Je ne suis pas sur de bien comprendre, peux tu le dire autrement ?",
        "Humm., même apres reflexion je ne comprends pas, reformules veux tu ?"
    ]

    # liste de réponses
    liste_réponses = [
        

    ]

    return {
        "title": #
        "gps": {
            "latitude": #
            "longitude": #
        }
        "article_extract": #
        "url_article": #
        "error" : # A prendre au hasard dans une liste de phrases d'erreur
        "grandpy-response" # # A prendre au hasard dans une liste de reponses
    }