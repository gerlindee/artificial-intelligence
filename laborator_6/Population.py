from Chromosome import Chromosome


class Population:
    def __init__(self, nrIndividuals):
        self.nrIndividuals = nrIndividuals
        self.individuals = [Chromosome() for i in range(nrIndividuals)]

    def evaluateFitness(self, input, output, noExamples):
        self.individuals = sorted(self.individuals, key=lambda x: x.computeFitness(input, output, noExamples))

    def selection(self, nrInd):
        if nrInd < self.nrIndividuals:
            self.nrIndividuals = nrInd
            self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
            self.individuals = self.individuals[:nrInd]

    def best(self, maxInd):
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
        return self.individuals[:maxInd]
