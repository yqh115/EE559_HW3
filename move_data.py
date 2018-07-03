import pandas as pd
import os
import shutil
import numpy as np

i = 1
Folder_Path = r'/Users/yqh/Desktop/' + str(i)
old_pos = r'/Users/yqh/Desktop/' + str(i)
new_pos1 = r'/Users/yqh/Desktop/testing/'
new_pos2 = r'/Users/yqh/Desktop/training/'

os.chdir(Folder_Path)
file_list = os.listdir()

testing_list = ['bending1_dataset1.', 'bending1_dataset2.', 'bending2_dataset1.', 'bending2_dataset2.',
                'cycling_dataset1.', 'cycling_dataset2.', 'cycling_dataset3.',
                'lying_dataset1.', 'lying_dataset2.', 'lying_dataset3.',
                'sitting_dataset1.', 'sitting_dataset2.', 'sitting_dataset3.',
                'walking_dataset1.', 'walking_dataset2.', 'walking_dataset3.',
                'standing_dataset1.', 'standing_dataset2.', 'standing_dataset3.']

no_use_list = ['.DS_Store']

for i in range(0, len(file_list)):
    filename = Folder_Path + '/' + file_list[i]
    l = 0
    if no_use_list[0] in filename:
        l = l + 100000
    else:
         l = 0

    for j in range(0, len(testing_list)):
        if testing_list[j] in filename:
            l = l + 1
        else:
            l = l

    if l == 0:
        shutil.move(filename, new_pos2)
    elif l==1:
        shutil.move(filename, new_pos1)
    else:
        continue
