from Problem import Problem
from Controller import Controller
from random import randint
import matplotlib.pyplot as plt
import statistics


def main():
    problem = Problem(10)

    pheromoneMatrix = [[1 for i in range(problem.getSize())] for j in range(problem.getSize())]

    controller = Controller(problem)

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
        print(cube)
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