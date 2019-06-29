from sys import float_info
from PIL import Image
from numpy import linalg


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:
    def __init__(self, center, points):
        self.center = center
        self.points = points


class BaseProblemSolver:
    def __init__(self, img_path, n_cluster):
        self.n_cluster = n_cluster
        self.img_path = img_path
        self.clusters = [[] for _ in range(n_cluster)]
        self.img_points = self._get_image_data()

    def distance(self, p, q):
        pass

    def calculate_new_center(self, cluster):
        pass

    def formulate_new_clt_points(self):
        pass

    def single_fit_calculation(self):
        iteration_clusters = self.formulate_new_clt_points()
        diff = 0
        self.a
        pass
        # PODEMOS IMPLEMENTAR AQUI, ACHO Q FIT NAO MUDAREMOS

    def is_fit_enough(self):
        return True
        #### SABER SE DEVEMOS PARAR DE RE CLUSTERIZAR

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

    def __init__(self):
        self.__super__()


########## AI PRA FAZER AS COISAS VISUAIS, MUDAR OUTRO ARQUIVO #######

class DefaultSolver(EuclidianDistanceProblemSolver):
    def __init__(self):
        self.__super__()

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
            distances = [ self.distance(point, c.center) for c in self.clusters[i] ]
            (_, min_dist_index) = distances.index(min(distances))
            new_clusters[min_dist_index] = point

        return new_clusters

    def is_fit_enough(self):
        pass


class Runner:
    def __init__(self, img_path):
        self.problem_solver = EuclidianDistanceProblemSolver()

    def run(self):
        while not self.problem_solver.is_fit_enough():
            self.problem_solver.single_fit_calculation()


