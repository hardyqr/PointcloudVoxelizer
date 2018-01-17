# Freddy Fangyu Liu @Jiange, Sichuan, China 16/8/2017

from pointclouds_to_voxelgrid import *
from os import sys
import numpy as np
import h5py

# print(sys.argv[1])

data_loader = data_loader(sys.argv[1],(0,1,2))
xyz_range = data_loader.__xyz_range__()

#print(data_loader.d.shape)
#print(xyz_range)

full_mat, threeD_mat, threeD_label, list_mat, label_mat = data_loader(xyz_range,10,sys.argv[3]) # invoke __call__

#print(list_mat.shape)
#print(list_mat[0])
#print(label_mat.shape)
#print(label_mat[0])
#print(threeD_mat.shape)
#print(threeD_label.shape)

h5f = h5py.File(sys.argv[2], 'w')
h5f.create_dataset('default',data = full_mat)

#np.savez(sys.argv[2], full_mat)

print(sys.argv[2]+" done")
print("shape: "+ str(full_mat.shape))
