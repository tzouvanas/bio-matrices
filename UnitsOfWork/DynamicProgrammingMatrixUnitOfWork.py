import numpy as np 
from matrices.DynamicProgrammingMatrix import DynamicProgrammingMatrix
from matrices.PositionWeightMatrix import PositionWeightMatrix
from Blosum import blosum50

class DynamicProgrammingMatrixUnitOfWork:

    def go(self):

        #xSeq = ['A', 'A', 'G' ,'T' , 'T', 'A', 'G', 'C', 'A', 'G']
        #ySeq = ['C', 'A', 'G' ,'T' , 'A', 'T', 'C', 'G', 'C', 'A']
        #d = 1

        # global alignment example for nucleotides
        xSeq = "GAATTC"
        ySeq = "GATTA"
        dm = DynamicProgrammingMatrix(xSeq, ySeq, 2)
        dm.update()
        dm.print_matrix()
        dm.print_origins_of(5, 6)

        # global alignment example for proteins
        xSeq = "HEAGAWGHEE"
        ySeq = "PAWHEAE"
        dm = DynamicProgrammingMatrix(xSeq, ySeq, 6)
        dm.setSubstitutionMatrix(blosum50)
        dm.update()
        dm.print_matrix()
        dm.print_origins_of(7, 10)

        # local alignment example
        dm = DynamicProgrammingMatrix(xSeq, ySeq, 6, True)
        dm.setSubstitutionMatrix(blosum50)
        dm.update()
        dm.print_matrix()
        dm.print_origins_of(7, 10)