from random import randint
from numpy import random


Ncore = random.randint(10, 20)
# Ncore = 16
Ntasks = 200
PopSize = 30
avg_arrival = 20
GEN_MAX = 48

Cg = 0.7                # define Cg
Cp = 0.9                # define Cp
# Cw = 0.9              # define Cw

min_c = 30
max_c = 60

Ri_param = 2
Di_lowerB = 2
Di_upperB = 3