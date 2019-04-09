from Individ import Individual
from Population import Population


class Problem:
    def __init__(self, fileName):
        self._fileName = fileName

    def loadData(self):
        population = Population([], 4)
        f = open(self._fileName, "r")
        for line in f:
            current_pyramid_line = []
            for cube in line.split(","):
                cube = cube.strip()
                items = cube.split(" ")
                current_pyramid_line.append([int(items[0]), items[1]])
            pyramid = Individual(current_pyramid_line, 4)
            population.add_individual(pyramid)
        f.close()
        return population
