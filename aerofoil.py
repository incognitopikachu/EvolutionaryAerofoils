from dataclasses import dataclass
from xfoil import run_xfoil
import numpy as np
import os
import random
from airfoils import fileio
import matplotlib.pyplot as plt


@dataclass
class Aerofoil:
    """
    Class encapsulating an aerofoil. Stores coordinates and methods to alter them.
    """
    name: str
    airfoil: np.ndarray
    polar_array: np.asanyarray = None
    optimum_array: np.asanyarray = None

    def __init__(self, name, upper, lower):
        self.name = name
        self.upper = upper
        self.lower = lower

    def __repr__(self):
        return self.name

    def to_dat_file(self):
        all = np.concatenate((self.upper.T, self.lower.T))  # todo remove duplicated point
        path = os.path.join("xfoil_temp", self.name + ".dat")
        if os.path.exists(path):
            os.remove(path)
        np.savetxt(path, all, delimiter="   ", header="test", fmt='%f')

    def mutate(self):
        for _ in range(1):
            self.mutate_surface_point(self.upper)
            self.mutate_surface_point(self.lower)

    @staticmethod
    def mutate_surface_point(surface):
        mutate_i = random.randint(2, max(surface.shape) - 3)
        mutation = 0.0001 * random.randint(-1, 1)
        surface[1][mutate_i] = surface[1][mutate_i] + mutation
        surface[1][mutate_i - 1] = surface[1][mutate_i - 1] + 0.5 * mutation
        surface[1][mutate_i + 1] = surface[1][mutate_i + 1] + 0.5 * mutation
        surface[1][mutate_i - 2] = surface[1][mutate_i - 2] + 0.25 * mutation
        surface[1][mutate_i + 2] = surface[1][mutate_i + 2] + 0.25 * mutation

    def plot(self):
        plt.plot(self.upper[0], self.upper[1], 'x')
        plt.plot(self.lower[0], self.lower[1], 'x')
        plt.show()

    def run(self):
        self.to_dat_file()
        self.polar_array = run_xfoil(self.name)

    def get_max_lift_to_drag_ratio(self):
        # columns are: alpha,CL,CD,CDp,CM,Top_Xtr,Bot_Xtr
        try:
            LD = self.polar_array[:, 1] / self.polar_array[:, 2]
            LDmax = max(LD)
            return LDmax
        except Exception as e: # todo show catch when running xfoil not here
            print(e)
            print(self.polar_array)
            return 0



if __name__ == "__main__":
    name = "ag24"
    path = os.path.join("aerofoil_data", name + ".dat")
    tup = fileio.import_airfoil_data(path)
    upper = tup[0]
    lower = tup[1]
    airfoil = Aerofoil(name, upper, lower)
    airfoil.plot()
    for i in range(10):
        airfoil.mutate()
    airfoil.plot()


