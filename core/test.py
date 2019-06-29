from core.kmeans import core

# def __init__(self, ncluster, img_path, mindif):


if __name__ == '__main__':
    runner = core.Runner(5, "/home/andrietta/PycharmProjects/IA_t4/images/750x750bb.png", 3)
    res = runner.run()
    print(res)