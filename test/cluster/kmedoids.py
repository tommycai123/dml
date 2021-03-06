from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
from dml.CLUSTER import KmedoidsC
features  = array([
[1,6,11.05],
[1,7.35,10.6],
[1,8.35,8.35],
[1,10.1,7.8],
[1,10.2,8.7],
[1,9.25,10],
[1,8.05,10.8],
[1,6.6,11.6],
[1,6.4,9.15],
[1,8.35,8.25],
[1,9.5,7.05],
[1,9.05,8.85],
[1,8.2,9.45],
[1,7.15,9.4],
[1,7.3,7.75],
[1,8.2,6.7],
[1,15.45,17.3],
[1,16.35,16.35],
[1,17.45,16.5],
[1,18.05,17.45],
[1,17.5,18.6],
[1,16.1,18.9],
[1,16.75,17.5],
[1,17.55,17.45],
[1,15.95,18.35],
[1,15.2,18],
[1,15,17.45],
[1,19.75,8.25],
[1,20.75,7.9],
[1,25.65,8.2],
[1,25.05,10.5],
[1,22.85,11.2],
[1,21.6,9.9],
[1,23.05,8.3],
[1,24.65,8.8],
[1,23.55,10.1],
[1,23.05,9.45],
[1,23.2,8.35],
[1,24.2,7.95],
[1,22.15,7.1],
[1,21.6,7.8],
[1,21.7,8.2]]).transpose()
a=KmedoidsC(features,3)
a.train()
print a.labels