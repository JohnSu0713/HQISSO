import globalFunc
from globals import *
import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)


class TaskQueue():
    def __init__(self, Ntasks) -> None:

        self.task_queue = np.zeros((Ntasks, 5))
        self.Ntasks = Ntasks
        self.unscheduled_tasks = None
        self.min_c = min_c
        self.max_c = max_c

    def init_tasks(self, Ncore):
        # task[0]: index
        self.task_queue[:, 0] = np.arange(1, self.Ntasks + 1)
        # task[1]: Ai
        self.task_queue[:, 1] = np.round(
            np.arange(0, self.Ntasks * 0.05, 0.05), 2)
        # task[2]: Ri
        for task in self.task_queue:
            task[2] = np.random.uniform(
                int(task[1]), int(task[1]) + Ri_param * Ncore)
        # task[3]: Ci
        self.task_queue[:, 3] = np.random.uniform(
            self.min_c, self.max_c, self.Ntasks)
        # task[4]: Di
        for task in self.task_queue:
            task[4] = np.random.uniform(
                task[2] + Di_lowerB * task[3], task[2] + Di_upperB * task[3])

        self.unscheduled_tasks = self.task_queue[:, 0]

    def get_tasks_info(self, idx):
        # TODO: get Tasks information
        target_queue = self.task_queue[np.isin(self.task_queue[:, 0], idx)]
        return target_queue

    def update_unscheduled_tasks(self, scheduled_tasks):
        self.unscheduled_tasks = self.unscheduled_tasks[~np.isin(
            self.unscheduled_tasks, scheduled_tasks)]


class ReadyQueue():
    def __init__(self) -> None:
        self.size = None
        self.ready_queue = None

    def set_task_spec(self):
        pass

    def get_arrived_tasks(self, TaskQueue, t):
        # 1. load the tasks from task_queue and sorted by EDF
        ready_queue = globalFunc.sort_task(
            TaskQueue.get_tasks_info(TaskQueue.unscheduled_tasks))
        # 2. return the tasks only Ai <= t: This function return a "Tasks list"
        ready_queue = ready_queue[ready_queue[:, 1] <= t]
        self.ready_queue = ready_queue
        self.size = ready_queue.shape[0]
        return ready_queue

    def get_index(self):
        return self.ready_queue[:, 0].astype(int)

    def pop_tasks(self, size, TaskQueue):
        TaskQueue.update_unscheduled_tasks(self.get_index()[:size])
        self.ready_queue = self.ready_queue[size:]
        self.size = self.ready_queue.shape[0]