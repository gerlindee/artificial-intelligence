import random
from copy import deepcopy
from Individ import Individual


class Population:
    def __init__(self, individuals, size):
        # size = the dimension of the population
        self._size = size
        self._individuals = individuals

    def getIndividuals(self):
        return self._individuals

    @staticmethod
    def generatePopulation(population_size, individual_size):
        # takes a generated permutation representing a pyramid configuration and "develops" a population from it
        # aka just moves cubes around randomly until the population gets the desired number of individuals
        no_individuals = 0
        individual = Individual.generateIndividual(individual_size)
        population = Population([individual], population_size)
        while no_individuals < (population_size - 1):
            # we now change the initial configuration in order to get new individuals
            new_individual = deepcopy(individual)
            position_1 = random.randint(0, individual_size - 1)
            position_2 = position_1
            while position_1 == position_2:
                position_2 = random.randint(0, individual_size - 1)
            aux_cube = new_individual.get_cubes()[position_1]
            new_individual.get_cubes()[position_1] = new_individual.get_cubes()[position_2]
            new_individual.get_cubes()[position_2] = aux_cube
            population.getIndividuals().append(new_individual)
            no_individuals = no_individuals + 1
        return population

    def evaluate(self):
        # sort the individuals based on the fitness function
        return sorted(self._individuals, key=lambda x: x.fitness(), reverse=True)

    def selection(self):
        # survival selection, the least qualitative individual is eliminated
        self._individuals = self.evaluate()[:-1]
        return self

    def add_individual(self, candidate):
        self._individuals.append(candidate)
