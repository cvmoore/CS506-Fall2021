from collections import defaultdict
from math import inf
import random
import csv
from random import randint


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    finalPoint = []
    for i in range(len(points)):
        for point in range(len(points[i])):
            sumP = [sum(X) for X in points[point[X]]]
            sumP = [sumP[0] / len(points)]
        finalPoint = finalPoint+sumP
    return finalPoint



def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    raise NotImplementedError()

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    raise NotImplementedError()

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    ans = []
    for i in range(k):
        new = []
        for iterate in range(len(dataset[0])):
            index = randint(len(dataset))
            index2 = randint(len(dataset[index]))
            new = new+[dataset[index][index2]]
        ans = ans+new
    return ans

def cost_function(clustering):
    raise NotImplementedError()


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    raise NotImplementedError()


def _do_lloyds_algo(dataset, k_points):
    assigned_points = assign_points(dataset, k_points)
    old_points = None
    while assigned_points != old_points:
        new_centers = update_centers(dataset, assigned_points)
        old_points = assigned_points
        assigned_points = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assigned_points, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
