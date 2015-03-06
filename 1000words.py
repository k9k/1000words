# coding= utf-8
__author__ = 'kamil'

from bs4 import BeautifulSoup
import requests
import random


def parse_words():
    """returns list of 1000 basic words in English"""
    url = "http://pl.wiktionary.org/wiki/Indeks:Angielski_-_1000_podstawowych_s%C5%82%C3%B3w"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    dd = soup.find_all("dd")
    words = []

    for i in dd:
        for j in i.find_all("a"):
            words.append(j.get("title"))
    return words


def get_def(word):
    """returns list of translations"""
    transl = []
    url = "http://pl.wiktionary.org/wiki/" + word + "#en"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    dfn = soup.find_all("dfn")

    for i in dfn:
        j = i.find_all("a")
        translation = ""
        for k in j:
            if k and k.get("title"):
                if translation:
                    translation += " " + k.get("title")
                else:
                    translation += k.get("title")
                if "(strona nie istnieje)" in translation:
                    translation = translation.replace(" (strona nie istnieje)", "")
                elif "Aneks" in translation:
                    translation = ""
                elif u"Wikisłownik" in translation:
                    translation = ""
                elif "Kategoria:" in translation:
                    translation = ""
                elif "w:" in translation:
                    translation = ""
            else:
                break
        if translation:
            transl.append(translation)

    if transl:
        return transl
    else:
        return None


def check_score(score):
    """checks actual score and prints comunicates"""
    if score == 3:
        print("\nDo 3 razy sztuka?\n")
    elif score == 10:
        print("\n10 z rzędu!\n")
    elif score == 20:
        print("\n\tUCZ MNIE, MISTRZU!\n")


def main():
    WORDS = parse_words()
    decision = "t"
    definitions = []
    score = 0

    while decision is "t":
        while not definitions:
            word = random.choice(WORDS)
            definitions = get_def(word)
        print("\n\t", word, "\n")
        answer = input("Wprowadź tłumaczenie: ")
        for i in definitions:
            if answer in i and len(answer) > 1:
                result = "Brawo!"
                score += 1
                check_score(score)
                break
            else:
                result = "Niestety, nie udało się zgadnąć."
                score = 0
        if result is "Niestety, nie udało się zgadnąć.":
            score = 0
        print(result)
        definitions = []
        decision = input("Losować kolejne słowo? t/n: ")

if __name__ == "__main__":
    main()

