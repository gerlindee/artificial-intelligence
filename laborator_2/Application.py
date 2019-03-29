from Problem import Problem
from Algorithm import Algorithm
from statistics import mean, stdev


class Application:
    def main(self):
        prb = Problem("data/data01.in")
        prb.loadData()
        alg = Algorithm(prb)
        results = []
        for i in range(0, 100):
            best = alg.run()
            stability = best.fitness()
            results.append(stability)
        mean_overall = mean(results)
        std_overall = stdev(results)
        print("The average for the best solutions is: ", mean_overall)
        print("The standard deviation for the best solutions is: ", std_overall)


a = Application()
a.main()
