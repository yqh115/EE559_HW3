import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix

file_name1 = 'trainingdata1.csv'
file_name2 = 'label.csv'
a = pd.read_csv(file_name1, header=0)
b = pd.read_csv(file_name2, header=0)
print(b)
bb = np.squeeze(b)
print(bb)
df = pd.DataFrame(a)
print(df)
g = scatter_matrix(df, alpha=1, c=np.squeeze(b), figsize=[10, 10], marker='.')
plt.savefig('scatter_plot_1.png')
plt.show()