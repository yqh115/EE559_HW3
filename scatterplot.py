import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix

file_name1 = '2_splite.csv'
label = ['label']
cols_except = ['6', '7', '8', '9', '10', '11', '12', '13', '14', 'label']

a = pd.read_csv(file_name1, usecols=lambda x: x not in cols_except, header=0)
b = pd.read_csv(file_name1, usecols=label, header=0)

bb = np.squeeze(b)

df = pd.DataFrame(a)

g = scatter_matrix(df, alpha=1, c=np.squeeze(b), figsize=[10, 10], marker='.')
plt.savefig('scatter_plot_2.png')
plt.show()
