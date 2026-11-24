import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    np_new = np.array(matrix)
    if mode == "column":
        return np.mean(np_new, axis=0).tolist()
    elif mode == "row":
        return np.mean(np_new, axis=1).tolist()  