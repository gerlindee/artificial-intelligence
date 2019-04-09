import random

# An individual represents a pyramid configuration; cubes are stacked one on top of the other

COLORS = ['red', 'green', 'yellow', 'pink', 'purple', 'blue', 'white', 'black']


class Individual:
    def __init__(self, cubes, size):
        # size represents the n number of cubes in our configuration
        # a cube is represented as [ side_length, color ]
        # representation = permutations of cubes
        self._size = size
        self._cubes = cubes

    def get_cubes(self):
        return self._cubes

    @staticmethod
    def generateIndividual(no_cubes):
        # always generates a valid pyramid configuration, meaning that there can not be any identical cubes
        number_cubes = 0
        cube_sizes = []
        for idx in range(0, no_cubes):
            cube_sizes.append(idx + 1)
        pyramid = Individual([], no_cubes)
        while number_cubes < no_cubes:
            cube_color = random.choice(COLORS)
            cube_size = random.choice(cube_sizes)
            cube_sizes.remove(cube_size)
            cube = [cube_size, cube_color]
            if cube not in pyramid.get_cubes():
                pyramid.get_cubes().append(cube)
                number_cubes = number_cubes + 1
        return pyramid

    def fitness(self):
        # computes the height of the pyramid until it find a bigger cube over a smaller cube or two cubes of the same
        # color on top of each other
        height = 0
        current_cube = 0
        while current_cube < (self._size - 1):
            height = height + self._cubes[current_cube][0]
            cube_on_top = current_cube + 1
            if self._cubes[current_cube][0] < self._cubes[cube_on_top][0]:  # cube size check
                return height
            if self._cubes[current_cube][1] == self._cubes[cube_on_top][1]:  # cube color check
                return height
            current_cube = current_cube + 1
        height = height + self._cubes[current_cube][0]
        return height

    def mutate(self, probability):
        # chosen mutation method: swap mutation
        # perform a mutation on an individual, with a given probability
        # mutation = we switch two random cubes in our pyramid
        if probability > random.random():
            position_1 = random.randint(0, self._size - 1)
            position_2 = position_1
            while position_1 == position_2:  # makes sure it doesn't just swap itself
                position_2 = random.randint(0, self._size - 1)
            aux_cube = self._cubes[position_1]
            self._cubes[position_1] = self._cubes[position_2]
            self._cubes[position_2] = aux_cube
            return self
        return False

    def crossover(self, other_parent):
        # this is the version with one offspring
        # order crossover
        offspring = Individual([], self._size)
        for _ in range(0, self._size):
            offspring.get_cubes().append(0)
        start_parent_1 = random.randint(0, self._size - 1)
        end_parent_1 = random.randint(start_parent_1, self._size - 1)
        while start_parent_1 == end_parent_1:
            end_parent_1 = random.randint(start_parent_1, self._size - 1)
        idx = start_parent_1
        while idx <= end_parent_1:
            offspring.get_cubes()[idx] = self.get_cubes()[idx]
            idx = idx + 1
        offspring_idx = idx
        while idx != start_parent_1:
            if idx == self._size:
                idx = 0
                offspring_idx = 0
            if other_parent.get_cubes()[idx] not in offspring.get_cubes():
                offspring.get_cubes()[offspring_idx] = other_parent.get_cubes()[idx]
                offspring_idx = offspring_idx + 1
            idx = idx + 1
        return offspring

    def crossover_2(self, other_parent):
        # this is the version with two offsprings
        offspring_1 = self.crossover(other_parent)
        offspring_2 = self.crossover(other_parent)
        return offspring_1, offspring_2

    def __str__(self):
        result = ""
        for current_cube in reversed(self._cubes):
            result = result + "( " + str(current_cube[0]) + ", " + current_cube[1] + " )" + "\n"
        return result
