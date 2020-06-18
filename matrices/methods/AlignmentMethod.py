class AlignmentMethod:
    
    def __init__(self,d, lookupTable:dict):
        self.d = d
        self.lookupTable = lookupTable
    
    def calculate(self, upleft, left, up):
        raise Exception("Abstract method") 

    def init(self):
        raise Exception("Abstract method")
