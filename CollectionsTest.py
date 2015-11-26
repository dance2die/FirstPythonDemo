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
    pp(divider + " END List Test " + divider)


testLists()
testSets()


