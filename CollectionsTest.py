import collections
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


def testDictionaries():
    names = {"Me": "Min",
             "Brother": "Bum",
             "Sister": "Hui"}
    pp('names["Me"]={}'.format(names["Me"]))
    urls = dict(microsoft="microsoft.com", google="google.com")
    pp("urls={}".format(urls))
    for key,value in names.items():
        pp("key={}; value={}".format(key, value))


def testDeque():
    myDeque = collections.deque("abcdef", 10)
    pp("Starting state:")
    for item in myDeque:
        print(item, end=" ")

    pp("\r\n\r\nAppending and extending right")
    myDeque.append("h")
    myDeque.append("ij")
    for item in myDeque:
        print(item, end=" ")

    print("\r\nmyDeque contains {0} items.".format(len(myDeque)))
    print("\r\nPopping right")
    print("Popping {0}".format(myDeque.pop()))
    for Item in myDeque:
       print(Item, end=" ")
    print("\r\n\r\nAppending and extending left")
    myDeque.appendleft("xyz")
    myDeque.extendleft("abc")
    for Item in myDeque:
       print(Item, end=" ")
    print("\r\nmyDeque contains {0} items."
          .format(len(myDeque)))
    print("\r\nPopping left")
    print("Popping {0}".format(myDeque.popleft()))
    for Item in myDeque:
       print(Item, end=" ")
    print("\r\n\r\nRemoving")
    myDeque.remove("a")
    for Item in myDeque:
       print(Item, end=" ")

def main():
    # testSets()
    # testLists()
    # testDictionaries()
    testDeque()


if __name__ == '__main__':
    pp("name={}".format(__name__))
    main()







