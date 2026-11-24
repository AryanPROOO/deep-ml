import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    np_new=np.array(matrix)
    result=np_new*scalar
    return result.tolist()
