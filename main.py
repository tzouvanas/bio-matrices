from UnitsOfWork import erg3
from DynamicProgrammingMatrix import DynamicProgrammingMatrix

ergasia = erg3() 
ergasia.go()

xSeq = "ATAG"
ySeq = "TTCG"

dm = DynamicProgrammingMatrix(xSeq, ySeq, 1)
dm.update()

dm.printMatrix()
dm.print_origins_of(4,4)
