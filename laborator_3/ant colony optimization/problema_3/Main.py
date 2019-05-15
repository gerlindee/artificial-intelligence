
class Problem:
    def __init__(self, fileName):
        self._words = self.loadFile(fileName)

    @staticmethod
    def loadFile(fileName):
        words = []
        file = open(fileName, "r")
        for line in file:
            print(line)
        return words


    def getNumberWords(self):
        return len(self._words)

