#Calculates average total energy and plots it
#Used for debugging to find optimal time step

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-temp", action="store_true", help="use -temp to analyze temp data")
parser.add_argument("-n", type=str, default=1)
#parser.add_argument("-save", help="Path to save images")

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

#print "mean: {} std: {}".format(avg, std)
#print avg, std

ystart = avg - 30.0
ystop = avg + 30.0
n = str(args.n)
fname = "derp" + n + ".png"
plt.plot(data)
plt.xlabel('Step')
plt.ylabel(y_axis)
plt.axis([0, len(data), ystart, ystop])
#plt.savefig(args.save + "/" + fname)
#plt.clf()
plt.show()
