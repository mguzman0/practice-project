import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-mc", action="store_true", help="Analyze monte carlo data")
parser.add_argument("-n", type=str, default=1)
parser.add_argument("-save", help="Path to save images")

args = parser.parse_args()

#n = args.n
y = []
#fil = args.save + "/" + "lj" + n + ".xyz"
if args.mc == True:
    fil = "new.xyz"
else:
    fil = "lj.xyz"
with open(fil, 'r') as f:
#want to take 'n' number of lines and skip the first two lines in the
#begining of 'n' line
    for num, line in enumerate(f): 
        if line[1] == '0' or line[0] == "A":
            continue
        else:
            nline = map(np.float, line.split()) #converts into float
            y.append(nline)
data = np.split(np.array(y),1001) # second parameter is tf
L = 11.408
#fname = n + ".png"
#print data
#exit()
rsqt = [] #difference in position from one particle to the next
msd = [0]

for n in range(len(data)-1):
    n += 1
    for i in range(len(data)-n):
        dr = np.abs(data[i]-data[i+n])
        dr[dr >= L/2.0] -= L
        rsq = np.sum(np.square(dr), axis = 1)
        rsum = np.mean(rsq)
        rsqt.append(rsum)
    meanrsq = np.mean(rsqt)
    msd.append(meanrsq)
    rsqt = []

tau = np.arange(1001)
slope, intercept = np.polyfit(tau,msd,1)
D = slope/6.0

# Converting units: reduced to real 
l = 3.405e-10 	# sigma [meters]
m = 6.63e-26 	# mass/atom [kg]
ep = 3.32e-20 	# epsilon [J]
D = D * l/np.sqrt(m/ep)

print "diffusion coefficient: {} m^2/s".format( D)
plt.plot(tau,msd)
#plt.savefig(args.save + "/" + fname)
plt.clf()
plt.show()
