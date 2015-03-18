import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Generate a file for clustering')
parser.add_argument('rows', help="number of rows", type=int)
parser.add_argument('cols', help="number of columns", type=int)
parser.add_argument('output', help="output file name")

args = parser.parse_args()

data = np.random.randint(1, 99, (args.rows, args.cols))
data = data / 10.0

np.savetxt(args.output, data, fmt='%.1f', delimiter=",")

