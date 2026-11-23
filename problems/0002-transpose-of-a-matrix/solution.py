import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    matrix = np.array(a)
    result = matrix.T
    return result.tolist()