
### Data cleaning

#### Obtain 3D Voxelgrid from raw data

```bash
./make_xyz_rgb_label.sh [Area_X]
```

This produces a list of points in the format of "x y z r g b label" for evey room in `Area_X`.


```bash
./make_list_mats_to_h5py_mat.sh [home dir of the stanford dataset] [Area_X_xyz_rgb_label]
```

This converts the "x y z r g b label" list into `h5py` matrix and writes to files.

