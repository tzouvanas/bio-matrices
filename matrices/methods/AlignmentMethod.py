from matrices.lookupTables.LookupWrapper import LookupWrapper
class AlignmentMethod:
    
    def __init__(self,d, lookupTable:dict):
        self.d = d
        self.lookupTable = lookupTable
 
    def init(self):
        raise Exception("Abstract method")

    def calculate(self, upleft, left, up, x, y):
        
        upleftScore = upleft + self.matchingScore(x, y)
        leftScore = left - self.d
        upScore = up - self.d

        maxResult = self.maxFormula(upleftScore, leftScore, upScore)
        maxIndex = self.resolveMaxIndeces(maxResult, upleftScore, leftScore, upScore)

        return (maxResult, maxIndex)
    
    def maxFormula(self, upleftScore, leftScore, upScore):
        return -1

    def matchingScore(self, x, y):
        
        if self.lookupTable is None:
            if x == y:
                return 1
            return -1

        lookupWrapper = LookupWrapper(self.lookupTable)
        value = lookupWrapper.get(x, y)
        
        return value

    def resolveMaxIndeces(self, maxResult, upleftScore, leftScore, upScore):

        maxIndeces = []

        if  (maxResult == upleftScore):
            maxIndeces.append(1)

        if (maxResult == leftScore):
            maxIndeces.append(2)

        if (maxResult == upScore):
            maxIndeces.append(3)

        return maxIndeces

