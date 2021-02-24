#import necessary stuff
import numpy as np 
import pandas as pd 
import math
import random

df = pd.read_csv(".csv")
data = np.array(df)

#intialize centroids index randomly
random_index_centroid = random(range(0,len(data)), 3)

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
def assign_nearest_centroids(data,k):
    #c here is selected centroids
    assigned_centroids = []
    for ele in data:
        dist = []
        for cent in k:
            dist.append(distance_from_centroid(i,j))
        assigned_centroids.append(dist.index(min(dist)))
    return assigned_centroids
            


#Move centroids based on mean of distances
def move_centroid_position(data, cluster):

    

def KMeans(data,k):
    centroids = select_centroid(random_index_centroid)
    assigned_centroids = assign_nearest_centroids(data,k)

