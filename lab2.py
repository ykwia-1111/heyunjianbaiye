import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
# Creating a sample dataset with 4 clusters
X, y = make_blobs(n_samples=100, n_features=3, centers=4)
# Initializing KMeans with 4 clusters
kmeans = _________________
# Fitting with inputs
kmeans = kmeans.__________(X)
# Labelling the clusters
labels = kmeans.__________(X)
print(labels)
# Getting the cluster centers
C = kmeans._______________
print(C)
