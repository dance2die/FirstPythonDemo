from pprint import pprint as pp

class Person:
    def __init__(self, name):
        self._name = name

    def printPerson(self, printer):
        printer(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


def personPrinter(person):
    ''' To test Duck Typing '''
    pp("Name: {}".format(person.name))


def main():
    p1 = Person("Mike")
    p1.printPerson(personPrinter)
    p1.name = "John"
    p1.printPerson(personPrinter)
    p1._name = "Chris"
    p1.printPerson(personPrinter)

if __name__ == '__main__':
    main()




