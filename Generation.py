from aerofoil import Aerofoil
from airfoils import Airfoil, fileio
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from xfoil import run_xfoil
import os


class Generation:
    """"
    Class encapsulating a generation of aerofoils and methods to manipulate and create proceeding generations
    """

    def __init__(self, aerofoils):
        self.aerofoils = aerofoils

    @staticmethod
    def make_first_generation(aerofoils_folder):
        aerofoils = []
        with os.scandir("aerofoil_data") as it:
            for file in it:
                if file.name.endswith(".dat") and file.name.startswith("naca00"):
                    tup = fileio.import_airfoil_data(file.path)
                    upper = tup[0]
                    lower = tup[1]
                    aerofoils.append(Aerofoil(file.name.split(".")[0], upper, lower))
                else:
                    continue
        return Generation(aerofoils)

    def select(self):
        self.aerofoils.sort(key=lambda x: x.get_max_lift_to_drag_ratio(), reverse=True)
        next_gen = deepcopy(self.aerofoils[0:5])
        for aerofoil in next_gen:
            aerofoil.polar_array = None  # todo make constructor for this
            aerofoil.mutate()
        return Generation(next_gen)

    def run(self):
        for aerofoil in self.aerofoils:
            aerofoil.run()


if __name__ == "__main__":

    generations = []
    g1 = Generation.make_first_generation("aerofoil_data")
    generations.append(g1)

    for i in range(10):
        g = generations[-1]
        g.run()
        print("gen: " + str(i) + "\n")
        for aerofoil in g.aerofoils:
            print(aerofoil.get_max_lift_to_drag_ratio())
        print("\n")
        generations.append(g.select())

    # g2 = g1.select()
    # g2.run()
    # print("g1: \n")
    # for aerofoil in g1.aerofoils:
    #     print(aerofoil.get_max_lift_to_drag_ratio())
    #
    # print("g2: \n")
    # for aerofoil in g2.aerofoils:
    #     print(aerofoil.get_max_lift_to_drag_ratio())

    # # run_xfoil("test")
    # name = "ag24"
    # path = os.path.join("aerofoil_data", name + ".dat")
    # tup = fileio.import_airfoil_data(path)
    # upper = tup[0]
    # lower = tup[1]
    # airfoil = Airfoil(upper, lower)
    #
    # # all = np.concatenate([upper[0], lower[0]], [upper[1], lower[1]])
    # all = np.concatenate((upper.T, lower.T))
    # path = os.path.join("aerofoil_data", "test.dat")
    # if os.path.exists(path):
    #     os.remove(path)
    # np.savetxt(path, all, delimiter="   ", header="test", fmt='%f')
    #
    # a = Aerofoil("testA", airfoil)
    # # airfoil.plot()
    # np.set_printoptions(suppress=True)
    # x = np.concatenate([np.flip(airfoil._x_upper), airfoil._x_lower])
    #
    # y = np.concatenate([np.flip(airfoil._y_upper), airfoil._y_lower])
    #
    # deleted_i = []
    # for i in range(len(x)):
    #     if x[i] > 1.0:
    #         x[i] = 1.0
    #     if i != 0 and abs(x[i] - x[i - 1]) < 0.001:
    #         deleted_i.append(i)
    # x = np.delete(x, deleted_i)
    # y = np.delete(y, deleted_i)
    #
    # combined = np.vstack((x, y)).T  # todo may need to prevent x-coord > 1
    # path = os.path.join("aerofoil_data", "test.dat")
    # if os.path.exists(path):
    #     os.remove(path)
    # np.savetxt(path, combined, delimiter="   ", header="test", fmt='%f')
    #
    # run_xfoil(name)
    # run_xfoil("test")
    #
    # plt.plot(x, y)
    # plt.plot(lower[0], lower[1])
    # plt.plot(upper[0], upper[1])
    # # plt.plot(upper)
    # plt.show()
    #
    # # airfoil.plot()
