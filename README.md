
# Poincloud Voxelizer


## Usage
### Convert
```
python3 p_to_v_main.py [pointcloud.txt] [voxel.h5py] s
```
- `pointcloud.txt` should be in the list format [x,y,z,r,g,b,label]
- `s` is the size of longest side after conversion

### Visualize
```
python2 visualization/visualize_npy.py [voxel.h5py]
```
- requires Mayavi


## Sample
![sample](https://github.com/hardyqr/PointcloudVoxelizer/blob/master/sample/imgs/sample.png)
