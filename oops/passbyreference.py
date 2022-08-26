class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == 'male':
        print(f"Hello {customer.name} sir")
    else:
        print(f"Hello {customer.name} mam")

cust1 = Customer("Abhinav", 'male')
cust2 = Customer("Akansha", 'female')
greet(cust1)
greet(cust2)