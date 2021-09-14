from theta import AngleRecorder

import numpy as np
import math
from globals import *
from best import FitnessAgent
np.set_printoptions(precision=2)
# ChromeSize 應該要是min(Ncore, size_of_ready_queue)
# ChromeSize = 10 processors
# m <= 10
# Ncore = 10, size_of_ready_queue = 5
# ChromeSize = 5
# 如果有16 個Core/ Tasks : 需要 4個bits表示
# SolSize = Nbit * varSize -> 16 個Core/Tasks : 需要 4個bits表示
# 則一條Solution: 4 * 16 = 64 bits


class QuantumPop():
    def __init__(self, PopSize=PopSize, varSize=Ncore):
        # Meta Information
        self.PopSize = PopSize
        self.varSize = varSize
        self.Nbit = math.ceil(math.log(self.varSize, 2))
        self.solSize = (self.Nbit * self.varSize)
        self.dim = 2
        # Init Qgbest and Qpbest(qpv)
        self.Qgbest = np.zeros([self.solSize, self.dim])
        self.Qgbest_sqr = np.zeros([self.solSize, self.dim])
        self.qpv = np.zeros([self.PopSize, self.solSize, self.dim])
        self.qpv_sqr = np.zeros(
            [self.PopSize, self.solSize, self.dim])
        self.QuBitZero = np.array([[1], [0]])
        self.QuBitOne = np.array([[0], [1]])
        self.AlphaBeta = np.zeros([self.dim])

    def init_quantumPop(self):
        # Hadamard gate
        r2 = math.sqrt(2.0)
        h = np.array([[1/r2, 1/r2], [1/r2, -1/r2]])

        # Rotation Q-gate
        rot = np.empty([2, 2])

        # Initialize Qgbest
        for j in range(self.solSize):
            self.Qgbest[j, 0] = np.sin(np.radians(45))
            self.Qgbest[j, 1] = np.sin(np.radians(45))
            self.Qgbest_sqr[j, 0] = np.around(pow(self.Qgbest[j, 0], 2), 2)
            self.Qgbest_sqr[j, 1] = np.around(pow(self.Qgbest[j, 1], 2), 2)

        # Initialize Qpbest
        for i in range(self.PopSize):
            for j in range(self.solSize):

                # Quantum state alpha_beta
                self.qpv[i, j, 0] = np.sin(np.radians(45))
                self.qpv[i, j, 1] = np.sin(np.radians(45))

                # alpha squared
                self.qpv_sqr[i, j, 0] = np.around(pow(self.qpv[i, j, 0], 2), 2)
                # beta squared
                self.qpv_sqr[i, j, 1] = np.around(pow(self.qpv[i, j, 1], 2), 2)

    def get_rot_matrix(self, delta_theta):
        rot = np.empty([2, 2])
        # print("Delta_theta: ", delta_theta)
        rot[0, 0] = np.cos(delta_theta)
        rot[0, 1] = -np.sin(delta_theta)
        rot[1, 0] = np.sin(delta_theta)
        rot[1, 1] = np.cos(delta_theta)
        # print("Rot: \n", rot)
        return rot

    def rotate(self, cpv, FitnessAgent):
        # Lookup table of the rotation angle
        for i in range(self.PopSize):
            for j in range(self.solSize):
                # print(f"Update Q global by sol_{i}, bit_{j}")
                ###################### Rotate Qgbest ######################
                g_alpha = self.Qgbest[j, 0]
                g_beta = self.Qgbest[j, 1]

                angle_recorder_global = AngleRecorder()
                angle_recorder_global.lookup_theta(
                    cpv.fitness[i], FitnessAgent.gbest_fitness, cpv.binary_solution[i, j], FitnessAgent.gbest_sol[j], g_alpha, g_beta)
                delta_theta = angle_recorder_global.delta_theta
                rot = self.get_rot_matrix(delta_theta)
                next_Qgbest_alpha = (
                    rot[0, 0]*self.Qgbest[j, 0]) + (rot[0, 1]*self.Qgbest[j, 1])
                next_Qgbest_beta = (
                    rot[1, 0]*self.Qgbest[j, 0]) + (rot[1, 1]*self.Qgbest[j, 1])

                self.Qgbest[j, 0] = next_Qgbest_alpha
                self.Qgbest[j, 1] = next_Qgbest_beta

                # update alpha, beta squared
                self.Qgbest_sqr[j, 0] = np.round(pow(self.Qgbest[j, 0], 2), 3)
                self.Qgbest_sqr[j, 1] = np.round(pow(self.Qgbest[j, 1], 2), 3)
                ###################### Rotate Qpbest ######################
                # Lookup table of the rotation angle
        for i in range(self.PopSize):
            for j in range(self.solSize):
                p_alpha = self.qpv[i, j, 0]
                p_beta = self.qpv[i, j, 1]
                angle_recorder_p = AngleRecorder()
                angle_recorder_p.lookup_theta(
                    cpv.fitness[i], FitnessAgent.pbest_fitness[i], cpv.binary_solution[i, j], FitnessAgent.pbest_sol[i, j], p_alpha, p_beta)
                delta_theta = angle_recorder_p.delta_theta
                rot = self.get_rot_matrix(delta_theta)
                next_qpv_alpha = (
                    rot[0, 0]*self.qpv[i, j, 0]) + (rot[0, 1]*self.qpv[i, j, 1])
                next_qpv_beta = (
                    rot[1, 0]*self.qpv[i, j, 0]) + (rot[1, 1]*self.qpv[i, j, 1])
                self.qpv[i, j, 0] = next_qpv_alpha
                self.qpv[i, j, 1] = next_qpv_beta
                # update alpha, beta squared
                self.qpv_sqr[i, j, 0] = np.round(pow(self.qpv[i, j, 0], 2), 3)
                self.qpv_sqr[i, j, 1] = np.round(pow(self.qpv[i, j, 1], 2), 3)
                # print()

    def show_Qpopulation(self):
        print(f"========== Quantum Population ==========")
        # print(f"########## Quantum Gbest ##########")
        # for j in range(self.solSize):
        #     print(np.round(self.Qgbest[j, 0], 3), end="")
        #     print("||", end="")
        # print()
        # for j in range(self.solSize):
        #     print(self.Qgbest[j, 1], end="")
        #     print("||", end="")
        # print()
        print(f"########## Quantum Gbest Sqr ##########")
        for j in range(self.solSize):
            print(self.Qgbest_sqr[j, 0], end="")
            print("||", end="")
        print()
        for j in range(self.solSize):
            print(self.Qgbest_sqr[j, 1], end="")
            print("||", end="")
        print()

        print(f"########## Quantum Pbest ##########")
        for i in range(self.PopSize):
            # print(f"\n\nqpv {i} :")
            # print()
            # for j in range(self.solSize):
            #     print(np.round(self.qpv[i, j, 0], 3), end="")
            #     print("||", end="")
            # print()
            # for j in range(self.solSize):
            #     print(np.round(self.qpv[i, j, 1], 3), end="")
            #     print("||", end="")
            # print()
            print(f"\nqpv_sqr {i} :")
            print()
            for j in range(self.solSize):
                print(self.qpv_sqr[i, j, 0], end="")
                print("||", end="")
            print()
            for j in range(self.solSize):
                print(self.qpv_sqr[i, j, 1], end="")
                print("||", end="")
        print()
