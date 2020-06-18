from matrices.methods.AlignmentMethod import AlignmentMethod

class NeedlemanWunschMethod(AlignmentMethod):
    
    def __init__(self, d, lookupTable:dict):
        super().__init__(d, lookupTable)

    def calculate(self, upleft, left, up, x, y):
        super().adjustValues(upleft, left, up, x, y)
        maxResult =  max(self.upleft, self.left, self.up) 
        return maxResult

    def init(self, n):
        return -n * self.d