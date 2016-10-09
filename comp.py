import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
#import argarse

#parser = argparse.ArgumentParser()
#parse.add_argument("-n", type=str, default=none)

#args = parser.parse_args()

mc = np.loadtxt("a.txt")
md = np.loadtxt("b.txt")
ix_mcmax = np.argmax(mc)
ix_mdmax = np.argmax(md)

mc = mc[ix_mcmax : 200+ix_mcmax]
md = md[ix_mdmax : 200+ix_mdmax]
bins = np.linspace(1,5, 1000)
ctr = (bins[1:] + bins[:-1])/2



plt.plot(mc, 'g', label="Monte Carlo")
plt.plot(md, 'r', label="MD")
## plt.xlim(0,4)
plt.ylabel("g(r)", fontsize=15)
plt.xlabel(r'r [$\AA$]', fontsize=15)
plt.legend()
plt.show()
#plt.savefig("rdf" + args.n + ".png")
