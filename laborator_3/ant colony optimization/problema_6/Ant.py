from random import randint, random, choice


class Ant:
    def __init__(self, problem):
        self._problem = problem
        self._path = [randint(0, self._problem.getSize() - 1)]

    def getPath(self):
        return self._path

    def fitness(self):
        # the fitness is the height of the pyramid
        return len(self._path)

    def nextMoves(self):
        # represents where the ant could move to next
        # in this case, a future position represents a cube that is smaller than the current top one and a different
            # colour, that could be placed as the new top
        moves = []
        for currentCube in self._problem.getCubes():
            if currentCube[0] < self._path[-1] and self._problem.getCubes()[self._path[-1]][1] != currentCube[1]:
                moves.append(currentCube[0])
        return moves.copy()

    def evaluate(self, nextMove):
        # Adds the fitness of the current element to the path, if a possible solution has not been found
        ant = Ant(self._problem)
        ant._path = self._path.copy()

        if len(ant.getPath()) == self._problem.getSize():
            return
        ant._path.append(nextMove)
        return self.fitness()

    def addMove(self, pheromoneTraceMatrix, alpha, beta, q0):
        # we try to add a new move to the ant's path, if possible
        p = [0 for i in range(self._problem.getSize())]
        nextMoves = self.nextMoves()

        # if there are not valid positions we stop
        if not nextMoves:
            return False

        for move in nextMoves:
            p[move] = self.evaluate(move)

        p = [(p[i] ** beta) * (pheromoneTraceMatrix[self._path[-1]][i] ** alpha) for i in range(len(p))]
        probability1 = random()
        # probability based selection of the next move
        if probability1 < q0:
            # we determine the best move out of all the possible ones
            r = [[i, p[i]] for i in range(len(p))]
            r = max(r, key=lambda a: a[1])
            self._path.append(r[0])
        else:
            # roulette selection
            s = sum(p)
            if s == 0:
                return choice(nextMoves)
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0: i + 1]) for i in range(len(p))]
            probability2 = random()
            i = 0
            while probability2 > p[i]:
                i = i + 1
            self._path.append(i)
        return True

    def __str__(self):
        return str(self.getPath())