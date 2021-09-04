import numpy as np
import math
from beautifultable import BeautifulTable


class FitnessAgent():
    def __init__(self, PopSize, varSize) -> None:
        # Set Meta size data
        self.PopSize = PopSize
        self.varSize = varSize
        self.Nbit = math.ceil(math.log(self.varSize, 2))
        self.solSize = (self.Nbit * self.varSize)
        self.dim = 2
        # Set classical pBest, gBest
        self.pbest_fitness = np.zeros(self.PopSize)
        self.pbest_sol = np.zeros((self.PopSize, self.solSize))
        self.pbest_tasks_schedule = np.zeros((self.PopSize, self.varSize))
        self.gbest_fitness = 0
        self.gbest_sol = np.zeros(self.solSize)
        self.gbest_tasks_schedule = np.zeros(varSize)

    def best_update(self, ClassicalPop):
        for i in range(self.PopSize):
            # Update gbest
            if ClassicalPop.fitness[i] >= self.gbest_fitness:
                self.gbest_fitness = ClassicalPop.fitness[i]
                self.gbest_sol = ClassicalPop.binary_solution[i]
                self.gbest_tasks_schedule = ClassicalPop.tasks_index_schedules[i]
            # Update pbest
            if ClassicalPop.fitness[i] >= self.pbest_fitness[i]:
                self.pbest_fitness[i] = ClassicalPop.fitness[i]
                self.pbest_sol[i] = ClassicalPop.binary_solution[i]
                self.pbest_tasks_schedule[i] = ClassicalPop.tasks_index_schedules[i]

    def show_best(self):
        best_table = BeautifulTable()
        print("############ global best ############")
        print(f"gbest schedule | {self.gbest_tasks_schedule}")
        print(f"gbest fitness  | {self.gbest_fitness}")

        print("############ pbest ############")
        for i in range(self.PopSize):
            print(
                f"pbest_{i} schedule | {self.pbest_tasks_schedule[i]} | fitness: {self.pbest_fitness[i]}")
