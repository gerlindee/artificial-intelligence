import random

# An individual represents a pyramid configuration; cubes are stacked one on top of the other

CONST_COLORS = ['red', 'green', 'yellow', 'pink', 'purple', 'blue']


class Individual:
    def __init__(self, cubes):
        # size denotes the number of cubes in our configuration
        # a cube is represented as [ side_length, color ]
        self._size = len(cubes)
        self._cubes = cubes

    @staticmethod
    def generate_individual(size):
        individual = Individual([])
        for idx in range(0, size):
            length_cube = random.randint(1)
            color_cube = random.choice(CONST_COLORS)
            cube = [length_cube, color_cube]
            individual.get_cubes().append(cube)
        return individual

    def get_cubes(self):
        return self._cubes

    def fitness(self):
        # represents the value of the stability coefficient
        stability_coefficient = 0
        height = 0
        for idx in range(0, self._size):
            height = height + self._cubes[idx][0]
            if idx < (self._size - 1):
                if self._cubes[idx][0] < self._cubes[idx+1][0]:  # if a smaller cube has a bigger cube on top of it
                    stability_coefficient = stability_coefficient + 1
                if self._cubes[idx][1] == self._cubes[idx+1][1]:  # if there are two consecutive cubes of the same color
                    stability_coefficient = stability_coefficient + 1
        return stability_coefficient

    def mutate(self, probability):
        # perform a mutation on an individual, with a given probability
        # mutation = we switch two random cubes in our pyramid
        if probability > random.random():
            position_1 = random.randint(0, self._size - 1)
            position_2 = position_1
            while position_1 == position_2:
                position_2 = random.randint(0, self._size - 1)
            aux_cube = self._cubes[position_1]
            self._cubes[position_1] = self._cubes[position_2]
            self._cubes[position_2] = aux_cube
            return self
        return False

    def crossover(self, other_parent, probability):
        # merge two pyramid configurations into a child pyramid configuration, with a given probability
        # could be optimized to be fancier tbh
        if probability > random.random():
            offspring_pyramid = []
            cubes_parent_1 = random.randint(1, self._size - 1)
            idx = 0
            while idx < cubes_parent_1:
                offspring_pyramid.append(self._cubes[idx])
                idx = idx + 1
            while idx < self._size:
                offspring_pyramid.append(other_parent.get_cubes()[idx])
                idx = idx + 1
            return Individual(offspring_pyramid)
        return False

    def __str__(self):
        result = ""
        for current_cube in reversed(self._cubes):
            result = result + "( " + str(current_cube[0]) + "," + current_cube[1] + " )" + "\n"
        return result



