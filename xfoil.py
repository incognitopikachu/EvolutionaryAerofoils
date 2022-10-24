import os
import subprocess
import numpy as np
# from aerofoil import Aerofoil
from post_process import get_max_lift_to_drag_ratio


def run_xfoil(airfoil_name):

    # inputs
    alpha_i = 0
    alpha_f = 15
    alpha_step = 0.25
    Re = 1000000
    n_iter = 500

    # clear output file
    if os.path.exists("xfoil_temp\\polar_file.txt"):
        os.remove("xfoil_temp\\polar_file.txt")

    if os.path.exists("input_file.in"):
        os.remove("input_file.in")

    # make input file
    input_file = open("input_file.in", 'w')
    # input_file.write("LOAD aerofoil_data\\{0}.dat\n".format(airfoil_name))
    input_file.write("LOAD xfoil_temp\\{0}.dat\n".format(airfoil_name))
    input_file.write(airfoil_name + '\n')
    input_file.write("PANE\n")
    input_file.write("OPER\n")
    input_file.write("Visc {0}\n".format(Re))
    input_file.write("PACC\n")
    input_file.write("xfoil_temp\\polar_file.txt\n\n")
    input_file.write("ITER {0}\n".format(n_iter))
    input_file.write("ASeq {0} {1} {2}\n".format(alpha_i, alpha_f,
                                                 alpha_step))
    input_file.write("\n\n")
    input_file.write("quit\n")
    input_file.close()

    subprocess.call("xfoil.exe < input_file.in > out.txt", shell=True)

    return np.loadtxt("xfoil_temp\\polar_file.txt", skiprows=12)

# def run_xfoil_aerofoil(aerofoil):
#     # inputs
#     alpha_i = 0
#     alpha_f = 20
#     alpha_step = 0.25
#     Re = 1000000
#     n_iter = 100
#
#     directory = "xfoil_temp"
#     polar_path = os.path.join(directory, "polar_file.txt")
#     dat_path = os.path.join(directory, aerofoil.name + ".dat")
#
#     # clear dir
#     if os.path.exists(polar_path):
#         os.remove(polar_path)
#     if os.path.exists(dat_path):
#         # todo could clear all dat files
#         os.remove(dat_path)
#
#     # make dat file
#     aerofoil.write_dat_file(directory)



# if __name__ == '__main__':
#     # airfoil = "NACA0009"
#     # data = run_xfoil(airfoil)
#     # get_max_lift_to_drag_ratio(data)
#     # print(get_max_lift_to_drag_ratio(data))
#
#     # aerofoils = []
#     #
#     # with os.scandir(os.getcwd()) as it:
#     #     for file in it:
#     #         if file.name.endswith(".dat"):
#     #             # aerofoils.append(Aerofoil(filename[:-4], read_dat_file(file.path)))
#     #             aerofoils.append(Aerofoil.make_aerofoil_from_dat_file(file))
#     #
#     # print("a")
#
#
