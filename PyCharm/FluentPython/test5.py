class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


emp1 = Employee("Rashid",100)

emp1.displayEmployee()

print emp1.empCount

emp2 = Employee("Arif",100)

emp2.displayEmployee()

print emp2.empCount

print Employee.empCount

print emp2.__class__

class Foo(object):
    @staticmethod
    def bar(x):
        print "I m bar, x is", x
    @classmethod
    def spam(cls):
        print cls

Foo.bar(5)
Foo.spam()