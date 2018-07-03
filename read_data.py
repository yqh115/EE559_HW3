from os import walk
import pandas as pd
import numpy as np

dataframe_list = []
# a = np.zeros((1000, 1000))
# walk会返回3个参数，分别是路径，目录list，文件list，你可以按需修改下
for root, dirs, files in walk("/Users/yqh/Desktop/bending1"):
    for files in dirs:
        fr = open(files, 'r').read()
        with open('bending1.csv', 'a') as f:
            f.write(fr)

