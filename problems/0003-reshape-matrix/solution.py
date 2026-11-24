import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    ap = np.array(a)
    if ap.size != new_shape[0] * new_shape[1]:
        return []
    new = ap.reshape(new_shape)
    return new.tolist()