import os
import scipy.misc


id_path = {}
with open('CUB_200_2011/CUB_200_2011/images.txt') as f:
    line = f.readline()
    while not line == '':
        line = line[:-1]
        key, path = line.split()
        id_path[int(key)] = os.path.join('CUB_200_2011/CUB_200_2011/', 'images', path)
        line = f.readline()

id_box = {}
with open('CUB_200_2011/CUB_200_2011/bounding_boxes.txt') as f:
    line = f.readline()
    while not line == '':
        line = line[:-1]
        id, x, y, width, height = line.split()
        id_box[int(id)] = (float(x), float(y), float(width), float(height))
        line = f.readline()


for id in id_path:
    image = scipy.misc.imread(id_path[id])
    x, y, width, height = id_box[id]
    scipy.misc.imsave(os.path.join('bird_large_dataset', str(id) + '.jpg'), scipy.misc.imresize(image[int(y):int(y+height), int(x):int(x + width)], [64, 64]))





