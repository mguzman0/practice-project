#Plots Diffusion Coefficient vs Chosen Parameter (temp or ep)

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-temp", action="store_true", help="use -temp to plot temp as x")

args = parser.parse_args()

#Choosing x, y -axis variables

if args.temp:
    fT = np.loadtxt('temp_temp.txt')
    x = fT[:,[0]]
    x = x.ravel()
    x_axis = 'Temperature'
    y = np.loadtxt('coefficients_temp.txt')
    fname = "diff_temp" + ".png"
else:
    x = np.loadtxt('epsilon.txt')
    x_axis = 'Epsilon (kcal/mol)'
    y = np.loadtxt('coefficients_ep.txt') 
    fname = "diff_ep" + ".png"
#Plot
plt.plot(x, y,'yo')
plt.xlabel(x_axis)
plt.ylabel('Diffusion Coefficient ($Angstroms^2/fs')
plt.savefig(fname)
plt.show()
plt.clf
