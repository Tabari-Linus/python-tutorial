class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+"@company.com"

        Employee.num_of_emps +=1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee("Linus", "Nex", 10000)
emp_2 = Employee('Mr', "Lii", 8000)

emp_1.fullname()
print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(Employee.num_of_emps)

