from globals import *
import numpy as np
import math
import random


class AngleRecorder():
    def __init__(self) -> None:
        self.delta_theta = 0

    def lookup_theta(self, f_x, f_b, xi, bi, alpha, beta):
        cond = (f_x >= f_b)
        # if 𝑓(𝑥) > 𝑓(gbest): FALSE
        if cond == False:
            # print("𝑓(𝑥) <= 𝑓(gbest): 沒有比較好！！")
            if xi == 1 and bi == 0:
                # Define the rotation angle: delta_theta (e.g. -0.0785398163)
                theta = 0.01 * np.pi
                if (alpha * beta > 0):
                    self.delta_theta = -theta
                elif (alpha * beta < 0):
                    self.delta_theta = theta
                elif (alpha == 0):
                    sign = random.choice([-1, 1])
                    self.delta_theta = sign * theta
                else:
                    self.delta_theta = 0
            if xi == 1 and bi == 1:
                # Define the rotation angle: delta_theta (e.g. -0.0785398163)
                theta = 0.02 * np.pi
                if (alpha * beta > 0):
                    self.delta_theta = theta
                elif (alpha * beta < 0):
                    self.delta_theta = -theta
                elif (beta == 0):
                    sign = random.choice([-1, 1])
                    self.delta_theta = theta
                else:
                    self.delta_theta = 0
        elif cond == True:
            # print("𝑓(𝑥) > 𝑓(gbest): 有比較好！！")
            # if 𝑓(𝑥) > 𝑓(gbest): TRUE
            if xi == 0 and bi == 1:
                # Define the rotation angle: delta_theta (e.g. -0.0785398163)
                theta = 0.0025 * np.pi
                if (alpha * beta > 0):
                    self.delta_theta = -theta
                elif (alpha * beta < 0):
                    self.delta_theta = theta
                elif (alpha == 0):
                    sign = random.choice([-1, 1])
                    self.delta_theta = sign * theta
                else:
                    self.delta_theta = 0
            if xi == 1 and bi == 0:
                # Define the rotation angle: delta_theta (e.g. -0.0785398163)
                theta = 0.025 * np.pi
                if (alpha * beta > 0):
                    self.delta_theta = theta
                elif (alpha * beta < 0):
                    self.delta_theta = -theta
                elif (beta == 0):
                    sign = random.choice([-1, 1])
                    self.delta_theta = sign * theta
                else:
                    self.delta_theta = 0
            if xi == 1 and bi == 1:
                # Define the rotation angle: delta_theta (e.g. -0.0785398163)
                theta = 0.05 * np.pi
                if (alpha * beta > 0):
                    self.delta_theta = theta
                elif (alpha * beta < 0):
                    self.delta_theta = -theta
                elif (beta == 0):
                    sign = random.choice([-1, 1])
                    self.delta_theta = theta
                else:
                    self.delta_theta = 0
        return
    def GDAA_Linear(self, GEN):
        global GEN_MAX
        theta_max = 0.1 * np.pi
        theta_min = 0.0025 * np.pi
        self.delta = theta_max - (theta_max - theta_min)* (GEN/GEN_MAX)

    def GDAA_Exp(self, GEN):
        global GEN_MAX
        C = 10
        self.delta = C * math.exp(-GEN/GEN_MAX)
        # print("Theta: ", self.delta)

    def FVDAA(self, f_x, f_b):
        self.delta = np.pi * (1 - (f_b/f_x))
        pass
