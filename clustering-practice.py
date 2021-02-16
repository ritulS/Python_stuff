#import necessary stuff
import numpy as np 
import pandas as pd 
import math
import random

df = pd.read_csv("dataset.csv")
X = np.array(df)

#intialize centroids index randomly
random_index_centroid = random(range(0,len(X)), 3)

def select_centroid(random_index_centroid):
    centroids = []
    for i in random_index_centroid:
        centroids.append(df.loc[i])
    centroids = np.array(centroids)
    return centroids


#calculate distance of each point from all 3 centroids
def distance_from_centroid(a,b):
    return math.sqrt(sum(a - b)**2)

#assign point to the centroids
def assign_closest_centroids():
    assigned_centroids = []
    for i in X:
        distance = []
        for j in ic:
            distance.append(distance_from_centroid(i,j))
            


#Move centroids based on mean of distances
