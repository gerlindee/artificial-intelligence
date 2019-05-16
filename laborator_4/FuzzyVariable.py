
class FuzzyVariable:
    def __init__(self, label):
        self._label = label
        self._membershipSet = []

    def addSet(self, set):
        self._membershipSet.append(set)

    def membership(self, x):
        set = []
        for s in self._membershipSet:
            set.append([s.getLabel(), s.fuzzification(x)])
        return set

    def getSetLength(self):
        return len(self._membershipSet)

    def getSet(self):
        return self._membershipSet
