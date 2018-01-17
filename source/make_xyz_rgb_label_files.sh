#!/bin/bash

# Freddy Fangyu Liu @BNU 387
# Aug 23, 2017

# celing 0
# floor 1
# wall 2
# column 3
# beam 4 
# window 5
# door 6
# table 7
# chair 8
# bookcase 9
# sofa 10
# board 11
# clutter 12

# $2 is root dir of the dataset
cd $2

# $1 is [Area_X]
if ! [ -e ${1}_xyz_rgb_label ] ; then
	mkdir ${1}_xyz_rgb_label
	echo "created $1_xyz_rgb_label directory"	
fi

cd $1 # in /Area_X

for folder in $(ls); do
	if [ -d $folder ]; then
		cd ../${1}_xyz_rgb_label
		touch ${folder}_xyz_rgb_label.txt 
		cd ../${1}/$folder/Annotations
		for file in $(ls *.txt); do
			touch ${file}.tmp
			echo $folder ${file%_*.txt} $file
			python3 ../../../data_cleaning/pyjoint.py ${file%_*.txt} $file
			cat ${file}.tmp >> ../../../${1}_xyz_rgb_label/${folder}_xyz_rgb_label.txt
			rm *.tmp
		done
		cd ../../ # back to /Area_X
	fi
done
