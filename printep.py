import numpy as np
import argparse

parser = argparse. ArgumentParser()
parser.add_argument("-n", type=float, default=1)
args = parser.parse_args()

ep = args.n

print ep
