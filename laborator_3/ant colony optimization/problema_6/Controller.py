from Ant import Ant


class Controller:
    def __init__(self, problem):
        self._problem = problem
        self._numEpochs = 0
        self._numAnts = 0
        self._alpha = 0.0
        self._beta = 0.0
        self._rho = 0.0 # the evaporation rate
        self._q0 = 0.0
        self.loadParameters()

    def getEpoch(self):
        return self._numEpochs

    def loadParameters(self):
        with open("parameters.in") as file:
            line = file.readline().strip()
            self._numEpochs = int(line.replace("number of epochs: ", ""))

            line = file.readline().strip()
            self._numAnts = int(line.replace("number of ants: ", ""))

            line = file.readline().strip()
            self._alpha = float(line.replace("alpha: ", ""))

            line = file.readline().strip()
            self._beta = float(line.replace("beta: ", ""))

            line = file.readline().strip()
            self._rho = float(line.replace("rho: ", ""))

            line = file.readline().strip()
            self._q0 = float(line.replace("q0: ", ""))

    def epoch(self, pheromoneMatrix):
        population = []
        for i in range(self._numAnts):
            ant = Ant(self._problem)
            population.append(ant)

        for i in range(self._problem.getSize()):
            for ant in population:
                ant.addMove(pheromoneMatrix, self._alpha, self._beta, self._q0)

        # we update the trace with the pheromones left by all the ants
        t = [1.0/population[i].fitness() for i in range(len(population))]

        # pheromone decrease with the amount in the evaporation rate
        for i in range(self._problem.getSize()):
            for j in range(self._problem.getSize()):
                pheromoneMatrix[i][j] = (1 - self._rho) * pheromoneMatrix[i][j]

        for i in range(len(population)):
            for j in range(len(population[i].getPath()) - 1):
                x = population[i].getPath()[j]
                y = population[i].getPath()[j + 1]
                pheromoneMatrix[x][y] = pheromoneMatrix[x][y] + t[i]

        # get the path for the best ant
        fitness = [[population[i].fitness(), i] for i in range(len(population))]
        fitness = max(fitness)
        return population[fitness[1]]