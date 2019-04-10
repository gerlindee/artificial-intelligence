from Algorithm import Algorithm
from statistics import mean, stdev


class Application:
    def main(self):
        population_size = int(input("population size: "))
        individual_size = int(input("individual size: "))
        iterations = int(input("number of iterations per run: "))
        runs = int(input("number of runs: "))
        alg = Algorithm(population_size, individual_size, iterations)
        results = []
        best = None
        for i in range(0, runs):
            best = alg.run()
            stability = best.fitness()
            results.append(stability)
        mean_overall = mean(results)
        std_overall = stdev(results)
        print("The best individual after ", runs, "runs of ", iterations, "iterations is: ")
        print(best)
        print("The average for the best solutions is: ", mean_overall)
        print("The standard deviation for the best solutions is: ", format(std_overall,  '.10f'))


a = Application()
a.main()
