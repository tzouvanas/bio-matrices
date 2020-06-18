class AlignmentMethod:
    
    def __init__(self,d):
        self.d = d
    
    def calculate(self, upleft, left, up):
        raise Exception("Abstract method") 

    def init(self):
        raise Exception("Abstract method")
