from shelve import Shelf


class Employee:

    rasie_amt = 500000

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@emamail.com'
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = float(self.pay+ self.rasie_amt)


# first=input("enter your first name")
# last = input("enter your last name")
# e1 = Employee(first=first, last=last, pay=100000000)
# print(e1.full_name(), e1.email, e1.last, e1.pay)
# e1.apply_raise()
# print(e1.full_name(), e1.email, e1.last, e1.pay)


## Inheritance 

class Developer(Employee):
    rasie_amt=1000000
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



# dev1 = Developer('Rahul', 'Tripathi', 99999999999, "Python")
# dev2 = Developer('Rishabh', 'Tripathi', 99999999999, "Java")

# print(dev1.full_name(), dev1.email, dev1.prog_lang)
# print(dev2.full_name(), dev2.email, dev2.prog_lang)
# print(help(Developer))
# dev1.apply_raise()
# print(dev1.pay)


class Manager(Employee):

    def __init__(self, first, last, pay, employees= None):
        super().__init__(first, last, pay)
        if employees:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    
    def get_employees(self):
        for emp in self.employees:
            print("==>", emp.full_name())

dev1 = Developer('Rahul', 'Tripathi', 99999999999, "Python")
dev2 = Developer('Rishabh', 'Tripathi', 99999999999, "Java")

mgr1 = Manager("Abhishek", "Tripathi", 9009099089, [dev1])

# print(mgr1.email)

# mgr1.get_employees()

# mgr1.add_employee(dev2)
# mgr1.get_employees()
# mgr1.remove_employee(dev1)
# mgr1.get_employees()

## is instance and is sublass

print(isinstance(mgr1, Manager))

print(issubclass(Manager, Developer))
