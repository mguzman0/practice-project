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
else:
    x = np.loadtxt('epsilon.txt')
    x_axis = 'Epsilon'
    y = np.loadtxt('coefficients_ep.txt') 

#Plot
    
m, b = np.polyfit(x, y, 1)
plot(x, y, 'yo', x, m*x+b, '--k')
plt.xlabel(x_axis)
plt.ylabel('Diffusion Coefficient')
plt.show()
plt.clf
