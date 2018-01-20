# Freddy Fangyu Liu @Jiange, Sichuan, China

import numpy as np
import pandas as pd
from os import sys


class data_loader:
    def __init__(self, data_dir, xyz_index=(0,1,2), ext=False):
        self.d = np.genfromtxt(data_dir,delimiter=' ')
        self.ext = ext
        self.x, self.y, self.z = xyz_index

    def __call__(self, xyz_range=None,threshold=10, mag_coeff=100,_format='xyzrgbl'):
        if not xyz_range:
            xyz_range=[int(itm) for itm in [
        self.d[:, self.x].min(),
        self.d[:, self.y].min(),
        self.d[:, self.z].min(),
        self.d[:, self.x].max(),
        self.d[:, self.y].max(),
        self.d[:, self.z].max(),
        ]]
        full_list, list_matrix, label_matrix = self.__get_list_matrix__(xyz_range)
        if not self.ext:
            threeD_xyz_rgb_label, threeD_matrix, threeD_label = self.__get_3D_matrix__(full_list, list_matrix, xyz_range, mag_coeff,_format)
        else:
            #TODO
            raise "data_loader >> extension temporarily-unavailable !"
        return threeD_xyz_rgb_label, threeD_matrix, threeD_label, list_matrix, label_matrix

  # data matrix -(xyz range)-> list and label matrix 
    def __get_list_matrix__(self,  xyz_range):
        X = self.d
        lx,ly,lz,hx,hy,hz = xyz_range
        X = X[
                (X[:,self.x]>=lx)&
                (X[:,self.x]<hx)&
                (X[:,self.y]>=ly)&
                (X[:,self.y]<hy)&
                (X[:,self.z]>=lz)&
                (X[:,self.z]<hz)
                ]
        return X, X[:,:-1], X[:, (self.x, self.y, self.z,-1)]
        # last column is label

    # list matrix -> 3D matrix
    def __get_3D_matrix__(self, full_list, list_matrix, xyz_range, mag_coeff,_format):
        lx,ly,lz,hx,hy,hz = xyz_range
        magnifier = int(mag_coeff)/(hx-lx) # control the scale of x (to be ...)
        dx, dy, dz = map(int, [(hx-lx)*magnifier, (hy-ly)*magnifier, (hz-lz)*magnifier])
        threeD_xyz_rgb_label = np.zeros(shape=[dx,dy,dz,self.d.shape[1]], dtype=np.float32)
        threeD_matrix = np.zeros(shape=[dx, dy, dz, list_matrix.shape[1]], dtype=np.float32)
        threeD_label = np.zeros(shape=[dx, dy, dz], dtype=np.float32)
        for itm in full_list:
            x,y,z = itm[[self.x, self.y, self.z]]
            threeD_xyz_rgb_label[int((x-lx)*magnifier)-1][int((y-ly)*magnifier)-1][int((z-lz)*magnifier)-1] = itm
            threeD_matrix[int((x-lx)*magnifier)-1][int((y-ly)*magnifier)-1][int((z-lz)*magnifier)-1] = itm[0:6]#to be fixed
            threeD_label[int((x-lx)*magnifier)-1][int((y-ly)*magnifier)-1][int((z-lz)*magnifier)-1] = itm[-1]
        return threeD_xyz_rgb_label, threeD_matrix, threeD_label
    
    def __xyz_range__(self):
        x_min = self.d[:,self.x].min()
        x_max = self.d[:,self.x].max()
        y_min = self.d[:,self.y].min()   
        y_max = self.d[:,self.y].max()   
        z_min = self.d[:,self.z].min()
        z_max = self.d[:,self.z].max()
        return x_min,y_min,z_min,x_max,y_max,z_max
