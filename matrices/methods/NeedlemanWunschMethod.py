from matrices.methods.AlignmentMethod import AlignmentMethod

class NeedlemanWunschMethod(AlignmentMethod):
    
    def __init__(self, d, lookupTable:dict):
        super().__init__(d, lookupTable)

    def init(self, n):
        return -n * self.d

    def maxFormula(self, upleftScore, leftScore, upScore):
        maxResult =  max(upleftScore, leftScore, upScore) 
        return maxResult
