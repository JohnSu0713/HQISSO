import numpy as np
import random
import math
from globals import *


class ClassicalPop():
    def __init__(self, PopSize=PopSize, varSize=Ncore):
        # Meta Information
        self.PopSize = PopSize
        self.varSize = varSize
        self.Nbit = math.ceil(math.log(self.varSize, 2))
        self.solSize = (self.Nbit * self.varSize)

        self.binary_solution = np.zeros(
            [self.PopSize, self.solSize], dtype=int)
        self.ordering_schedules = np.full((self.PopSize, self.varSize), -1)
        self.tasks_index_schedules = np.full((self.PopSize, self.varSize), -1)
        self.fitness = np.zeros((PopSize))

    def SSO_Measure(self, QuantumPop):
        for i in range(self.PopSize):
            for j in range(self.solSize):
                SSO_rnd = random.random()
                measure_rnd = random.random()
                if (SSO_rnd < Cg):
                    # print("Measure Q global")
                    if measure_rnd <= QuantumPop.Qgbest_sqr[j, 0]:

                        self.binary_solution[i, j] = 0
                    else:
                        self.binary_solution[i, j] = 1
                elif (SSO_rnd < Cp):
                    # print("Measure Q personal")
                    if measure_rnd <= QuantumPop.qpv_sqr[i, j, 0]:

                        self.binary_solution[i, j] = 0
                    else:
                        self.binary_solution[i, j] = 1
                else:
                    if measure_rnd <= 0.5:
                        # print("Random")
                        self.binary_solution[i, j] = 0
                    else:
                        self.binary_solution[i, j] = 1
            # print()
        # print()

    def get_ordering_schedules_by_permutation_trim(self):
        '''
        Input binary scheduling and output permutation scheduling list
        ref of permutation trimming: A Hybrid Quantum-Inspired Genetic Algorithm for Flow
        ref of random key: Genetic Algorithms and Random Keys for Sequencing and Optimization Shop Scheduling
        '''

        for i in range(self.PopSize):
            binary_schedule_str = "".join(str(binary)
                                          for binary in self.binary_solution[i])

            decimal_schedule = np.array([int(binary_schedule_str[i:i + self.Nbit], 2)
                                        for i in range(0, len(binary_schedule_str), self.Nbit)])
            argsort = np.argsort(decimal_schedule)
            trim_array = decimal_schedule
            k = 0
            for idx in argsort:
                trim_array[idx] = k
                k += 1
            self.ordering_schedules[i] = trim_array
        return

    def calculate_Task_index_schedules(self, tasks_size, ready_queue_idx):
        for i in range(self.PopSize):
            for Ti in range(tasks_size):
                core_idx = np.where(self.ordering_schedules[i] == Ti)[0][0]
                self.tasks_index_schedules[i, core_idx] = ready_queue_idx[Ti]

    def evaluate_population_fitness(self, TaskQueue, Cores, Ncore):
        schedules = self.tasks_index_schedules
        for i in range(self.PopSize):
            schedule = schedules[i]
            fitness = 0
            # 想法：一次就Random 這麼多var，讓Algorithm 自動收斂，取前三名
            for j in range(Ncore):
                fitness += Cores[j].evaluate_fitness(
                    TaskQueue.task_queue.get_tasks_info(schedule[j]))
            self.fitness[i] = fitness
        # End of evaluation of a classical population: get fittness

    def show_ClassicalPopulation(self):
        print(f"=============== Classical Population ===============")
        print(f"########## Binary solution ##########")
        for i in range(self.PopSize):
            print(f"sol_{i} | {self.binary_solution[i]}")
        print(f"########## Ordering Schedule ##########")
        for i in range(self.PopSize):
            print(f"sol_{i} | {self.ordering_schedules[i]}")
        print(f"########## Tasks Schedule ##########")
        for i in range(self.PopSize):
            print(f"sol_{i} | {self.tasks_index_schedules[i]}")
