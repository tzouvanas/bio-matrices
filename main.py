from UnitsOfWork.DynamicProgrammingMatrixUnitOfWork import DynamicProgrammingMatrixUnitOfWork
from UnitsOfWork.PositionWeightMatrixUnitOfWork import PositionWeightMatrixUnitOfWork
from UnitsOfWork.ConfusionMatrixUnitOfWork import ConfusionMatrixUnitOfWork
from UnitsOfWork.TestUnitOfWork import TestUnitOfWork

dpm_work = DynamicProgrammingMatrixUnitOfWork()
dpm_work.go()

pwm_work = PositionWeightMatrixUnitOfWork()
pwm_work.go()

cfm_work = ConfusionMatrixUnitOfWork()
cfm_work.go()
