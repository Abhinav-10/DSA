

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@emamail.com'

    @property
    def email(self):
        return self.first + '.' + self.last + '@emamail.com'


    def full_name(self):
        return "{} {}".format(self.first, self.last)


first=input("enter your first name")
last = input("enter your last name")
e1 = Employee(first=first, last=last)
print(e1.full_name(), e1.email, e1.last)

e1.first = "Shubham"

print(print(e1.full_name(), e1.email, e1.last))

# we need to change email as well if firstn and last name got changed here property decorater comes into picture

# To acces the function as an attribute we can use property decorator 