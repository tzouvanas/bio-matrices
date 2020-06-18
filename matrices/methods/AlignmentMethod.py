from matrices.lookupTables.LookupWrapper import LookupWrapper
class AlignmentMethod:
    
    def __init__(self,d, lookupTable:dict):
        self.d = d
        self.lookupTable = lookupTable
    
    def calculate(self, upleft, left, up):
        raise Exception("Abstract method") 

    def init(self):
        raise Exception("Abstract method")

    def calculateMatchingScore(self, x, y):
        
        if self.lookupTable is None:
            if x == y:
                return 1
            return -1

        lookupWrapper = LookupWrapper(self.lookupTable)
        value = lookupWrapper.get(x, y)
        
        return value

