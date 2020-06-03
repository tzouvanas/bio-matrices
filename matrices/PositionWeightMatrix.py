import numpy as np

class PositionWeightMatrix:

    def __init__(self):
        self.m = None
        self.position_frequency_matrix = []
        self.position_probability_matrix = []
        self.position_weight_matrix = []

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

    def __count_frequencies(self):
        nrOfColumns = len(self.m[0])

        temp_counts = []
        for j in range(0, nrOfColumns):
            column = list(self.m[:,j])
            column_counts = self.__count_occurencies_for_column(column)
            temp_counts.append(column_counts)
        
        self.position_frequency_matrix = np.transpose(temp_counts)

    def add_sequence(self, sequence):

        if self.m is None:
            self.m = list(sequence)
        else:
            self.m = np.vstack((self.m, list(sequence)))
    
    def update(self):   
        
        # frequencies
        self.__count_frequencies()

        # propabilities
        self.position_probability_matrix = np.divide(self.position_frequency_matrix, len(self.m))

        # weights
        temp_position_weight_matrix = np.divide(self.position_probability_matrix, 0.25)
        temp_position_weight_matrix = np.log(temp_position_weight_matrix)
        temp_position_weight_matrix = np.round(temp_position_weight_matrix, 3)
        self.position_weight_matrix = temp_position_weight_matrix

    def score(self, sequence):
        score = 0
        columnIndex = 0
        nucleotides = list(sequence)

        for nucleotide in list(nucleotides):
            index = self.__nucleotide_to_index(nucleotide)
            score = score + self.position_weight_matrix[index][columnIndex]
            columnIndex = columnIndex + 1

    def print_score(self, sequence):
        print(sequence, ' : ', self.score(sequence))
        print('\n')

    def print(self):    
        print('Frequencies:')
        print(self.position_frequency_matrix)
        print('\n')
        print('Propabilities:')
        print(self.position_probability_matrix)
        print('\n')
        print('Weights:')
        print(self.position_weight_matrix)
        print('\n')
