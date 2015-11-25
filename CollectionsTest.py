from pprint import pprint as pp

def testSets():
    developerSet = {"Sung", "Brendan", "Vasu"}
    helpDeskSet = {"Calvin", "Anthony"}
    itSet = developerSet.union(helpDeskSet)

    divider = "=" * 30
    pp(divider + " BEGIN Set Test " + divider)
    pp("developerSet={}".format(developerSet))
    pp("helpDeskSet={}".format(helpDeskSet))
    pp("itSet={}".format(itSet))
    pp(divider + " END Set Test " + divider)

testSets()


