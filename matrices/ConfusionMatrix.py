 
import numpy as np

class ConfusionMatrix:

    def __init__(self, nrOfClasses:int):
        self.nrOfClasses = nrOfClasses
        self.matrix = []

    def loadRow(self, row:list):
        if len(row) != self.nrOfClasses:
            raise Exception('Invalid array dimention. Expected value of {}'.format(self.nrOfClasses))
        self.matrix.append(row)
    
    def truePositiveOf(self, index:int):
        return self.matrix[index][index]
         
    def trueNegativeOf(self, index:int):
        return np.sum(self.matrix) - np.sum(self.matrix[index]) - np.sum(np.transpose(self.matrix)[index]) + self.truePositiveOf(index)

    def falsePositiveOf(self, index:int):
        return np.sum(np.transpose(self.matrix)[index]) - self.truePositiveOf(index)
    
    def falseNegativeOf(self, index:int):
        return np.sum(self.matrix[index]) - self.truePositiveOf(index)

    def sensitivityOf(self, index:int):
        tp = self.truePositiveOf(index)
        fn = self.falseNegativeOf(index)
        return round(tp / (tp + fn), 3)

    def specificityOf(self, index:int):
        tn = self.trueNegativeOf(index)
        fp = self.falsePositiveOf(index)
        return round(tn / (tn + fp), 3)

    def statsOf(self, index:int):
        sensitivity = self.sensitivityOf(index)
        specificity = self.specificityOf(index)
        return (sensitivity, specificity)

    def printStatsOf(self, index:int):
        stats = self.statsOf(index)
        print('index {}: [Sensitivity - Specifity] =  [{} - {}]'.format(index, stats[0], stats[1]))

    def totalSensitivity(self):
        tps = []
        for i in range(0, self.nrOfClasses):
            tps.append(self.truePositiveOf(i)) 

        fns = []
        for i in range(0, self.nrOfClasses):
            fns.append(self.falseNegativeOf(i)) 

        tp_total = np.sum(tps)
        fn_total = np.sum(fns)
        return round(tp_total / (tp_total + fn_total), 3)

    def totalSpecificity(self):
        tns = []
        for i in range(0, self.nrOfClasses):
            tns.append(self.trueNegativeOf(i)) 

        fps = []
        for i in range(0, self.nrOfClasses):
            fps.append(self.falsePositiveOf(i)) 

        tn_total = np.sum(tns)
        fp_total = np.sum(fps)

        return round(tn_total / (tn_total + fp_total), 3)