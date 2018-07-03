import pandas as pd
import os
import numpy as np


def calculate(filename):
    b = np.zeros((1, 42))
    file_name = filename
    a1 = pd.read_csv(file_name, header=1, usecols=[0], engine='python')
    a2 = pd.read_csv(file_name, header=1, usecols=[1], engine='python')
    a3 = pd.read_csv(file_name, header=1, usecols=[2], engine='python')
    a4 = pd.read_csv(file_name, header=1, usecols=[3], engine='python')
    a5 = pd.read_csv(file_name, header=1, usecols=[4], engine='python')
    a6 = pd.read_csv(file_name, header=1, usecols=[5], engine='python')

    b[0][0] = a1.min()
    b[0][1] = a1.max()
    b[0][2] = a1.mean()
    b[0][3] = a1.median()
    b[0][4] = a1.std()
    b[0][5] = a1.quantile(0.25)
    b[0][6] = a1.quantile(0.75)

    b[0][7] = a2.min()
    b[0][8] = a2.max()
    b[0][9] = a2.mean()
    b[0][10] = a2.median()
    b[0][11] = a2.std()
    b[0][12] = a2.quantile(0.25)
    b[0][13] = a2.quantile(0.75)

    b[0][14] = a3.min()
    b[0][15] = a3.max()
    b[0][16] = a3.mean()
    b[0][17] = a3.median()
    b[0][18] = a3.std()
    b[0][19] = a3.quantile(0.25)
    b[0][20] = a3.quantile(0.75)

    b[0][21] = a4.min()
    b[0][22] = a4.max()
    b[0][23] = a4.mean()
    b[0][24] = a4.median()
    b[0][25] = a4.std()
    b[0][26] = a4.quantile(0.25)
    b[0][27] = a4.quantile(0.75)

    b[0][28] = a5.min()
    b[0][29] = a5.max()
    b[0][30] = a5.mean()
    b[0][31] = a5.median()
    b[0][32] = a5.std()
    b[0][33] = a5.quantile(0.25)
    b[0][34] = a5.quantile(0.75)

    b[0][35] = a6.min()
    b[0][36] = a6.max()
    b[0][37] = a6.mean()
    b[0][38] = a6.median()
    b[0][39] = a6.std()
    b[0][40] = a6.quantile(0.25)
    b[0][41] = a6.quantile(0.75)

    return b


def extra(j):
    # j = 5
    Folder_Path = r"/Users/yqh/Desktop/" + str(j) + r"/testing"
    # SaveFile_Path = '/Users/yqh/Desktop/' + str(j) + '/'
    SaveFile_Path = r'/Users/yqh/Desktop'
    SaveFile_Name = str(j) + r"_testing.csv"

    os.chdir(Folder_Path)

    file_list = os.listdir()

    filename = Folder_Path + '/' + file_list[0]
    if file_list[0] != '.DS_Store':
        b = calculate(filename)
        df = pd.DataFrame(data=b)
        if "bending" in filename:
            df['label'] = 'g'
        else:
            df['label'] = 'r'
        df.to_csv(SaveFile_Path + '/' + SaveFile_Name, encoding="utf_8_sig", index=False)
    else:
        print('first file is not valid')

    for i in range(1, len(file_list)):
        filename = Folder_Path + '/' + file_list[i]
        if file_list[i] != '.DS_Store':
            b = calculate(filename)
            df = pd.DataFrame(data=b)
            if "bending" in filename:
                df['label'] = 'g'
            else:
                df['label'] = 'r'
            df.to_csv(SaveFile_Path + '/' + SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')
        else:
            continue


for j in range(20, 21, 1):
    extra(j)
