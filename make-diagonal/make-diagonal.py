import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    ans =[]
    n = len(v)
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp.append(v[i])
            else:
                temp.append(0)

        ans.append(temp)

    
    return np.array(ans)