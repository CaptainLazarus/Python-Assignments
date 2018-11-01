class student:
    def __init__(self , name , age , city , height):
        self.name = name
        self.age = age
        self.city = city
        self.height = height

    def __hash__(self):
        return hash((self.name, self.age , self.city , self.height))

    def __eq__(self, other):
        return (self.name, self.location) == (other.name, other.location)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

a = student('Aditya' , '18' , 'Hyderabad' , '176')#list(input().split(' ').strip())
print('Name: ' + a.name + '\nAge: ' + a.age + '\nCity: ' + a.city +  '\nHeight: ' + a.height)