import random
from Population import Population


class Algorithm:
    def __init__(self, population_size, individual_size, iterations):
        self._population = Population.generatePopulation(population_size, individual_size)
        parameters = self.readParameters()
        self._mutationProb = parameters[0]
        self._iterations = iterations
        self.writePopulation()

    def getPopulation(self):
        return self._population

    def writePopulation(self):
        f = open("data/population.txt", "w")
        for item in self._population.getIndividuals():
            f.write(str(item))
            f.write("\n")
        f.close()

    @staticmethod
    def readParameters():
        f = open("data/param.in", "r")
        parameters = []
        for line in f:
            line = line.strip()
            parameters.append(float(line))
        f.close()
        return parameters

    def iteration(self):
        current_population = self._population.evaluate()
        index1 = random.randint(0, len(current_population) - 2)
        index2 = index1
        while index2 <= index1:
            index2 = random.randint(0, len(current_population) - 1)
        parent1 = current_population[index1]
        parent2 = current_population[index2]
        offspring = parent1.crossover(parent2)
        offspring = offspring.mutate(self._mutationProb)
        if offspring:
            self._population.add_individual(offspring)
        return self._population.selection()

    def run(self):
        current_runs = self._iterations
        while current_runs and len(self._population.getIndividuals()) > 1:
            self._population = self.iteration()
            current_runs = current_runs - 1
        return self._population.evaluate()[0]
