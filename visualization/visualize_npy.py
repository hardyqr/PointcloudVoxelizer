
import mayavi.mlab
import numpy as np
import tqdm
import h5py
from os import sys

#data = np.load(sys.argv[1])
data = h5py.File(sys.argv[1], 'r')
data = data['default'][:]

#print data.shape

xx, yy, zz, sub = np.where(data != 0)

print xx.shape, sub.shape

rgbs = [(0,0,0)]*len(xx)
labels = [0]*len(xx)
for count in range(len(xx)):
    item = data[xx[count]][yy[count]][zz[count]]
    rgbs[count] = (float(item[3]),float(item[4]),float(item[5]))
    labels[count] = float(item[6])/12

rgbs = np.array(rgbs)
labels = np.array(labels)
print rgbs.shape, labels.shape

nodes = mayavi.mlab.points3d(xx, yy, zz, mode="cube", scale_factor=0.8)


nodes.glyph.scale_mode = 'scale_by_vector'
nodes.mlab_source.dataset.point_data.scalars = labels


mayavi.mlab.show()


