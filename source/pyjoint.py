# Freddy Fangyu Liu @BNU 387
# Aug 23, 2017

import numpy as np
import sys

# argv1 [the file to process]

# a dictionary

label_dict = {
	"ceiling":0, 
	"floor":1, 
	"wall":2, 
	"column":3, 
	"beam":4, 
	"window":5 , 
	"door":6, 
	"table":7,
	"chair":8, 
	"bookcase":9, 
	"sofa":10, 
	"board":11, 
	"clutter":12
}


data = np.loadtxt(sys.argv[2],delimiter=' ')
new_col = [label_dict[sys.argv[1]]]*len(data)
new_col = np.array(new_col)

data = np.column_stack((data, new_col))
np.savetxt(sys.argv[2]+".tmp",data,fmt='%.3f %.3f %.3f %i %i %i %i ')
