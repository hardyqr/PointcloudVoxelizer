#!/bin/bash

ori_dir="$(pwd)"

# $1 is the home directory of the dataset
# $2 is Area_X_xyz_rgb_label
# $3 is the scale param 

cd $1/$2
echo "in $1/$2"

echo $ori_dir

if ! [ -e fmt_h5py_$3 ]; then
	mkdir fmt_h5py_${3}
	echo "fmt_h5py_${3} created"
fi


for room in $(ls *.txt); do
	python3 $ori_dir/p_to_v_main.py $room fmt_h5py_${3}/${room%.txt}_$3.h5 $3
done
