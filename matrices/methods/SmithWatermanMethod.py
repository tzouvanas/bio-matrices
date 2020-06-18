from matrices.methods.AlignmentMethod import AlignmentMethod

class SmithWatermanMethod(AlignmentMethod):
    
    def __init__(self, d, lookupTable:dict):
        super().__init__(d, lookupTable)

    def init(self, n):
        return 0

    def maxFormula(self, upleftScore, leftScore, upScore):
        maxResult =  max(upleftScore, leftScore, upScore, 0) 
        return maxResult


