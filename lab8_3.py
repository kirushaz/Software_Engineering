class sity:
    def __init__(self, name,population,new):
        self.name = name
        self.population = population
        self.new = new
    def new(self):
        print(f'new {self.new}')

class sityy(sity):
    def __init__(self, name, population, new):
        super().__init__(name, population, new)

    def aaa(self):
        print('demidov')

sity = sityy('ekb', 200000000, 456)

print(sity.name, sity.population, sity.new)
sity.aaa()



