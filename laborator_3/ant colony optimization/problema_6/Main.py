from Problem import Problem
from Controller import Controller
from random import randint
import matplotlib.pyplot as plt
import statistics


def main():
    chosenSize = int(input("maximum number of cubes: "))
    problem = Problem(chosenSize)

    pheromoneMatrix = [[1 for i in range(problem.getSize())] for j in range(problem.getSize())]
    cubeMatrix = [[0 for i in range(problem.getSize())] for j in range(problem.getSize())]
    for cube in problem.getCubes():
        i = randint(0, problem.getSize() - 1)
        j = randint(0, problem.getSize() - 1)
        while cubeMatrix[i][j] != 0:
            i = randint(0, problem.getSize() - 1)
            j = randint(0, problem.getSize() - 1)
        cubeMatrix[i][j] = cube

    controller = Controller(problem, cubeMatrix)

    fitness = []
    bestAnt = None
    for i in range(controller.getEpoch()):
        solution = controller.epoch(pheromoneMatrix)
        if bestAnt is None:
            bestAnt = solution
        if solution.fitness() > bestAnt.fitness():
            bestAnt = solution
        fitness.append(bestAnt.fitness())

    mean = statistics.mean(fitness)
    stddev = statistics.stdev(fitness, mean)
    print("the mean of the fitness is: ", mean)
    print("the standard deviation of the fitness is: ", stddev)
    pyramid = ""
    for cube in bestAnt.getPath():
        for c in problem.getCubes():
            if c[0] == cube:
                pyramid = pyramid + str(c)
                break
    print("the highest pyramid configuration is: ", pyramid)

    plt.plot(fitness)
    plt.ylabel("Fitness variation")
    plt.xlabel("Epoch number")
    plt.show()


main()