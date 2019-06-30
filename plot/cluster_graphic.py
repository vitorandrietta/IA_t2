from mpl_toolkits import mplot3d
from core.kmeans.core import *

import numpy as np
import matplotlib.pyplot as plt

def rgb_to_hex(rgb):
	return '#%s' % ''.join(('%02x' % p for p in rgb))

class PlotAlgoritmState:

	def plot(self, clusters):
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')

		for c in clusters:
			for p in c.points:
				(x, y, z) = p.coordinates
				ax.scatter(x, y, z, color=rgb_to_hex(map(int, c.center.coordinates)))
		plt.show()