import random

def random_word():
    return WORD_LIST[random.randrange(len(WORD_LIST))].lower()

def random_word2(category):
    # print(CATEGORIES.get(category))
    return CATEGORIES.get(category)[random.randrange(len(CATEGORIES.get(category)))].lower()

def get_categories():
    return list(CATEGORIES.keys())

WORD_LIST = ("Football","Basketball","Quaterback","Soccer","Intersteller","Wicked","Moana","Avengers","Algorithm","Cybersecurity","Encryption","software","JavaScript")


sport_list =[
    "Football",
    "Basketball",
    "Quaterback",
    "Soccer"
]

movie_list=[
    "Intersteller",
    "Wicked",
    "Moana",
    "Avengers"
]

coding_list=[
    "Algorithm",
    "Cybersecurity",
    "Encryption",
    "Software",
    "JavaScript"
]

CATEGORIES = {"Sports": sport_list, "Movies": movie_list, "Coding": coding_list}
