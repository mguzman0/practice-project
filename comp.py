import numpy as np
import matplotlib.pyplot as plt

mc = np.loadtxt("a.txt")
md = np.loadtxt("b.txt")

bins = np.linspace(1,5, 1000)
ctr = (bins[1:] + bins[:-1])/2

plt.plot(ctr, mc, 'g', label="Monte Carlo")
plt.plot(ctr, md, 'r', label="MD")
plt.xlim(0,4)
plt.ylabel("g(r)", fontsize=15)
plt.xlabel(r'r [$\AA$]', fontsize=15)
plt.legend()
plt.show()
