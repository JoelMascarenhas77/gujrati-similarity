import numpy as np

def euclidean_distance(v1, v2):
    total_distance = np.sqrt(np.sum((np.array(v1) - np.array(v2)) ** 2))
    return total_distance

def hamilton_distance(v1, v2):
    total_distance = np.sum(np.abs(np.array(v1) - np.array(v2)))
    return total_distance

def cosine_similarity(v1,v2):
    dot_prod = np.dot(np.array(v1), np.array(v2))
    v1_sum = np.sqrt(np.sum(np.square(v1)))
    v2_sum = np.sqrt(np.sum(np.square(v2)))
    return dot_prod/(v1_sum*v2_sum)


def get_similarity(v1,v2):
    similarity_scores = {
        "cosine":  cosine_similarity(v1,v2),
        "euclidean": euclidean_distance(v1, v2),
        "hamilton":  hamilton_distance(v1, v2)
    }
    return similarity_scores
