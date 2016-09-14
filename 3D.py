import numpy as np
import numpy.random as rand
import logging
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-vmd",action="store_true", help="Turn on VMD mode")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG)
sigma = 2.8
dim = 3
rho = .05
n   = 5
L   = (n+1)*sigma
#n*(3.92)*((4./3.)*np.pi/rho)**(1/3.)
#(n + 1)*sigma
#n * np.sqrt(np.pi) * .5 / np.sqrt(rho)
xf  = (1.0 - 1/n) * L
x0 = np.linspace(0, xf, n, endpoint=False)
y0 = np.linspace(0, xf, n, endpoint=False)
z0 = np.linspace(0, xf, n, endpoint=False)
r0 = np.array(np.meshgrid(x0, y0, z0))
r_ir = np.reshape(r0, ( dim, (n**dim)))
r_ir = r_ir.T


tf = 1000
tprint = 100
nsucess = 0
newr = []
msd_t = []
T = []

for t in range(tf * (n**dim) + 1):
    if t % (tprint * (n**dim)) == 0 and t !=0:
        if args.vmd:
            print "{}".format(n**dim)
            print "t = {}".format(t)
            for i in xrange(n**dim):
                print "1 {} {} {}".format(r_ir[i,0], r_ir[i,1], r_ir[i,2])
           
        else:
            for i in xrange(n**dim):
                print "{}  {}  {}".format(r_ir[i, 0], r_ir[i, 1], r_ir[i, 2])
        if t == tf * (n**dim) + 1:
            continue
    disp = rand.uniform(-.5, .5, dim)
    i = rand.randint(n*n*n)
    trial = r_ir[i,:] + disp
    trial[trial > L] -= L
    trial[trial < 0] += L
    dr = np.abs(r_ir[:,:] - trial[np.newaxis, :])
    dr[dr > L*.5] -= L
    trial_rsq_j =np.sum( np.square(dr), axis = 1)
    trial_rsq_j[i] = 100
    rejections = trial_rsq_j[trial_rsq_j < np.square(sigma)]
    if len(rejections) == 0:
        r_ir[i,:] = trial

	nsucess += 1

logging.debug("{} of {} attempts".format(nsucess, tf * (n**dim)))
