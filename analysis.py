import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=str, default=1)
parser.add_argument("-save", help="Path to save images")

args = parser.parse_args()

y = []
with open('lj.xyz', 'r') as f:
#want to take 'n' number of lines and skip the first two lines in the
#begining of 'n' line
    for num, line in enumerate(f): 
        if line[1] == '0' or line[0] == "A":
            continue
        else:
            nline = map(np.float, line.split()) #converts into float
            y.append(nline)
data = np.split(np.array(y),1001) # second parameter is tf
L = 35
n = args.n
fname = n + ".png"
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
print  slope/4.0
plt.plot(tau,msd)
plt.savefig(args.save + "/" + fname)
plt.clf()

