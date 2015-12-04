from pprint import pprint as pp

class Person:
    def __init__(self, name):
        self.setName(name)

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def printPerson(self, printer):
        printer(self)


def personPrinter(person):
    ''' To test Duck Typing '''
    pp("Name: {}".format(person.getName()))


def main():
    p1 = Person("Mike")
    p1.printPerson(personPrinter)

if __name__ == '__main__':
    main()




