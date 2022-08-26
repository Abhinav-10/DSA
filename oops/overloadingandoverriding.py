# Method Overloading python does not support method

# method overloading

class Student:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self, a, b):
        s = a+b
        return s

# s1 = Student(5, 6)
# print(s1.sum(5, 6))


###### Method Overriding

class A:

    def show(self):
        print("in A show")


class B(A):
    def show(self):
        print("in B show")
# a1 = A()
# a1.show()
b1 = B()
b1.show()