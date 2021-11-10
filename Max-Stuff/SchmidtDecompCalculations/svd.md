# Singular Value Decomposition
## Calculating the SVD for Schmidt Decomposition

Import some modules
> ```python
> import numpy as np
> from scipy.linalg import *
> ```

Use the `scipy.linalg.svd(A)` function to get the matrices U, Sigma, and V Transpose from SVD.
> ```python
> A = array([[1, 2], [3, 4], [5, 6]])
> print(A)
> U, s, VT = svd(A)
> print(U)
> print(s)
> print(VT)
> ```

There's just *one* problem for reconstructing SVD: **the matrices don't have the correct shape for multiplication**.
