from unitOfWork_3 import UnitOfWork_3
from BioMatrix import DynamicProgrammingMatrix

erg_3 = UnitOfWork_3() 
erg_3.go()

xSeq = "ATAG"
ySeq = "TTCG"

dm = DynamicProgrammingMatrix(xSeq, ySeq, 1)
dm.update()

dm.printMatrix()
dm.print_origins_of(4,4)
