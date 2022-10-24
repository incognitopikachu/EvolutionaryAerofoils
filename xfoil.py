import os
import subprocess
import numpy as np


def run_xfoil(airfoil_name):
    """
    todo
    """

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
