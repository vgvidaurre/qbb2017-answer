#!/usr/bin/env python

import sys
import math
import itertools
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hac
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
from sklearn.cluster import KMeans

"""

"""


in_file = open(sys.argv[1],'r')
#saves the column/row headers (conditions/genes) into an array
col_headers = in_file.next().strip().split()[1:]
row_headers = []
data_matrix = []

for line in in_file:
	data = line.strip().split('\t')
	row_headers.append(data[0])
	data_matrix.append([float(x) for x in data[1:]])

#convert the data array into a numpy array
data_matrix_np = np.array(data_matrix) 

linkage_matrix = hac.linkage(data_matrix_np, method = "average")
heatmap_order = hac.leaves_list(linkage_matrix)

transposed_matrix = hac.linkage(data_matrix_np.T, method = "average")
transposed_heatmap = hac.leaves_list(transposed_matrix)

ordered_matrix = data_matrix_np[heatmap_order,:][:, transposed_heatmap]

labels = np.array(['CFU', 'poly', 'unk', 'int', 'mys', 'mid'])
t_labels = labels[transposed_heatmap]
plt.figure()
plt.imshow(ordered_matrix, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], t_labels) 
plt.savefig("heatmap.png") # Save the image
plt.close()


plt.figure()
hac.dendrogram(transposed_matrix, labels=labels )
plt.savefig( 'dendrogram.png' )
plt.close()


k_means = KMeans( n_clusters=5, random_state=0 )
k_means.fit( data_matrix_np )
labels = k_means.predict( data_matrix_np )
data_matrix_df = pd.merge( pd.DataFrame(data_matrix_np, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = data_matrix_df.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], t_labels) 
plt.savefig("k_clustered.png") # Save the image
plt.close()




