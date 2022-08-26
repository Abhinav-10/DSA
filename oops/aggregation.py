class Customer:

    def __init__(self, name, age, address):
        self.name = name
        self.address = address
        self.age = age


class Address:
    
    def __init__(self,city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def change_address(self, city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

add = Address('Gurgaon', 'Haryana', '122001')
cust1 = Customer('Abhinav', '23', add)

print(cust1.address.pincode)
