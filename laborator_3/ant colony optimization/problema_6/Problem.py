from random import random, choice

COLORS = ['red', 'green', 'yellow', 'pink', 'purple', 'blue', 'white', 'black']


class Problem:
    def __init__(self, totalNumCubes):
        self._cubes = []
        self._numCubes = totalNumCubes
        self._cubes = self.generateIndividual(totalNumCubes)

    def getCubes(self):
        return self._cubes

    def getSize(self):
        return self._numCubes

    @staticmethod
    def generateIndividual(no_cubes):
        # always generates a valid pyramid configuration, meaning that there can not be any identical cubes
        number_cubes = 0
        cube_sizes = []
        for idx in range(0, no_cubes):
            cube_sizes.append(idx + 1)
        pyramid = []
        while number_cubes < no_cubes:
            cube_color = choice(COLORS)
            cube_size = choice(cube_sizes)
            cube_sizes.remove(cube_size)
            cube = [cube_size, cube_color]
            if cube not in pyramid:
                pyramid.append(cube)
                number_cubes = number_cubes + 1
        return pyramid

    def __str__(self):
        result = ""
        for current_cube in reversed(self._cubes):
            result = result + "( " + str(current_cube[0]) + ", " + current_cube[1] + " )" + "\n"
        return result
