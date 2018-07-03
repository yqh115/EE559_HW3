import numpy as np
import matplotlib.pyplot as plt
import pandas

df = pandas.DataFrame(np.random.randn(1000,4 ), columns=['a', 'b', 'c', 'd'])
pandas.tools.plotting.scatter_matrix(df, alpha=0.2)
plt.show()