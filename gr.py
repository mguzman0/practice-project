#import matplotlib
#matplotlib.use('Agg')
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-mc", action="store_true", help="Input is MC trajectories")
parser.add_argument("-f", type=int, default = 0)
parser.add_argument("-n", type=int, default = 1)

args = parser.parse_args()

# Setting parameters for MC or MD
if args.mc == True:
    # Monte Carlo
    filename = "traj.xyz"
    with open(filename, 'r') as tL:
        first_line = tL.readline()
    data = np.loadtxt(filename, skiprows=1)
    #n = 10
    #rho = 0.34
    #L = n*(.5)*(((4./3.)*(np.pi/rho))**(1./3.))
    L = first_line
    L = float(L)
    name = "mc_rdf.png"

else:
    # Molecular Dynamics
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
    L = 11.4
    name = "md_rdf.png"
# Loading data
frames = args.f
data = np.split(data, frames)

# Number of particles/molecules
N = len(data[0])
density = N/(L**3)

bins = np.linspace(1,6,frames)
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
#for i in gr:
#print i

plt.xlim([0, max(ctr)])
plt.ylabel("g(r)")
plt.xlabel("r")
#plt.show()
plt.savefig(name)
