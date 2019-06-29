from core.kmeans.core import BaseProblemSolver, EuclidianDistanceProblemSolver, Point, Runner
from sys import float_info

"""
Default solver which uses euclidian distance to create the clusters
"""


class DefaultSolver(EuclidianDistanceProblemSolver):
    def __init__(self):
        self
        self.__super__()

    def calculate_new_center(self, cluster):
        rep_dim = len(self.img_points[0].coordinates)
        points_val = [0.0] * rep_dim
        for p in self.img_points:
            for i in range(rep_dim):
                points_val[i] += p.coordinates[i]
            coordinates = [(v / self.img_dim) for v in points_val]
            return Point(coordinates)

    def assign_points(self, cluster, points):
        clusters = [[] for _ in range(self.n_cluster)]
        for p in self.img_points:
            smallest_distance = float_info.max
            for i in range(self.n_cluster):
                distance = self.distance(p, cluster.clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    choosen_cluster = i
            clusters.cluster_list[i].append(p)
        return clusters

    def is_fit_enough(self):
        pass


class DefaultRunner(Runner):
    def __init__(self):
        self.__super__()