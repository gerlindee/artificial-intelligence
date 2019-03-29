

class Population:
    def __init__(self, individuals):
        self._noOfIndividuals = len(individuals)
        self._individuals = individuals

    def getIndividuals(self):
        return self._individuals

    def evaluate(self):
        # sort the individuals based on the fitness function
        return sorted(self._individuals, key=lambda x: x.fitness())

    def selection(self):
        # survival selection, the least qualitative individual is eliminated
        return self.evaluate()[:-1]

    def add_individual(self, candidate):
        self._individuals.append(candidate)


