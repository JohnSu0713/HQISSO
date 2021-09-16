import numpy as np
from beautifultable import BeautifulTable
from TaskQueue import ReadyQueue
from quantum_pop import QuantumPop
from classical_pop import ClassicalPop
from best import FitnessAgent
from globals import *


def sort_task(task_queue, target_col=4):
    '''
    Initialize task_queue with Ai, Ri, Ci and Di for each real-time task i.
    array structure: [index, Ai, Ri, Ci, Di]
    array sorted parameter: [index->0, Ai->1, Ri->2, Ci->3, Di->4]
    '''
    return task_queue[np.argsort(task_queue[:, target_col])]


def show_queue(queue):
    task_queue_table = BeautifulTable()
    task_queue_table.rows.append(["index", "Ai", "Ri", "Ci", "Di"])

    for task in queue:
        task_queue_table.rows.append([int(task[0]), np.round(task[1], 2), np.round(
            task[2], 2), np.round(task[3], 2), np.round(task[4], 2)])
    print(task_queue_table)


def show_Cores(Cores):
    for i in range(len(Cores)):
        Cores[i].show_core_info(i)


# def simulation_iter(t, PopSize, Ncore, TaskQ, Cores, GEN_MAX=generation_max):
#     # print(f"current time：{t}")
#     # ----- First Assignment for each core -----
#     readyQ = ReadyQueue()
#     readyQ.get_arrived_tasks(TaskQ, t)
#     show_queue(readyQ.ready_queue)
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
#     ############# Calculate fitness for current population #############
#     for i in range(PopSize):
#         fitness = 0
#         for j in range(Ncore):
#             if (cpv.tasks_index_schedules[i, j] == -1):
#                 fitness += Cores[j].evaluate_fitness(
#                     task=np.empty([1, 5]), NEW_TASKS=False)
#             else:
#                 task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[i, j])
#                 fitness += Cores[j].evaluate_fitness(task=task, NEW_TASKS=True)
#         cpv.fitness[i] = fitness
#     # print(f"cpv.fitness: ", cpv.fitness)
#     fitness_agent.best_update(cpv)
#     # fitness_agent.show_best()

#     GEN = 0
#     while GEN < GEN_MAX-1:
#         # print()
#         # print(" ============== GEN: ",
#         #       GEN + 1, " ============== \n")

#         qpv.rotate(cpv, fitness_agent)
#         cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
#         cpv.SSO_Measure(qpv)
#         cpv.get_ordering_schedules_by_permutation_trim()
#         m = min(Ncore, readyQ.size)
#         cpv.calculate_Task_index_schedules(m, readyQ.get_index())
#         ############# Calculate fitness for current GEN population #############
#         for i in range(PopSize):
#             fitness = 0
#             for j in range(Ncore):
#                 if (cpv.tasks_index_schedules[i, j] == -1):
#                     fitness += Cores[j].evaluate_fitness(
#                         task=np.empty([1, 5]), NEW_TASKS=False)
#                 else:
#                     task = TaskQ.get_tasks_info(
#                         cpv.tasks_index_schedules[i, j])
#                     fitness += Cores[j].evaluate_fitness(
#                         task=task, NEW_TASKS=True)
#             cpv.fitness[i] = fitness
#         # print(f"cpv.fitness: ", cpv.fitness)
#         fitness_agent.best_update(cpv)
#         # fitness_agent.show_best()
#         GEN += 1

#     ############# Schedule Global best #############
#     for j in range(Ncore):
#         if (fitness_agent.gbest_tasks_schedule[j] == -1):
#             continue
#         task = TaskQ.get_tasks_info(fitness_agent.gbest_tasks_schedule[j])

#         Cores[j].append_task_to_dispatcher(task)

#     readyQ.pop_tasks(Ncore, TaskQ)
#     # cpv.show_ClassicalPopulation()
#     show_queue(readyQ.ready_queue)
#     # fitness_agent.show_best()
#     show_Cores(Cores)
#     print("Unscheduled Size: ", len(TaskQ.unscheduled_tasks))
#     print("################# END ################\n\n\n")


def simulation_iter(t, PopSize, Ncore, TaskQ, Cores, GEN_MAX=generation_max):
    # print(f"current time：{t}")
    # ----- First Assignment for each core -----
    readyQ = ReadyQueue()
    readyQ.get_arrived_tasks(TaskQ, t)
    # show_queue(readyQ.ready_queue)
    qpv = QuantumPop(PopSize=PopSize, varSize=Ncore)
    cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
    fitness_agent = FitnessAgent(PopSize=PopSize, varSize=Ncore)
    qpv.init_quantumPop()
    # qpv.show_Qpopulation()
    cpv.SSO_Measure(qpv)
    cpv.get_ordering_schedules_by_permutation_trim()
    m = min(Ncore, readyQ.size)
    cpv.calculate_Task_index_schedules(m, readyQ.get_index())
    # cpv.show_ClassicalPopulation()
    ############# Calculate fitness for current population #############
    for i in range(PopSize):
        fitness = 0
        for j in range(Ncore):
            if (cpv.tasks_index_schedules[i, j] == -1):
                fitness += Cores[j].evaluate_fitness(
                    task=np.empty([1, 5]), NEW_TASKS=False)
            else:
                task = TaskQ.get_tasks_info(cpv.tasks_index_schedules[i, j])
                fitness += Cores[j].evaluate_fitness(task=task, NEW_TASKS=True)
        cpv.fitness[i] = fitness
    print(f"cpv.fitness: ", cpv.fitness)
    fitness_agent.best_update(cpv)
    # fitness_agent.show_best()

    GEN = 0
    while GEN < GEN_MAX-1:
        print()
        print(" ============== GEN: ",
              GEN + 1, " ============== \n")

        qpv.rotate(cpv, fitness_agent)
        cpv = ClassicalPop(PopSize=PopSize, varSize=Ncore)
        cpv.SSO_Measure(qpv)
        cpv.get_ordering_schedules_by_permutation_trim()
        m = min(Ncore, readyQ.size)
        cpv.calculate_Task_index_schedules(m, readyQ.get_index())
        ############# Calculate fitness for current GEN population #############
        for i in range(PopSize):
            fitness = 0
            for j in range(Ncore):
                if (cpv.tasks_index_schedules[i, j] == -1):
                    fitness += Cores[j].evaluate_fitness(
                        task=np.empty([1, 5]), NEW_TASKS=False)
                else:
                    task = TaskQ.get_tasks_info(
                        cpv.tasks_index_schedules[i, j])
                    fitness += Cores[j].evaluate_fitness(
                        task=task, NEW_TASKS=True)
            cpv.fitness[i] = fitness
        print(f"cpv.fitness: ", cpv.fitness)
        fitness_agent.best_update(cpv)
        fitness_agent.show_best()
        # cpv.show_ClassicalPopulation()
        # qpv.show_Qpopulation()
        GEN += 1

    ############# Schedule Global best #############
    for j in range(Ncore):
        if (fitness_agent.gbest_tasks_schedule[j] == -1):
            continue
        task = TaskQ.get_tasks_info(fitness_agent.gbest_tasks_schedule[j])

        Cores[j].append_task_to_dispatcher(task)

    readyQ.pop_tasks(Ncore, TaskQ)
    # cpv.show_ClassicalPopulation()
    # show_queue(readyQ.ready_queue)
    # fitness_agent.show_best()
    # show_Cores(Cores)
    print("Unscheduled Size: ", len(TaskQ.unscheduled_tasks))
    print("################# END ################\n\n\n")
