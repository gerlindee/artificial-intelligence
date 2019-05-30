from random import random


class Neuron:
    def __init__(self, noOfInputs, activationFunction):
        self.noOfInputs = noOfInputs
        self.activationFunction = activationFunction
        self.weights = [random() for i in range(self.noOfInputs)]
        self.output = 0

    def setWeights(self, newWeights):
        self.weights = newWeights

    def fireNeuron(self, inputs):
        # neuron processing -> computing the weighted sum of inputs
        # zip = returns an iterator of tuples
        # example: [1, 2, 3] and ['one','two','three']
        # result: [1, 'one'], [2, 'two'], [3, 'three']
        u = sum([x * y for x, y in zip(inputs, self.weights)])
        # processing the information using an activation function
        self.output = self.activationFunction(u)
        return self.output

    def __str__(self):
        return str(self.weights)

