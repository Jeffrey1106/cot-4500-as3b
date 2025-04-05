import numpy as np

def P1():
    # Augmented matrix approach: A|b
    # A is the 3x3 matrix, b is the 3x1 vector
    A = np.array([
        [ 2, -1,  1],
        [ 1,  3,  1],
        [-1,  5,  4]
    ], dtype=float)

    b = np.array([ 6, 0, -3 ], dtype=float)

    # Number of variables
    n = 3

    # Forward Elimination
    for i in range(n):
        # Pivot element (no partial pivoting here for simplicity)
        pivot = A[i, i]
        
        for j in range(i+1, n):
            # Factor to eliminate A[j, i]
            factor = A[j, i] / pivot
            # Eliminate from row j
            A[j, i:] = A[j, i:] - factor * A[i, i:]
            b[j]     = b[j]     - factor * b[i]

    # Back-Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        # Subtract the known terms
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i, j] * x[j]
        # Solve for x[i]
        x[i] = (b[i] - sum_ax) / A[i, i]

    return x  # returns a numpy array [x, y, z]

def P2():
    # We use the Doolittle method (no pivoting) for LU decomposition.
    # Define the matrix A.
    A = np.array([[1,  1,  0,  3],
                  [2,  1, -1,  1],
                  [3, -1, -1,  2],
                  [-1, 2,  3, -1]], dtype=float)
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Set ones on L's diagonal.
    for i in range(n):
        L[i, i] = 1.0

    # Compute first row of U.
    for j in range(n):
        U[0, j] = A[0, j]
    
    # Compute first column of L.
    for i in range(1, n):
        L[i, 0] = A[i, 0] / U[0, 0]
    
    # Compute remaining entries.
    for i in range(1, n):
        for j in range(i, n):
            sum_val = 0.0
            for k in range(i):
                sum_val += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - sum_val
        
        for j in range(i+1, n):
            sum_val = 0.0
            for k in range(i):
                sum_val += L[j, k] * U[k, i]
            L[j, i] = (A[j, i] - sum_val) / U[i, i]
    
    # The determinant is the product of U's diagonal elements.
    det = np.prod(np.diag(U))
    return det, L, U

def P3():
    """
    Checks if the following 5x5 matrix is diagonally dominant:
       9   0   5   2   1
       3   9   1   2   1
       0   7   2   1   3
       4   2   3  12   2
       3   2   4   0   2
    """
    A = np.array([
        [ 9,  0,  5,  2,  1],
        [ 3,  9,  1,  2,  1],
        [ 0,  7,  2,  1,  3],
        [ 4,  2,  3, 12,  2],
        [ 3,  2,  4,  0,  2]
    ], dtype=float)

    n = A.shape[0]
    for i in range(n):
        # Sum of the non-diagonal elements in row i
        row_sum = np.sum(np.abs(A[i])) - abs(A[i, i])
        # Check if |a_ii| >= sum of other elements in that row
        if abs(A[i, i]) < row_sum:
            return False  # Not diagonally dominant
    return True  # Every row satisfies diagonal dominance

def P4():
    """
    Checks if the following 3x3 matrix is positive definite:
       2  2  1
       2  3  0
       1  0  2
    """
    A = np.array([
        [2, 2, 1],
        [2, 3, 0],
        [1, 0, 2]
    ], dtype=float)

    # One quick way: check leading principal minors
    # 1x1 minor
    if A[0, 0] <= 0:
        return False

    # 2x2 minor
    top_left_2x2 = A[:2, :2]
    if np.linalg.det(top_left_2x2) <= 0:
        return False

    # 3x3 minor (the determinant of the full matrix)
    if np.linalg.det(A) <= 0:
        return False

    return True