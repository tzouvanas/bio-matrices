import numpy as np
from Math import MathTools
from matrices.methods.AlignmentMethod import AlignmentMethod
from matrices.lookupTables.LookupWrapper import LookupWrapper


class DynamicProgrammingMatrix:

    def __init__(self, xSeq, ySeq, method:AlignmentMethod):

        self.xSeq = list(xSeq)
        self.ySeq = list(ySeq)

        self.method = method
        self.substitutionMatrix = None

        self.nrOfRows = len(ySeq)+1
        self.nrOfColumns = len(xSeq)+1

        self.origins = {}

    # initialize matrix values
    def __init__matrice_values(self):
        self.m = np.zeros((self.nrOfRows, self.nrOfColumns))
        self.__init__first_column()
        self.__init__first_row()

    # initialize first row
    def __init__first_row(self):
        for j in range(1, self.nrOfColumns):

            self.m[0][j] = self.method.init(j)
            
            # init first row origings
            self.origins[0,j] = [(0, j-1)]

    # initialize first column
    def __init__first_column(self):
        for i in range(1, self.nrOfRows):

            self.m[i][0] = self.method.init(i)

            # init first column origings
            self.origins[i,0] = [(i-1, 0)]

    def __calculateMatchingScore(self, i, j):

        if self.substitutionMatrix is None:
            if self.xSeq[j-1] == self.ySeq[i-1]:
                return 1
            return -1

        # go with scores in replacement matrix. Symmetric matrix is assumed !
        lookupWrapper = LookupWrapper(self.substitutionMatrix)
        value = lookupWrapper.get(self.xSeq[j-1], self.ySeq[i-1])
        
        return value

    def __calculateMaxValueForCell(self, i, j):

        upleft = self.m[i-1][j-1] + self.__calculateMatchingScore(i, j)
        left = self.m[i][j-1] - self.method.d
        up = self.m[i-1][j] - self.method.d

        maxResult = self.method.calculate(upleft, left, up)
        self.__register_origin(upleft, left, up, maxResult, i, j)

        return maxResult

    # records originator / originators of cell's max value
    def __register_origin(self, upleft, left, up, maxValue, i, j):

        origin = []

        if  (maxValue == upleft):
            origin.append((i-1,j-1))

        if (maxValue == up):
            origin.append((i-1,j))

        if (maxValue == left):
            origin.append((i,j-1))
        
        self.origins[(i, j)] = origin

    def __calculate_permutation_index_table(self, countArray):

        lists = []
        for j in range(0, len(countArray)):
            lists.append(list(range(0, countArray[j])))
        
        if (len(lists) == 1):
            return np.transpose(lists)

        result = MathTools.cartesian_of_many(lists)

        return result

    def __permutate_origins(self, permutationIndexRow):
        
        permutatedOrigin = self.origins.copy()
        
        seq = 0
        for permutation_cell in self.__permutationCells:
            permutatedOrigin[permutation_cell] = [permutatedOrigin[permutation_cell][int(permutationIndexRow[seq])]]
            seq = seq + 1
        
        return permutatedOrigin

    def __find_permutations_of_cell(self, i, j):
        
        if ((i, j) in self.origins):
            
            nodes = self.origins[(i, j)]

            if (nodes == None) | (len(nodes) == 0):
                return

            if len(nodes) > 1:
                self.__permutationCells.append((i,j))

            for node in nodes:
                if (node != (0,0)):
                    self.__find_permutations_of_cell(node[0], node[1])

    def __calculate_permutated_origin_path_of(self, i, j):
        
        self.permutation_origin_path.append((i, j))

        if ((i, j) in self.__permutatedOrigin):
            
            nodes = self.__permutatedOrigin[(i, j)]

            if (nodes == None) | (len(nodes) == 0):
                return

            nextNode = nodes[0]

            if (nextNode != (0,0)):
                self.__calculate_permutated_origin_path_of(nextNode[0], nextNode[1])

    def setSubstitutionMatrix(self, substitutionMatrix):
        self.substitutionMatrix = substitutionMatrix

    def update(self):
        
        self.__init__matrice_values()

        for i in range(1, self.nrOfRows):
            for j in range(1, self.nrOfColumns):
                self.m[i][j] = self.__calculateMaxValueForCell(i, j)

    def print_matrix(self):
        print('Dynamic Programming Matrix:')
        print(self.m)
        print('\n')

    def print_origins_of(self, i, j):
        
        # find cells that cause permutations
        self.__permutationCells = []
        self.__find_permutations_of_cell(i, j)

        # record nr of permutations per cell
        nrOfnodesPerPermutationCell = []
        for permutationCell in self.__permutationCells:
            nrOfnodesPerPermutationCell.append(len(self.origins[permutationCell]))
            
        # create permutation index table
        permutationIndexTable = self.__calculate_permutation_index_table(nrOfnodesPerPermutationCell)
        
        self.__permutated_origins = []

        if permutationIndexTable is None:
            self.__permutated_origins.append(self.origins.copy())
        else:
            # create permutations of origins
            for permutationIndexRow in permutationIndexTable:
                permutatedOrigin = self.__permutate_origins(permutationIndexRow)
                self.__permutated_origins.append(permutatedOrigin)
                    
        self.permutation_origin_path = []
        self.all_origin_paths = []
        
        for permutatedOrigin in self.__permutated_origins:
            self.__permutatedOrigin = permutatedOrigin
            self.__calculate_permutated_origin_path_of(i, j)
            self.all_origin_paths.append(self.permutation_origin_path)
            self.permutation_origin_path = []

        print('Paths:')
        for the_path_to_righteousness in self.all_origin_paths:
            print(the_path_to_righteousness)
        
        print('\n')
        
