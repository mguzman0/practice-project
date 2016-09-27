#import matplotlib
#matplotlib.use('Agg')
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-mc", action="store_true", help="Input is MC trajectories")
parser.add_argument("-f", type=int, default = 0)
args = parser.parse_args()

# Setting parameters for MC or MD
frames = args.f
if args.mc == True:
    filename = "output.xyz"
    data = np.loadtxt(filename)
    n = 5
    sigma = 2.8
    rho = 0.5
    L = (n+1)*sigma
#n*(3.92)*(((4./3.)*(np.pi/rho))**(1/3.))
#n * np.sqrt(np.pi) * .5 / np.sqrt(rho)
else:
    fil = "lj.xyz"
    y =[]
    with open(fil, 'r') as f:
        for num, line in enumerate(f):
            if line[1] == '0' or line[0]  == 'A':
                continue
            else:
                nline = map(np.float, line.split())
                y.append(nline)
    data = np.array(y,  dtype=np.float)
    L = 40
    L += 0.0
# Loading data
data = np.split(data, frames)

# Number of particles/molecules
N = len(data[0])
density = N/(L**3)

bins = np.linspace(1,20,1001)
size = (bins[1:] - bins[:-1])
ctr = (bins[1:] + bins[:-1])/2.

N_ic = np.zeros(len(bins) - 1, dtype=np.float)
for frame in data:
 
    for i in xrange(N):
        dr = frame[:,:] - frame[i,:]
        dr = np.abs(dr)
        dr[dr > L/2.] -= L
        sqdr = np.sum(np.square(dr), axis=1)
        dis = np.sqrt(sqdr)

        # Histogramming distances
        N_i, bins = np.histogram(dis[dis != 0.], bins=bins)
        N_ic = N_ic + N_i

# Averaging
N_ic = N_ic.astype(np.float)
N_ic = N_ic / (frames*(N))

gr = N_ic / (4 * np.pi *np.square(ctr) * size * density) 

plt.plot(ctr, gr)
plt.xlim([0, max(ctr)])
#plt.ylim([0, 5])
plt.ylabel("g(r)")
plt.xlabel("r")
#plt.show()
plt.savefig("rdf.png")
