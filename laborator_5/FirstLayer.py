from ActivationFunctions import identical
from Layer import Layer


class FirstLayer(Layer):
    def __init__(self, noOfNeurons, bias=False):
        if bias:
            noOfNeurons = noOfNeurons + 1
        # here we chose the identical function as an activation function
        Layer.__init__(self, 1, identical, noOfNeurons)
        for x in self.neurons:
            x.setWeights([1])

    def forward(self, inputs):
        for i in range(len(self.neurons)):
            self.neurons[i].fireNeuron([inputs[i]])
        return [x.output for x in self.neurons]