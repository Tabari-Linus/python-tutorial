

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+"@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)



emp_1 = Employee("Linus", "Nex", 10000)
emp_2 = Employee('Mr', "Lii", 8000)

emp_1.fullname()
print(emp_1.fullname())
print(Employee.fullname(emp_1))

