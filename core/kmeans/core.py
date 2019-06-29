class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:
    def __init__(self, center, points):
        self.center = center
        self.points = points


class BaseProblemSolver:
    def __init__(self, img_path):
        self.img_path = img_path
        self.clusters = []

    def distance(self, p, q):
        pass

    def calculate_new_center(self, cluster):
        pass

    def assign_points(self, cluster, points):
        pass

    def single_fit_calculation(self):
        pass
        # PODEMOS IMPLEMENTAR AQUI, ACHO Q FIT NAO MUDAREMOS

    def is_fit_enough(self):
        return True
        #### SABER SE DEVEMOS PARAR DE RE CLUSTERIZAR

    def get_image_points(self):
        pass
        # TODO IMPLEMENTAR AQUI, NAO DEVE MUDAR


class EuclidianDistanceProblemSolver(BaseProblemSolver):
    def distance(self, p, q):
        return 0


########## AI PRA FAZER AS COISAS VISUAIS, MUDAR OUTRO ARQUIVO #######

class Runner:
    def __init__(self, img_path):
        self.problem_solver = EuclidianDistanceProblemSolver()

    def run(self):
        while not self.problem_solver.is_fit_enough():
            self.problem_solver.single_fit_calculation()