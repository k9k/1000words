# coding= utf-8
__author__ = 'kamil'

import unittest
words = __import__('1000words')     # problematic file which starts with digit


class KnownValues(unittest.TestCase):
    knownValues= ( ("he", "on"),
                   ("she", "ona"),
                   ("ship", "statek"),
                   ("ball", u"piłka"),
                   ("change", "zmiana"),
                   ("job", "praca"),
                   ("name", "nazwa"),
                   ("paper", "papier"),
                   ("uncle", "wujek"),
                   ("taxi", u"taksówka"),
                   ("boy", u"chłopak"),
                   ("old", "stary"),
                   ("or", "albo"),
                   ("be", u"być"),
                   ("two", "dwa"),
                   ("three", "trzy"),
                   ("eight", "osiem"),
                   ("ten", u"dziesięć"),
                   ("look", u"patrzeć"),
                   ("her", "jej"),
                   ("sun", u"słońce"),
                   ("keep", u"trzymać"),
                   ("both", "razem"),
                   ("music", "muzyka"),
                   ("cry", u"płakać"),
                   ("fish", "ryba"),
                   ("machine", "maszyna"),
                   ("main", u"główny"),
                   ("young", u"młody"),
                   ("red", "czerwony"),
                   ("black", "czarny"),
                   ("half", "połowa"),
                   ("island", "wyspa"),
                   ("problem", "problem"),
                   ("hot", u"gorący"),
                   ("forest", "las"),
                   ("summer", "lato"),
                   ("key", "klucz"),
                   ("deal", "umowa"),
                   ("success", "sukces"))

    """def testGetDef(self):
        #testGet should return correct definition (at least one)
        for eng, pl in self.knownValues:
            #print(eng, pl)
            result = words.get_def(eng)
            splitted = []
            for i in result:
                for j in i.split():
                    splitted.append(j)
            self.assertIn(pl, splitted)"""


def testGetDef():
    for eng, pl in KnownValues.knownValues:
        test_name = 'test_%s' % (eng)
        print(test_name)
        result = words.get_def(eng)
        splitted = []
        for i in result:
            for j in i.split():
                splitted.append(j)
        test = generator(pl, splitted)
        setattr(KnownValues, test_name, test)


def generator(correct, ret):
    def test(self):
        self.assertIn(correct, ret)
    return test




if __name__ == "__main__":
    testGetDef()
    #unittest.main()
