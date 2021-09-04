import numpy as np
import time

from globals import *
from core import Core
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
# show_queue(TaskQ.task_queue)
sort_taskQ = sort_task(TaskQ.task_queue)
show_queue(sort_taskQ)

print(f"current time：{t}")
readyQ = ReadyQueue()
readyQ.get_arrived_tasks(TaskQ, t)
# show_queue(readyQ.ready_queue)
m = min(Ncore, readyQ.size)
for j in range(m):
    Cores[j].append_task_to_dispatcher(
        readyQ.ready_queue[j], FIRST_ASSIGNMENT=True)
readyQ.pop_tasks(m, TaskQ)
print()
# show_queue(readyQ.ready_queue)
show_Cores(Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # # simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)

############## Schedule Start #################
# print("t = 1 Start！")
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# print("t = 1 Ready queue歸零！")
# # simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=1, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# print("t = 2 Start！!!!!!!!!!!!!!!")
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # # # simulation_iter(t=2, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # print("t = 2 Ready queue歸零！")
# print("t = 3 Start！!!!!!!!!!!!!!!")

# simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=3, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)

# print("t = 3 Ready queue歸零！")
# print("t = 4 Start！!!!!!!!!!!!!!!")

# simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # # simulation_iter(t=4, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)

# print("t = 4 Ready queue歸零！")
# print("t = 5 Start！!!!!!!!!!!!!!!")

# simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)
# # simulation_iter(t=5, PopSize=PopSize, Ncore=Ncore, TaskQ=TaskQ, Cores=Cores)

# t = 1
# print(f"current time：{t}")
# ----- First Assignment for each core -----
# readyQ = ReadyQueue()
# readyQ.get_arrived_tasks(TaskQ, t)
# show_queue(readyQ.ready_queue)
# qpv = QuantumPop(PopSize=PopSize, varSize=Ncore)
# cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
# fitness_agent = FitnessAgent(PopSize=PopSize, varSize=Ncore)
# qpv.init_quantumPop()
# # qpv.show_Qpopulation()
# cpv.SSO_Measure(qpv)
# cpv.get_ordering_schedules_by_permutation_trim()
# m = min(Ncore, readyQ.size)
# cpv.calculate_Task_index_schedules(m, readyQ.get_index())
# # cpv.show_ClassicalPopulation()
# for i in range(PopSize):
#     fitness = 0
#     for j in range(Ncore):
#         if (cpv.tasks_index_schedules[i, j] == -1):
#             continue
#         task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[i, j])
#         fitness += Cores[j].evaluate_fitness(task)
#     cpv.fitness[i] = fitness

# print(f"cpv.fitness: ", cpv.fitness)
# for j in range(Ncore):
#     if (cpv.tasks_index_schedules[0, j] == -1):
#         continue
#     task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[0, j])
#     Cores[j].append_task_to_dispatcher(task)

# readyQ.pop_tasks(Ncore, TaskQ)
# show_queue(readyQ.ready_queue)
# # ================= t = 1, round 2 =================
# print("\n==================== t = 1, round 2 ====================")
# readyQ = ReadyQueue()
# readyQ.get_arrived_tasks(TaskQ, t)
# show_queue(readyQ.ready_queue)
# qpv = QuantumPop(PopSize=PopSize, varSize=Ncore)
# cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
# fitness_agent = FitnessAgent(PopSize=PopSize, varSize=Ncore)
# qpv.init_quantumPop()
# # qpv.show_Qpopulation()
# cpv.SSO_Measure(qpv)
# cpv.get_ordering_schedules_by_permutation_trim()
# m = min(Ncore, readyQ.size)
# cpv.calculate_Task_index_schedules(m, readyQ.get_index())
# # cpv.show_ClassicalPopulation()
# for i in range(PopSize):
#     fitness = 0
#     for j in range(Ncore):
#         if (cpv.tasks_index_schedules[i, j] == -1):
#             continue
#         task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[i, j])
#         fitness += Cores[j].evaluate_fitness(task)
#     cpv.fitness[i] = fitness

# print(f"cpv.fitness: ", cpv.fitness)
# for j in range(Ncore):
#     if (cpv.tasks_index_schedules[0, j] == -1):
#         continue
#     task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[0, j])
#     Cores[j].append_task_to_dispatcher(task)

# readyQ.pop_tasks(Ncore, TaskQ)
# show_queue(readyQ.ready_queue)


# while TaskQ.unscheduled_tasks.size != 0:
#     t = int(time.time() - start_t + 1)
#     # print(f"current time：{t}")
# # ----- First Assignment for each core -----
#     readyQ = ReadyQueue()
#     readyQ.get_arrived_tasks(TaskQ, t)
#     qpv = QuantumPop(PopSize=PopSize, varSize=Ncore)
#     cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
#     fitness_agent = FitnessAgent(PopSize=PopSize, varSize=Ncore)
#     qpv.init_quantumPop()
#     # qpv.show_Qpopulation()
#     cpv.SSO_Measure(qpv)
#     cpv.get_ordering_schedules_by_permutation_trim()
#     m = min(Ncore, readyQ.size)
#     cpv.calculate_Task_index_schedules(m, readyQ.get_index())
#     # cpv.show_ClassicalPopulation()
#     for i in range(PopSize):
#         fitness = 0
#         for j in range(Ncore):
#             if (cpv.tasks_index_schedules[i, j] == -1):
#                 continue
#             task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[i, j])
#             fitness += Cores[j].evaluate_fitness(task)
#         cpv.fitness[i] = fitness

#     print(f"cpv.fitness: ", cpv.fitness)
#     for j in range(Ncore):
#         if (cpv.tasks_index_schedules[0, j] == -1):
#             continue
#         task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[0, j])
#         print("task: ", task)
#         Cores[j].append_task_to_dispatcher(task)
#     readyQ.pop_tasks(Ncore, TaskQ)

# for core in Cores:
#     print(core.dispatcher)

# readyQ = ReadyQueue()
# readyQ.get_arrived_tasks(TaskQ, 0.3)
# # show_queue(readyQ.ready_queue)

# qpv = QuantumPop(PopSize=PopSize, varSize=Ncore)
# cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
# qpv.init_quantumPop()
# # qpv.show_Qpopulation()
# cpv.SSO_Measure(qpv)
# cpv.get_ordering_schedules_by_permutation_trim()
# cpv.calculate_Task_index_schedules(
#     tasks_size=2, ready_queue=readyQ.get_index())
# cpv.show_ClassicalPopulation()

############## Schedule End #################
end_t = time.time()
duration = end_t - start_t
print(f"Time Cost: {duration}")
