class team:
    def __init__(self , name , country , year):
        self.name = name
        self.country = country
        self.year = year

    def __hash__(self):
        return hash((self.name, self.country , self.year))

    def __eq__(self, other):
        return (self.name, self.year) == (other.name, other.year)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

a = team('Arsenal' , 'Spain' , '1884')#list(input().split(' ').strip())
print('Name: ' + a.name + '\nCountry: ' + a.country + '\nYear: ' + a.year)

