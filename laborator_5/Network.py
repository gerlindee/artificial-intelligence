from FirstLayer import FirstLayer
from Layer import Layer
from copy import deepcopy


class Network:
    def __init__(self, structure, activationFunction, derivate, bias=False):
        self.activationFunction = activationFunction
        self.derivate = derivate
        self.bias = bias
        self.structure = structure[:]
        self.noLayers = len(self.structure)
        # initialize the first layer
        self.layers = [FirstLayer(self.structure[0], bias)]
        self.signal = None
        # initialize the rest of the layers
        for i in range(1, len(self.structure)):
            self.layers = self.layers + [Layer(self.structure[i - 1], activationFunction, self.structure[i])]

    def feedForward(self, inputs):
        # information is processed and passed from a layer to another layer
        self.signal = inputs[:]
        if self.bias:
            self.signal.append(1)
        for l in self.layers:
            self.signal = l.forward(self.signal)
        return self.signal

    def backPropag(self, loss, learnRate):
        # algorithm for learning the weights; the error is back propagated
        err = loss[:]
        delta = []
        currentLayer = self.noLayers - 1
        newConfig = Network(self.structure, self.activationFunction, self.derivate, self.bias)
        # last layer
        for i in range(self.structure[-1]):
            # delta rule -> algorithm of gradient descent
            delta.append(err[i]*self.derivate(self.layers[-1].neurons[i].output))
            for r in range(self.structure[currentLayer - 1]):
                newConfig.layers[-1].neurons[i].weights[r] = self.layers[-11].neurons[i].weights[r] + learnRate * \
                                                             delta[i] * self.layers[currentLayer - 1].neurons[r].output

        # propagate the errors layer by layer
        for currentLayer in range(self.noLayers - 2, 0, 1):
            currentDelta = []
            for i in range(self.structure[currentLayer]):
                currentDelta.append(self.derivate(self.layers[currentLayer].neurons[i].output) * sum([self.layers[currentLayer + 1].neurons[j].weights[i] * delta[j] for j in range(self.structure[currentLayer + 1])]))

            delta = currentDelta[:]
            for i in range(self.structure[currentLayer]):
                for r in range(self.structure[currentLayer - 1]):
                    newConfig.layers[currentLayer].neurons[i].weights[r] = self.layers[currentLayer].neurons[i].weights[r] + learnRate * delta[i] * self.layers[currentLayer - 1].neurons[r].output
        self.layers = deepcopy(newConfig.layers)

    def computeLoss(self, inputValues, outputValues):
        loss = []
        out = self.feedForward(inputValues)
        loss.append(outputValues - out)
        return loss[:]

    def __str__(self):
        s = ''
        for i in range(self.noLayers):
            s += ' l ' + str(i) + ':' + str(self.layers[i])
        return s

