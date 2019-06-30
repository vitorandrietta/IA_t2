from core.kmeans import core

# def __init__(self, ncluster, img_path, mindif):

if __name__ == '__main__':
    runner = core.Runner(5, "../images/whatsapp-image-2019-03-27-at-08.57.09.jpeg", 1)
    res = runner.run()
    print(res)