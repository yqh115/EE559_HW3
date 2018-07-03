from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt

j = 20
Folder_Path = r"/Users/yqh/Desktop/" + str(j)
file_name = Folder_Path + '/' + str(j) + r"_training.csv"

X = pd.read_csv(file_name, header=None, usecols=range(0, 41))
y = pd.read_csv(file_name, header=None, usecols=[42])

LR = LogisticRegression(penalty='l1')
rfecv = RFECV(estimator=LR, step=1, cv=5, scoring='accuracy')
rfecv = rfecv.fit(X, y)
# print(rfecv.support_)
# print(rfecv.ranking_)
print("Optimal number of features : %d" % rfecv.n_features_)

plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.title('l = ' + str(j))
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()
