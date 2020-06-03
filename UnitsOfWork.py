import numpy as np 
from matrices.DynamicProgrammingMatrix import DynamicProgrammingMatrix
from matrices.WeightMatrix import PositionWeightMatrix
from Blosum import blosum50

#xSeq = ['A', 'A', 'G' ,'T' , 'T', 'A', 'G', 'C', 'A', 'G']
#ySeq = ['C', 'A', 'G' ,'T' , 'A', 'T', 'C', 'G', 'C', 'A']
#d = 1

class erg3:

    def go(self):

        xSeq = "GAATTC"
        ySeq = "GATTA"

        dm = DynamicProgrammingMatrix(xSeq, ySeq, 2)
        dm.update()
        dm.printMatrix()
        dm.print_origins_of(5, 6)

        xSeq = "HEAGAWGHEE"
        ySeq = "PAWHEAE"
        dm = DynamicProgrammingMatrix(xSeq, ySeq, 6)
        dm.setSubstitutionMatrix(blosum50)
        dm.update()
        dm.printMatrix()
        dm.print_origins_of(7, 10)

        dm = DynamicProgrammingMatrix(xSeq, ySeq, 6, True)
        dm.setSubstitutionMatrix(blosum50)
        dm.update()
        dm.printMatrix()
        dm.print_origins_of(7, 10)

        wm = PositionWeightMatrix()
        wm.add_sequence("TATAGA")
        wm.add_sequence("TATAAA")
        wm.add_sequence("TATAGA")
        wm.add_sequence("TATAAA")
        wm.add_sequence("GATAGT")
        wm.add_sequence("TATAAT")
        wm.add_sequence("TATAAT")
        wm.add_sequence("TATAGT")
        wm.update()
        wm.print() 

        wm.print_score("TATAAA")

        wm.print_score("GATAAA")

        wm.print_score("TAATAA")



