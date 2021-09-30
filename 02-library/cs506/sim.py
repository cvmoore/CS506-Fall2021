import numpy as np
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])
    return res

def jaccard_dist(x, y):
    res = (len(x.intersection(y)) / len(x.union(y)))
    return res

def cosine_sim(x, y):
    disY = 0
    disX = 0
    for i in range(len(x)):
        disX = disX + x[i]
        disY = disY + y[i]
    num = np.dot(np.transpose(x) * y) / (disX * disY)
    return num

# Feel free to add more
