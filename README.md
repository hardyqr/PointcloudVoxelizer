
# Poincloud Voxelizer


## Usage
### Convert
```
python3 source/p_to_v_main.py [pointcloud.txt] [sample/voxel.h5py] [s]
```
- `pointcloud.txt`: source, should be in the list format [x y z r g b label]
- `sample/voxel.h5py`: destination, voxel matrix stores as h5py file
- `s`: the size of longest side after conversion

- requires [h5py](http://docs.h5py.org/en/latest/)

### Visualize
```
python2 visualization/visualize_npy.py [sample/voxel.h5py]
```
- requires [Mayavi](http://docs.enthought.com/mayavi/mayavi/)


## Sample
![sample](https://github.com/hardyqr/PointcloudVoxelizer/blob/master/sample/imgs/sample.png)

