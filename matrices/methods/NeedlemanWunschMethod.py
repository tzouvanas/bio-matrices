from matrices.methods.AlignmentMethod import AlignmentMethod

class NeedlemanWunschMethod(AlignmentMethod):
    
    def __init__(self, d):
        super().__init__(d)

    def calculate(self, upleft, left, up):
        maxResult =  max(upleft, left, up) 
        return maxResult

    def init(self, n):
        return -n * self.d