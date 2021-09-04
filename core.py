import numpy as np
import copy

from numpy.lib.ufunclike import _dispatcher
from globalFunc import *
from beautifultable import beautifultable


class Core():
    def __init__(self) -> None:
        self.dispatcher = np.zeros([1, 5])
        self.STi = 0

    def append_task_to_dispatcher(self, task, FIRST_ASSIGNMENT=False):

        # Append the task in gbest schedule for certain core into it.
        task = task.reshape(1, 5)
        if FIRST_ASSIGNMENT:
            # self.dispatcher = np.concatenate((self.dispatcher, task))
            self.dispatcher = sort_task(
                np.concatenate((self.dispatcher, task)))
            STi = self.dispatcher[1][3]
        else:
            # pass
            task = task.reshape(1, 5)

            dispatcher = copy.deepcopy(self.dispatcher)
            dispatcher = np.concatenate((dispatcher, task))
            dispatcher = sort_task(dispatcher)
            # Set STi as first task of this core
            STi = dispatcher[1][3]
            self.dispatcher = np.zeros([1, 5])
            self.dispatcher = np.concatenate(
                (self.dispatcher, dispatcher[1].reshape(1, 5)))

            for i in range(2, len(dispatcher)):
                if(self.able_to_scheduled(dispatcher[i], STi)):
                    append_task = dispatcher[i].reshape(1, 5)
                    self.dispatcher = np.concatenate(
                        (self.dispatcher, append_task))
                    STi += dispatcher[i][3]
        self.dispatcher = sort_task(self.dispatcher)
        self.STi = STi

    def able_to_scheduled(self, task, STi) -> bool:
        # 一個Task加進來之後，dispatcher Sort後能否成功排入dispatcher 不違反Deadline
        # Yes: True, No: False
        FTi = STi + task[3]
        if (task[2] <= STi) and (STi <= (task[4] - task[3])) and ((task[2] + task[3]) <= FTi) and (FTi <= task[4]):
            return True
        else:
            print(f"Fail to schedule: task_{int(task[0])}")
            ######### Debug ##########
            # [[idx, Ai, Ri, Ci, Di]]
            print("Index: ", task[0])
            print("STi: ", STi)
            print("FTi: ", FTi)
            print("Ri: ", task[2])
            print("Ci: ", task[3])
            print("Di: ", task[4])
            # print()
            if task[2] > self.STi:
                print("Ri > STi")
            if self.STi > task[4] - task[3]:
                print("STi > Di - Ci")
            if task[2] + task[3] > FTi:
                print("Ri + Ci > FTi")
            if FTi > task[4]:
                print("FTi > Di")
            print()
            ######## Debug ##########
            return False

    def evaluate_fitness(self, task, NEW_TASKS=True) -> int:
        # 0. Deep copy the dispatcher
        # 1. Add the certain tasks
        # 2. Sort dispatcher according to EDF
        # 3. for each task in dispatcher: if meet Deadline -> fittness += 1
        # [idx, Ai, Ri, Ci, Di]
        # For "THIS" core
        if NEW_TASKS == True:
            task = task.reshape(1, 5)
            dispatcher = copy.deepcopy(self.dispatcher)
            dispatcher = np.concatenate((dispatcher, task))
            dispatcher = sort_task(dispatcher)
            STi = dispatcher[1][3]
            fitness = 1
            for i in range(2, len(dispatcher)):
                if(self.able_to_scheduled(dispatcher[i], STi)):
                    # Increment fitness
                    fitness += 1
                    #  fitness
                    STi += dispatcher[i][3]
                # else:
                    # print(f"Fail to schedule: task_{dispatcher[i][0]}")
        elif NEW_TASKS == False:
            dispatcher = copy.deepcopy(self.dispatcher)
            dispatcher = sort_task(dispatcher)
            STi = dispatcher[1][3]
            fitness = 1
            for i in range(2, len(dispatcher)):
                if(self.able_to_scheduled(dispatcher[i], STi)):
                    # Increment fitness
                    fitness += 1
                    #  fitness
                    STi += dispatcher[i][3]

        return fitness

    def show_core_info(self, index):
        core_table = BeautifulTable()
        core_table.rows.append(["index", "STi", "dispatcher"])
        core_table.rows.append([index, self.STi, self.dispatcher])
        print(core_table)
