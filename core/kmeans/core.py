from sys import float_info
from PIL import Image
from numpy import linalg
from random import sample
from ..helper import util


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:
    def __init__(self, center, points):
        self.center = center
        self.points = points


class BaseProblemSolver:

    def __init__(self, img_path, n_cluster, min_diff):
        self.n_cluster = n_cluster
        self.img_path = img_path
        self.img_points = self._get_image_data()
        self.clusters = [Cluster(center=p, points=[p]) for p in sample(self.img_points, self.n_clusters)]
        self.min_diff = min_diff


    def distance(self, p, q):
        pass

    def calculate_new_center(self, cluster):
        pass

    def formulate_new_clt_points(self):
        pass

    def single_fit_calculation(self):
        gen_clusters = self.formulate_new_clt_points()

        for i in range(self.n_cluster):
            if gen_clusters[i]:
                previous = self.clusters[i]
                center = self.calculate_new_center(gen_clusters[i])
                new = Cluster(center, gen_clusters[i])
                self.clusters[i] = new

                if self.is_fit_enough(previous, new):
                    break

    def is_fit_enough(self, previous, new):
        return self.distance(previous.center, new.center) < self.min_diff

    def _get_image_data(self):
        img = Image.open(self.img_path)
        img = img.convert("RGB")
        width, height = img.size
        self.img_dim = width * height
        image_points = []
        for count, color in img.getcolors(self.img_dim):
            image_points += count * [color]
        return image_points
        # TODO IMPLEMENTAR AQUI, NAO DEVE MUDAR

    def get_colors(self):
        pass


class EuclidianDistanceProblemSolver(BaseProblemSolver):
    def distance(self, p, q):
        return sum(linalg(p.coordinates[i] - q.coordinates[i]) for i in range(self.img_dim))

    def __init__(self, ncluster, img_path, mindif):
        super().__init__(ncluster, img_path, mindif)


########## AI PRA FAZER AS COISAS VISUAIS, MUDAR OUTRO ARQUIVO #######

class DefaultSolver(EuclidianDistanceProblemSolver):
    def __init__(self, ncluster, img_path, mindif):
        super().__init__(ncluster, img_path, mindif)

    def calculate_new_center(self, cluster):
        rep_dim = len(self.img_points[0].coordinates)
        points_val = [0.0] * rep_dim
        for p in self.img_points:
            for i in range(rep_dim):
                points_val[i] += p.coordinates[i]

        coordinates = [(v / self.img_dim) for v in points_val]
        return Point(coordinates)

    def formulate_new_clt_points(self):
        new_clusters = [[] for _ in range(self.n_cluster)]
        for point in self.img_points:
            distances = [self.distance(point, c.center) for c in self.clusters[i]]
            (_, min_dist_index) = distances.index(min(distances))
            new_clusters[min_dist_index] = point

        return new_clusters

    def is_fit_enough(self):
        pass


class Runner:
    def __init__(self, ncluster, img_path, mindif):
        self.problem_solver = EuclidianDistanceProblemSolver(ncluster, img_path, mindif)

    def run(self):
        while not self.problem_solver.is_fit_enough():
            self.problem_solver.single_fit_calculation()
        self.problem_solver.clusters.sort(key=lambda c: len(c.points), reverse=True)
        rgbs = [map(int, c.center.coordinates) for c in self.problem_solver.clusters]
        return list(map(util.rgb_to_hex, rgbs))
