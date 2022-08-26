class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d
    
    def __str__(self):
        print(self)

    def __add__(self, other):
        temp = self.num + other.num