# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:22:08 2018

@author: DELL
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
#import cv2

img = mpimg.imread("C:/Users/DELL/Downloads/cup.jpg")
plt.imshow(img)
imgplot = plt.imshow(img)
plt.axis('off')
plt.show() 
# Dừng enter tiếp tục
#cv2.waitKey(0)

X = img.reshape((img.shape[0]*img.shape[1], 3))
#print(X.shape)
#for K in [2, 3, 10, 15, 20]:
for K in [2, 3]:
    kmeans = KMeans(n_clusters=K).fit(X)
    label = kmeans.predict(X)

    img4 = np.zeros_like(X)
    # replace each pixel by its center
    for k in range(K):
        img4[label == k] = kmeans.cluster_centers_[k]
    # reshape and display output image
    img5 = img4.reshape((img.shape[0], img.shape[1], img.shape[2]))
    plt.imshow(img5, interpolation='nearest')
    plt.axis('off')
    plt.show()
    #cv2.waitKey(0)
    
    

