from FuzzySet import FuzzySet
from FuzzyVariable import FuzzyVariable


class Controller:
    def __init__(self, problemFile, parametersFile):
        self._problemData = problemFile
        self._parametersFile = parametersFile
        self._temperature = None
        self._capacity = None
        self._power = None
        self._temperatureValue = None
        self._capacityValue = None
        self._rules = []
        self.readParameters()
        self.readData()

    @staticmethod
    def menu():
        print("0. Exit")
        print("1. Display the current temperature inside the furnace;")
        print("2. Display the current capacity of the furnace;")
        print("3. Display the rules;")
        print("4. Display the inferences;")
        print("5. Display the most efficient power mode for the furnace;")

    def readParameters(self):
        with open(self._parametersFile) as file:
            line = file.readline().strip('\n').split(' ')
            self._temperatureValue = float(line[0])
            self._capacityValue = float(line[1])

    def readData(self):
        with open(self._problemData) as file:
            line = file.readline().strip('\n').split(',')
            self._temperature = FuzzyVariable(line[0])
            self._capacity = FuzzyVariable(line[1])
            self._power = FuzzyVariable(line[2])

            for temps in range(5):
                line = file.readline().strip('\n').split(',')
                label = line[0]
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(label, values)
                self._temperature.addSet(set)

            for caps in range(3):
                line = file.readline().strip('\n').split(',')
                label = line[0]
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(label, values)
                self._capacity.addSet(set)

            for pows in range(3):
                line = file.readline().strip('\n').split(',')
                label = line[0]
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(label, values)
                self._power.addSet(set)

            for ruleCol in range(self._temperature.getSetLength()):
                line = file.readline().strip('\n').split(',')
                self._rules.append([])
                for ruleRow in range(self._capacity.getSetLength()):
                    self._rules[ruleCol].append(line[ruleRow])

    def inference(self):
        # forward inference
        # transforming the fuzzy inputs into fuzzy outputs by applying the rules
        inferences = {}
        temperatureList = self._temperature.membership(self._temperatureValue)
        capacityList = self._capacity.membership(self._capacityValue)
        for temp in range(0, len(temperatureList)):
            for cap in range(0, len(capacityList)):
                label = self._rules[temp][cap]
                if label in inferences.keys():
                    inferences[label].append(min(temperatureList[temp][1], capacityList[cap][1]))
                else:
                    inferences[label] = [min(temperatureList[temp][1], capacityList[cap][1])]

    @staticmethod
    def aggregate(inferences):
        # consider the membership functions for all the consequences and combine them into a single fuzzy set
        aggregated = []
        for inf in inferences:
            aggregated.append(max(inferences[inf]))
        return aggregated

    @staticmethod
    def defuzzify(aggregate, power):
        # transform the fuzzy result into a raw value
        # uses the center of area (COA) method
        # mamdani model -> estimation of COA by using a sample of points of the resulted fuzzy set
        s1 = 0.0
        s2 = 0.0
        centers = power.getSet()
        for i in range(len(aggregate)):
            s1 = s1 + aggregate[i] * centers[i].getCenter()
            s2 = s2 + aggregate[i]
        return s1 / s2

    @staticmethod
    def interpretResults(cy):
        maxim = -100000
        label = None
        for x in cy:
            if maxim < x[1]:
                maxim = x[1]
                label = x[0]
        return maxim, label

    def run(self):
        running = True
        while running:
            self.menu()
            command = input(">> ")
            if command == "1":
                pass
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass
            elif command == "5":
                pass
            elif command == "0":
                running = False
            else:
                print("Invalid command!")