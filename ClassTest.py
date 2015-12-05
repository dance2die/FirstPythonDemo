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


class Employee(Person):
    def __init__(self, name, employeeId):
        super().__init__(name)
        self.employeeId = employeeId

    @property
    def employeeId(self):
        return self._employeeId

    @employeeId.setter
    def employeeId(self, value):
        self._employeeId = value



def personPrinter(person):
    ''' To test Duck Typing '''
    pp("Name: {}".format(person.name))

def employeePrinter(employee):
    ''' To test Duck Typing '''
    pp("Name: {}; EmployeeID: {}".format(employee.name, employee.employeeId))


def main():
    p1 = Person("Mike")
    p1.printPerson(personPrinter)
    p1.name = "John"
    p1.printPerson(personPrinter)
    p1._name = "Chris"
    p1.printPerson(personPrinter)
    e1 = Employee("Employee1", 1)
    e2 = Employee("Employee2", 2)
    employeePrinter(e1)
    employeePrinter(e2)

if __name__ == '__main__':
    main()




