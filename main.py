import numpy as np
import time
from globals import *
from core import Core
from plot import PlotTool
from classical_pop import ClassicalPop
from quantum_pop import QuantumPop
from best import FitnessAgent
from globalFunc import *
from TaskQueue import TaskQueue, ReadyQueue

##################### Init #####################
start_t = time.time()
t = int(time.time() - start_t + 1)
Cores = [Core() for i in range(Ncore)]
TaskQ = TaskQueue(Ntasks)
TaskQ.init_tasks(Ncore)
############## First Task Assignment ################

print(f"current time：{t}")
readyQ = ReadyQueue()
readyQ.get_arrived_tasks(TaskQ, avg_arrival)
show_queue(readyQ.ready_queue)
# show_queue(readyQ.ready_queue)
m = min(Ncore, readyQ.size)
for j in range(m):
    Cores[j].append_task_to_dispatcher(
        readyQ.ready_queue[j], FIRST_ASSIGNMENT=True)
readyQ.pop_tasks(m, TaskQ)
print()
# show_queue(readyQ.ready_queue)
# show_Cores(Cores)

while TaskQ.unscheduled_tasks.size != 0:
    t = int(time.time() - start_t + 1)
    simulation_iter(t=t, PopSize=PopSize, Ncore=Ncore,
                    TaskQ=TaskQ, Cores=Cores)

############## Demo #################
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
#####################################
# show_queue(TaskQ.task_queue)

show_Cores(Cores)
############## Schedule End #################
end_t = time.time()
duration = end_t - start_t
print(f"Time Cost: {duration}")
gantt = PlotTool(Ncore)
gantt.plot_gantt(Cores)
