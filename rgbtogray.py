import os
import cv2
import numpy as np
import shutil
import random
from glob import glob

# # Creating Train / Val / Test folders (One time use)
root_dir = 'input/color/'
class_info = ['Aksu','Alanya','Antalya','Finike','Gazipasa','Kas','Kemer','Kumluca','Manavgat','Serik','Sparse']

directory = '.'
c = 0
for fn in os.listdir(directory):
	dirfile= os.path.join(directory, fn)
	
	if os.path.isdir(dirfile):
		dir = os.path.join(directory, dirfile)
		
		for file in os.listdir(dir):
				dir2 = os.path.join(dir,file)
				
				for img in os.listdir(dir2):
					
					print(c)
					if img.endswith(".jpg") or img.endswith(".jpg") or img.endswith(".png") or img.endswith(".png")  :

						read_dir=os.path.join(dir2,img)
						image = cv2.imread(read_dir)
						gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
						
						cv2.imwrite(os.path.join(dir2 , img),gray)
			
			
