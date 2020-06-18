from UnitsOfWork.DynamicProgrammingMatrixUnitOfWork import DynamicProgrammingMatrixUnitOfWork
from UnitsOfWork.PositionWeightMatrixUnitOfWork import PositionWeightMatrixUnitOfWork
from UnitsOfWork.TestUnitOfWork import TestUnitOfWork

dpm_work = DynamicProgrammingMatrixUnitOfWork()
dpm_work.go()

pwm_work = PositionWeightMatrixUnitOfWork()
pwm_work.go()

test_work = TestUnitOfWork()
test_work.go()