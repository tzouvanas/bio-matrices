import numpy as np
from matrices.ConfusionMatrix import ConfusionMatrix 

class ConfusionMatrixUnitOfWork:
    
    def go(self):
        cm = ConfusionMatrix(4)
        cm.loadRow([70, 10, 15, 5])
        cm.loadRow([8,  67, 20, 5])
        cm.loadRow([0,  11, 88, 1])
        cm.loadRow([4,  10, 14, 72])

        cm.printStatsOf(0)
        cm.printStatsOf(1)
        cm.printStatsOf(2)
        cm.printStatsOf(3)

        print(cm.totalSensitivity())
        print(cm.totalSpecificity())