from pprint import pprint as pp

developerSet = {"Sung", "Brendan", "Vasu"}
helpDeskSet = {"Calvin", "Anthony"}
itSet = developerSet.union(helpDeskSet)


pp("developerSet={}".format(developerSet))
pp("helpDeskSet={}".format(helpDeskSet))
pp("itSet={}".format(itSet))
