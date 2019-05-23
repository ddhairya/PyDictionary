__author__ = 'dhairya'

import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(file)


def dictword(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    else:
        matching = get_close_matches(w, data.keys(), 3, 0.8)[0]
        misspell = input("Press y for yes or n for no, Did you mean %s? " % matching)
        if misspell == 'y':
            return data[matching]
        else:
            return "This word doesn't exists"


print("Welcome to python dictionary, press x to exit")
while True:
    word = input("Enter the word to look for the meaning: ")
    if word == 'x':
        break
    else:
        result = dictword(word)
        for r in result:
            print(r)
