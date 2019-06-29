from core.kmeans import core

# def __init__(self, ncluster, img_path, mindif):

if __name__ == '__main__':
    runner = core.Runner(5, "../images/750x750bb.png", 10)
    res = runner.run()
    print(res)