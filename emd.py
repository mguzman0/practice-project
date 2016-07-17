#Calculates average total energy and plots it
#Used for debugging to find optimal time step

import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-temp", action="store_true", help="use -temp to analyze temp data")
args = parser.parse_args()

if args.temp:
    data_file = "ljtemp.txt"
    y_axis = "Temperature"
else:
    data_file = "energy.txt"
    y_axis = "Total Energy"

with open(data_file) as f:
    lines = (line for line in f if not line.startswith('#'))
    data = np.loadtxt(lines)
#d = list(data)
avg = np.mean(data)
std = np.std(data)

print "mean: {} std: {}".format(avg, std)

ystart = avg - 100
ystop = avg + 100

plt.plot(data)
plt.xlabel('Step')
plt.ylabel(y_axis)
plt.axis([0, len(data), ystart, ystop])
plt.show()

