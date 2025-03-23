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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Linus", "Nex", 10000)
emp_2 = Employee('Mr', "Lii", 8000)

emp_1.fullname()
print(emp_1.fullname())
print(Employee.fullname(emp_1))

emp_str_1 = 'Jak-jude-7000'
str_emp = Employee.from_string(emp_str_1)
print(str_emp.email, str_emp.pay)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

print(Employee.num_of_emps)

