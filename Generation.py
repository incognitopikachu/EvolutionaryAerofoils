from aerofoil import Aerofoil
from airfoils import Airfoil, fileio
from copy import deepcopy
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
        with os.scandir(aerofoils_folder) as it:
            for file in it:
                if file.name.endswith(".dat") and file.name.startswith("z"):
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


