# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# Importing the dataset
dataset = pd.read_csv('VICTIM_OF_MURDER_0.csv')
X = dataset.iloc[:, [3,9]].values

# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 15), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 14, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1 - 2001')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2 - 2002')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3 - 2003')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4 - 2004')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5 - 2005')
plt.scatter(X[y_kmeans == 5, 0], X[y_kmeans == 5, 1], s = 100, c = 'pink', label = 'Cluster 6 - 2006')
plt.scatter(X[y_kmeans == 6, 0], X[y_kmeans == 6, 1], s = 100, c = 'orange', label = 'Cluster 7 - 2007')
plt.scatter(X[y_kmeans == 7, 0], X[y_kmeans == 7, 1], s = 100, c = 'purple', label = 'Cluster 8 - 2008')
plt.scatter(X[y_kmeans == 8, 0], X[y_kmeans == 8, 1], s = 100, c = 'black', label = 'Cluster 9 - 2009')
plt.scatter(X[y_kmeans == 9, 0], X[y_kmeans == 9, 1], s = 100, c = '#FD4567', label = 'Cluster 10 - 2010')
plt.scatter(X[y_kmeans == 10, 0], X[y_kmeans == 10, 1], s = 100, c = 'violet', label = 'Cluster 11 - 2011')
plt.scatter(X[y_kmeans == 11, 0], X[y_kmeans == 11, 1], s = 100, c = 'grey', label = 'Cluster 12 - 2012')
plt.scatter(X[y_kmeans == 12, 0], X[y_kmeans == 12, 1], s = 100, c = 'brown', label = 'Cluster 13 - 2013')
plt.scatter(X[y_kmeans == 13, 0], X[y_kmeans == 13, 1], s = 100, c = 'gold', label = 'Cluster 14 - 2014')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, c = 'yellow', label = 'Centroids')
plt.title('Clusters of Victims of Murder')
plt.xlabel('Number of Age')
plt.ylabel('Number of People')
plt.legend()
plt.show()


dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('People')
plt.ylabel('Euclidean distances')
plt.show()

# Fitting Hierarchical Clustering to the dataset
hc = AgglomerativeClustering(n_clusters = 14, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1- 2001')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2 - 2002')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3 - 2003')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4 - 2004')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5 - 2005')
plt.scatter(X[y_hc == 5, 0], X[y_hc == 5, 1], s = 100, c = 'yellow', label = 'Cluster 6- 2006')
plt.scatter(X[y_hc == 6, 0], X[y_hc == 6, 1], s = 100, c = 'orange', label = 'Cluster 7 - 2007')
plt.scatter(X[y_hc == 7, 0], X[y_hc == 7, 1], s = 100, c = 'pink', label = 'Cluster 8 - 2008')
plt.scatter(X[y_hc == 8, 0], X[y_hc == 8, 1], s = 100, c = 'gold', label = 'Cluster 9 - 2009')
plt.scatter(X[y_hc == 9, 0], X[y_hc == 9, 1], s = 100, c = 'violet', label = 'Cluster 10 - 2010')
plt.scatter(X[y_hc == 10, 0], X[y_hc == 10, 1], s = 100, c = 'purple', label = 'Cluster 11 - 2011')
plt.scatter(X[y_hc == 11, 0], X[y_hc == 11, 1], s = 100, c = 'grey', label = 'Cluster 12 - 2012')
plt.scatter(X[y_hc == 12, 0], X[y_hc == 12, 1], s = 100, c = 'black', label = 'Cluster 13 - 2013')
plt.scatter(X[y_hc == 13, 0], X[y_hc == 13, 1], s = 100, c = 'brown', label = 'Cluster 14 - 2014')
plt.title('Clusters of Victims of Murder')
plt.xlabel('Number of Age')
plt.ylabel('Number of People')
plt.legend()
plt.show()