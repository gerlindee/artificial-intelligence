import random
from Problem import Problem


class Algorithm:
    def __init__(self, problem):
        self._problem = problem
        self._population = self._problem.loadData()
        parameters = self.readParameters()
        self._mutationProb = parameters[0]
        self._crossoverProb = parameters[1]

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
        index1 = random.randint(0, len(current_population) - 1)
        index2 = random.randint(0, len(current_population) - 1)
        if index1 != index2:
            parent1 = current_population[index1]
            parent2 = current_population[index2]
            offspring = parent1.crossover(parent2, self._crossoverProb)
            offspring = offspring.mutate(self._mutationProb)
            if offspring:
                self._population.add_individual(offspring)
        return self._population.selection()

    def run(self):
        runs = 30
        while runs:
            self.iteration()
            runs = runs - 1
        return self._population.evaluate()[0]



