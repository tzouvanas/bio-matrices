from matrices.methods.AlignmentMethod import AlignmentMethod


class SmithWatermanMethod(AlignmentMethod):
    
    def __init__(self, d):
        super().__init__(d)

    def calculate(self, upleft, left, up):
        maxResult =  max(upleft, left, up, 0) 
        return maxResult

    def init(self, n):
        return 0

