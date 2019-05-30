from Neuron import Neuron


class Layer:
    def __init__(self, noOfInputs, activationFunction, noOfNeurons):
        self.noOfNeurons = noOfNeurons
        self.neurons = [Neuron(noOfInputs, activationFunction) for i in range(self.noOfNeurons)]

    def forward(self, inputs):
        # propagate the information and modify the weights
        for x in self.neurons:
            x.fireNeuron(inputs)
        return [x.output for x in self.neurons]

    def __str__(self):
        s = ''
        for i in range(self.noOfNeurons):
            s += ' n ' + str(i) + ' ' + str(self.neurons[i]) + '\n'
        return s