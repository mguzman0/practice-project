import numpy as np
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=float, default=1)
args = parser.parse_args()



ep = args.n * 4184.0 #convert kcal/mol to J/mol
m = 0.5 / 1000.0 #convert g to kg
si = 3.0 * math.pow(10, -10) #convert A to m

freq = np.sqrt(ep / m) * np.power(2,float(1)/3) * 3 / (np.pi *si)
dts = 1/(freq * 10)
dt = dts * math.pow(10, 15) #convert s to fs

print dt
