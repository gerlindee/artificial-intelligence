from Chromosome import crossover
from Population import Population
from random import randint, random
from random import shuffle



class GPAlgorithm:
    def __init__(self, f, nrInd):
        self.n = 0
        self.header = []
        self.inputTest = []
        self.outputTest = []
        self.inputTrain = []
        self.outputTrain = []
        self.filename = f
        self.nrInd = nrInd
        self.population = Population(nrInd)
        self.probability_mutate = 0.5
        self.readedData = []
        self.read_data(f)

    def run(self):
        self.population.evaluateFitness(self.inputTrain, self.outputTrain, len(self.inputTrain))

        for i in range(100):
            print("Iteration: " + str(i))
            self.iteration()
            best = self.population.best(1)[0]
            print("fitness: %.3f" % best.fitness)

    def normalize_dataset(self, dataset):
        """ min-max normalization"""
        minn = [min(column) for column in zip(*dataset)]
        maxx = [max(column) for column in zip(*dataset)]
        for row in dataset:
            for i in range(len(row) - 1):
                row[i] = (row[i] - minn[i]) / (maxx[i] - minn[i])

    def read_data(self, filename):
        readed_data = []
        input = []
        output = []
        with open(filename, 'r') as f:
            self.header = f.readline().split(',')[1:-1]
            for line in f.readlines():
                readed_data.append([])
                line = line.strip().split(',')
                self.n += 1
                for i in range(len(line)):
                        readed_data[-1].append(float(line[i]))

        self.normalize_dataset(readed_data)
        self.readedData = readed_data

        for i in range(len(readed_data)):
            input.append([])
            for j in range(len(readed_data[i]) - 1):
                input[-1].append(float(readed_data[i][j]))
            output.append(float(readed_data[i][-1]))

        shuffle(input)
        shuffle(output)
        self.inputTrain = input[:int(self.n * 0.80)]
        self.outputTrain = output[:int(self.n * 0.80)]
        self.inputTest = input[int(self.n * 0.80):]
        self.outputTest = output[int(self.n * 0.80):]

        print("Training size: " + str(len(self.inputTrain)))
        print("Testing size: " + str(len(self.outputTest)))

    def iteration(self):
        pop = self.population.getIndividuals()
        i1 = randint(0, self.nrInd - 1)
        i2 = randint(0, self.nrInd - 1)
        if i1 != i2:
            newChild = crossover(self.population.getIndividuals()[i1], self.population.getIndividuals()[i2])
            pop.append(newChild)
            self.population.setIndividuals(pop)
            self.population.evaluateFitness(self.inputTrain, self.outputTrain, len(self.inputTrain))
            self.population.selection(self.nrInd)
