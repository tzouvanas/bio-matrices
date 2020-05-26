import numpy as np 
from BioMatrix import DynamicProgrammingMatrix
from BioMatrix import WeightMatrix
from Blosum import blosum50

#xSeq = ['A', 'A', 'G' ,'T' , 'T', 'A', 'G', 'C', 'A', 'G']
#ySeq = ['C', 'A', 'G' ,'T' , 'A', 'T', 'C', 'G', 'C', 'A']
#d = 1

class UnitOfWork_3:

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

        wm = WeightMatrix()
        wm.addSequence("TATAGA")
        wm.addSequence("TATAAA")
        wm.addSequence("TATAGA")
        wm.addSequence("TATAAA")
        wm.addSequence("GATAGT")
        wm.addSequence("TATAAT")
        wm.addSequence("TATAAT")
        wm.addSequence("TATAGT")
        wm.update()
        wm.print() 

        wm.printScore("TATAAA")

        wm.printScore("GATAAA")

        wm.printScore("TAATAA")



