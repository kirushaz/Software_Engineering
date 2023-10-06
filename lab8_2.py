class sity:
    def __init__(self, name,population,new):
        self.name = name
        self.population = population
        self.new = new
    def new(self):
        print(f'new {self.new}')

sity = sity('ekb', 200000000, 456)
print(sity.name , sity.population,  sity.new)


