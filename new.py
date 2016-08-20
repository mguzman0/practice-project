import numpy as np
import matplotlib.pyplot as plt
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-n", type=str, default=1)
#parser.add_argument("-save", help="Path to save images")

#args = parser.parse_args()

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
data = np.array(y) # second parameter is tf
L = 35
#n = args.n
#fname = n + ".png"
#print data[-1,:]
#exit()
rsqt = [0] #difference in position from one particle to the next
msd = [0]

for i in range(1,1001):
    print i
    dt = 100 * i
    dr = np.abs(data[dt:,:]-data[:-dt,:])
    dr[dr >= L/2.0] -= L
    rsq = np.sum(np.square(dr), axis = 1)
    rsum = np.mean(rsq)
    #rsqt.append(rsum)
    #meanrsq = np.mean(rsqt)
    #msd.append(meanrsq)
    #rsqt = []
print rsum 
exit()
tau = np.arange(1001)
#print len(tau)
#print len(rsqt)
#exit()

slope, intercept = np.polyfit(tau,rsqt,1)
print  slope/4.0
#plt.plot(tau,msd)
#plt.savefig(args.save + "/" + fname)
#plt.clf()

