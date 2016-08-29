import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-mc", action="store_true", help="Input is MC trajectories")
args = parser.parse_args()

density = 1
# Setting parameters for MC or MD
frames = 10
if args.mc == True:
    filename = "output.xyz"
    n = 10
    rho = 0.218
    L = n * np.sqrt(np.pi) * .5 / np.sqrt(rho)
else:
    print "hi"
    #filename = "lj.xyz"
    frames += 1
    L = 35
# Loading data
data = np.loadtxt(filename)
data = np.split(data, frames)

# Number of particles/molecules
N = len(data[0])

for frame in data:
    for i in xrange(N):
        dr = frame - frame[i]
        dr[dr > L] -= L
        dr[dr < L] += L
        sqdr = np.sum(np.square(dr), axis=1)
        dis = np.sqrt(sqdr)
        # Histogramming displacements
        bins = np.linspace(1,5,101)
        N_R, b = np.histogram(dis[dis != 0], bins=bins) 
        N_R /= (10* (N/2))
        size = (b[1:] - b[:-1])/2.
        ctr = (b[1:] + b[:-1])
        stuff = N_R/ (4 * np.pi *np.square(ctr) * size * density)
        plt.plot(ctr, stuff)
        plt.show()
