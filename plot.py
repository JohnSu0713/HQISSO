
import random
from matplotlib import cm
import matplotlib.pyplot as plt


class PlotTool():
    def __init__(self, Ncore):
        self.fig, self.gnt = plt.subplots(figsize=(20,8))
        # Set x, y axis limitation
        self.gnt.set_ylim(0, 10)
        self.gnt.set_xlim(0, 600)
        self.Ncore = Ncore

        self.gnt.set_xlabel('Time')
        self.gnt.set_ylabel('Processor')

        # Setting graph attribute
        self.gnt.grid(True)
        self.cmap = self.get_cmap()

    def get_cmap(self, cmap_name = "prism", n=60):
        return plt.cm.get_cmap(cmap_name, n)

    def plot_gantt(self, Cores):
        # Setting ticks on y-axis
        self.gnt.set_yticks(range(0, self.Ncore + 2, 1))
        # Labelling tickes of y-axis
        
        labels = [f"CPU_{str(i)}" for i in range(self.Ncore)]
        labels.insert(0, "-")
        labels.append("-")
        # self.gnt.set_yticklabels([f"CPU_{str(i)}" for i in range(self.Ncore + 1)])
        self.gnt.set_yticklabels(labels)
        icmap = 1
        for i in range(len(Cores)):
            STi = 0
            for task in Cores[i].dispatcher:
                Ci = task[3]
                if task[0] == 0:
                    continue
                self.gnt.broken_barh([(STi, Ci)], ((i + 1)-0.25, 0.5), facecolor=self.cmap(icmap))
                self.gnt.text(STi+5, (i + 1)-0.05, f"T_{str(int(task[0]))}", color = "black", fontsize=6)
                STi += Ci
                icmap += 1
                if icmap == 50:
                    icmap = 1
        plt.show()
        print("Debug!!!!")
        return
