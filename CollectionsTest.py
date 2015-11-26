from pprint import pprint as pp

divider = "=" * 30

def testSets():
    developerSet = {"Sung", "Brendan", "Vasu"}
    helpDeskSet = {"Calvin", "Anthony"}
    itSet = developerSet.union(helpDeskSet)

    pp(divider + " BEGIN Set Test " + divider)
    pp("developerSet={}".format(developerSet))
    pp("helpDeskSet={}".format(helpDeskSet))
    pp("itSet={}".format(itSet))
    pp(divider + " END Set Test " + divider)


def testLists():
    pp(divider + " BEGIN List Test " + divider)
    l = "this is a string".split()

    pp('l.index("string") = {}'.format(l.index("string")))
    del l[l.index("string")]
    pp("l={}".format(l))

    # [::-1] reverses the list without modifying the current list.
    # http://stackoverflow.com/a/5846048/4035
    pp("l[::-1]={}".format(l[::-1]))

    # sort and return a copy of a list instead of modifying in place.
    # http://stackoverflow.com/a/2587419/4035
    pp("sorted(l, key=len)={}".format(sorted(l, key=len)))

    pp(divider + " END List Test " + divider)


def testDictitionaries():
    names = {"Me": "Min",
             "Brother": "Bum",
             "Sister": "Hui"}
    pp('names["Me"]={}'.format(names["Me"]))


testSets()
testLists()
testDictitionaries()









