# Singular Value Decomposition
## Calculating the SVD for Schmidt Decomposition

Import some modules
> ```python
> import numpy as np
> from scipy.linalg import *
> ```

Use the `scipy.linalg.svd(A)` function to get the matrices `U`, `Sigma`, and `V Transpose` from SVD.
> ```python
> A = array([[1, 2], [3, 4], [5, 6]])
> print(A)
> U, s, VT = svd(A)
> print(U)
> print(s)
> print(VT)
> ```

There's just *one* problem for reconstructing SVD: **the matrices don't have the correct shape for multiplication**.  
We require `U (m x m) . Sigma (m x n) . V^T (n x n)` but we have `U (m x m) . Sigma (n x n) . V^T (n x n)`.  
We can fix this by creating a new Sigma matrix of all zero values that is m x n and populating
the first n x n part of the matrix with the square diagonal matrix calculated via `diag()`.

> ```python
> A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
> print(A)
> # Singular-value decomposition
> U, s, VT = svd(A)
> # create n x n Sigma matrix
> Sigma = diag(s)
> # reconstruct matrix
> B = U.dot(Sigma.dot(VT))
> print(B)
> ```

This problem only occurs when `m` and `n` are equal.
