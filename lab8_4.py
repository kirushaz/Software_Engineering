class sity:
    def __init__(self, name,population,new):
        self.name = name
        self.population = population
        self.new = new
    def new(self):
        print(f'new {self.new}')

class sityy(sity):
    def __init__(self, name, population, new,temp):
        super().__init__(name, population, new)
        super().__init__(name, population, new)
        self.__temp = temp

    def aaa(self):
            print('demidov')
    def gradus(self):
            print(f'Температура {self.__temp}')



sity = sityy('ekb', 200000000, 45, 20)
sity.gradus()

