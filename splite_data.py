import pandas as pd
import os


def data_splite(foldername, l, SaveFile_Path):
    folder_name = foldername
    Folder_Path = r'/Users/yqh/Desktop/' + folder_name
    SaveFile_Path = SaveFile_Path
    SaveFile_Name = folder_name

    os.chdir(Folder_Path)
    file_list = os.listdir()

    l = l
    for i in range(0, len(file_list)):

        filename = Folder_Path + '/' + file_list[i]
        j = 480 // l
        # if 480 % l == 0:
        #     j = (480 // l) + 1
        # else:
        #     j = (480 // l) + 2

        data = pd.read_csv(filename, chunksize=l)
        k = 1
        for chunk in data:
            if k <= j:
                chunk.to_csv(SaveFile_Path + '/' + SaveFile_Name + '_' + file_list[i] + str(k) + '.csv',
                             encoding="utf_8_sig",
                             index=False, header=False, mode='a+')
                k += 1


l = 480
SaveFile_Path = r'/Users/yqh/Desktop/1'
folder_list = ['bending1', 'bending2', 'cycling', 'lying', 'sitting', 'walking', 'standing']
for i in range(0, len(folder_list)):
    foldername = folder_list[i]
    data_splite(foldername, l, SaveFile_Path)
