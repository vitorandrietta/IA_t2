from mpl_toolkits import mplot3d
from core.kmeans.core import *

import numpy as np
import matplotlib.pyplot as plt

class PlotAlgoritmState:

	def plot(self, clusters):
		fig = plt.figure()
		ax = plt.axes(projection="3d")

		x_points = []
		y_points = []
		z_points = []

		for c in clusters:
			x_points.extend([ p.coordinates[0] for p in c.points])
			y_points.extend([ p.coordinates[1] for p in c.points])
			z_points.extend([ p.coordinates[2] for p in c.points])

		x_points = np.array(x_points)
		y_points = np.array(y_points)
		z_points = np.array(z_points)

		ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')
		plt.show()