import numpy as np

class WeightMatrix:

    def __init__(self):
        self.m = None
        self.m_counts = []
        self.m_probabilities = []
        self.m_pssm = []

    def __nucleotide_to_index(self, nucleotide):
        
        if nucleotide == 'A':
            return 0
        if nucleotide == 'T':
            return 1
        if nucleotide == 'G':
            return 2
        if nucleotide == 'C':
            return 3
        return -1

    def __count_occurencies_for_column(self, column):
        result = []
        result.append(column.count('A'))
        result.append(column.count('T'))
        result.append(column.count('G'))
        result.append(column.count('C'))
        return result

    def __countOccurenciesForMatrix(self):
        nrOfColumns = len(self.m[0])

        temp_counts = []
        for j in range(0, nrOfColumns):
            column = list(self.m[:,j])
            column_counts = self.__count_occurencies_for_column(column)
            temp_counts.append(column_counts)
        
        self.m_counts = np.transpose(temp_counts)

    def add_sequence(self, sequence):

        if self.m is None:
            self.m = list(sequence)
        else:
            self.m = np.vstack((self.m, list(sequence)))
    
    def update(self):   
        
        self.__countOccurenciesForMatrix()

        # propabilities
        self.m_probabilities = np.divide(self.m_counts, len(self.m))

        #pssm
        temp_pssm = np.divide(self.m_probabilities, 0.25)
        temp_pssm = np.log(temp_pssm)
        temp_pssm = np.round(temp_pssm, 3)

        self.m_pssm = temp_pssm
    

    def print_score(self, sequence):
        score = 0
        columnIndex = 0
        nucleotides = list(sequence)

        for nucleotide in list(nucleotides):
            index = self.__nucleotide_to_index(nucleotide)
            score = score + self.m_pssm[index][columnIndex]
            columnIndex = columnIndex + 1

        print(sequence, ' : ', score)
        print('\n')

    def print(self):    
        print('Counters:')
        print(self.m_counts)
        print('\n')
        print('Propabilities:')
        print(self.m_probabilities)
        print('\n')
        print('PSSM:')
        print(self.m_pssm)
        print('\n')
