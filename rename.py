import os
import cv2
import numpy as np
import shutil
import random
from glob import glob
from fnmatch import fnmatch

# # Creating Train / Val / Test folders (One time use)

directory = '.'
c = 0
for fn in os.listdir(directory):
	dirname= os.path.join(directory, fn)
	
	
	for img in os.listdir(dirname):
		c+=1
		dst_name = "500.jpg"
		dst = os.path.join(dirname,dst_name)
		src = os.path.join(dirname,img)
		if fnmatch(img, "*500*"):
			os.rename(src, dst)

						 
			
			
