from sklearn import datasets
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression

dataset = datasets.load_iris()
model = LogisticRegression()
rfe = RFECV(model, step=1, cv=5)
rfe = rfe.fit(dataset.data, dataset.target)
print(rfe.support_)
print(rfe.ranking_)