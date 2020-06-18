import numpy as np 
from matrices.DynamicProgrammingMatrix import DynamicProgrammingMatrix
from matrices.PositionWeightMatrix import PositionWeightMatrix
from matrices.methods.NeedlemanWunschMethod import NeedlemanWunschMethod
from matrices.lookupTables.Blosum import blosum50

class TestUnitOfWork:

    def go(self):

        # global alignment example for nucleotides
        xSeq = "GTGCCT"
        ySeq = "GATCCA"
        dm = DynamicProgrammingMatrix(xSeq, ySeq, NeedlemanWunschMethod(4, None))
        dm.update()
        dm.print_matrix()
        dm.print_origins_of(6, 6)
