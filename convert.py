import os
import sys

def convert(imgf, labelf, outf, n, d):
    f = open(imgf, "rb")
    l = open(labelf, "rb")
    o = open(outf, "w")
    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        if  ord(l.read(1))  ==  d :
            image = []
            for j in range(28*28):
                image.append(ord(f.read(1)))
            images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")

    f.close()
    o.close()
    l.close()

convert("train-images.idx3-ubyte","train-labels.idx1-ubyte","test.csv", sys.argv[0] , sys.argv[1] )