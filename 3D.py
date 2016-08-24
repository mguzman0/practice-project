import numpy as np
import numpy.random as rand
import logging
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-vmd",action="store_true", help="Turn on VMD mode")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG)


rho = .5
n   = 5
L   = n * np.sqrt(np.pi) * .5 / np.sqrt(rho)
xf  = (1.0 - 1/n) * L
x0 = np.linspace(0, xf, n)
y0 = np.linspace(0, xf, n)
z0 = np.linspace(0, xf, n)
r0 = np.array(np.meshgrid(x0, y0, z0))
r_ir = np.reshape(r0, ( 3, n*n*n))
r_ir = r_ir.T


tf = 10
nsucess = 0
newr = []
msd_t = []
T = []

for t in range(tf * n * n):
    """if t % (n*n) == 0:
        if args.vmd:
            print "{}".format(n*n)
            print "t = {}".format(t)
            for i in xrange(n):
                for j in xrange(n):
                    print "C {}  {}  0.0".format(r_ir[i + n*j, 0], r_ir[i + n*j, 1])
        else:
            for i in xrange(n):
                for j in xrange(n):
                    print "{}  {}  0.0".format(r_ir[i + n*j, 0], r_ir[i + n*j, 1])"""
    disp = rand.uniform(-.5, .5, 3)
    i = rand.randint(n*n*n)
    trial = r_ir[i,:] + disp
    trial[trial > L] -= L
    trial[trial < 0] += L
    dr = np.abs(r_ir[:,:] - trial)
    dr[dr > L*.5] -= L
    trial_rsq_j =np.sum( np.square(dr), axis = 1)
    #print "trial_rsq: ", trial_rsq_j
    trial_rsq_j[i] = 100
    rejections = trial_rsq_j[trial_rsq_j < 1.0]
    #print "reject: ", rejections
    if len(rejections) == 0:
        r_ir[i,:] = trial

	nsucess += 1

logging.debug("{} of {} attempts".format(nsucess, tf * n * n * n))
