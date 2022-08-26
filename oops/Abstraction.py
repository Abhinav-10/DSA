# Abstraction

"""
Abstract Methods are methods which only needs declaration not defenition
and class which have abstract method called abstract class
Python does not support abstraction
but a module abc which is abstract base class

we can't instantiate an abstract class

"""
from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("I'm running")

l1= Laptop()
l1.process()


class Whiteboard:

    def write(self):
        print("its running")

class Programmer:
    def work(self, com):
        print("Solving bugs")
        print(com.process())
p1 = Programmer()
p1.work(l1)