
class FuzzySet:
    def __init__(self, label, values):
        self._label = label
        # the triangle values
        self._a = values[0]
        self._b = values[1]
        self._c = values[2]

    def fuzzification(self, x):
        # triangular membership function
        minimum = min((x - self.getLeftCorner()) / (self.getCenter() - self.getLeftCorner()), 1, (self.getRightCorner() - x) / (self.getRightCorner() - self.getCenter()))
        return max(minimum, 0)

    def getCenter(self):
        return self._b

    def getLeftCorner(self):
        return self._a

    def getRightCorner(self):
        return self._c

    def getLabel(self):
        return self._label
