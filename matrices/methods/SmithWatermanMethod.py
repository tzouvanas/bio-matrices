from matrices.methods.AlignmentMethod import AlignmentMethod

class SmithWatermanMethod(AlignmentMethod):
    
    def __init__(self, d, lookupTable:dict):
        super().__init__(d, lookupTable)

    def calculate(self, upleft, left, up, x, y):
        super().adjustValues(upleft, left, up, x, y)
        maxResult =  max(self.upleft, self.left, self.up, 0) 
        return maxResult

    def init(self, n):
        return 0

