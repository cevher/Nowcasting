import os
import numpy as np
import shutil
import random

# # Creating Train / Val / Test folders (One time use)
root_dir =  'Input' #'color'
classes_dir = ["c_0","c_1", "c_2","c_3","c_4", "c_5", "c_6", "c_7", "c_8", "c_9", "c_10", "c_11","c_12",
    "c_13", "c_14", "c_15", "c_16", "c_17", "c_18","c_19", "c_20","c_21", "c_22", "c_23","c_24",
    "c_25","c_26","c_27","c_28","c_29", "c_30","c_31","c_32","c_33", "c_34", "c_35", "c_36", "c_37"] 



val_ratio = 0.2
#test_ratio = 0.05

for clas in classes_dir:
    os.makedirs(root_dir +'/train/' + clas)
    os.makedirs(root_dir +'/val/' + clas)
    os.makedirs(root_dir +'/test/' + clas)


    # Creating partitions of the data after shuffeling
    src = root_dir + '/'+  clas # Folder to copy images from

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                              [int(len(allFileNames)* (1 - val_ratio + test_ratio)), 
                                                               int(len(allFileNames)* (1 - test_ratio))])


    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
    test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    # Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, root_dir +'/train/' + clas)

    for name in val_FileNames:
        shutil.copy(name, root_dir +'/val/' + clas)

    for name in test_FileNames:
        shutil.copy(name, root_dir +'/test/' + clas)