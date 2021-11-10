# Calculating Schmidt Decomposition of a Tensor
## Using pyqentangle: Quantum Entanglement in Python

> release 3.1.10  
> supports python > 3.5

### What is pyqentangle?
[`pyqentangle`](https://pypi.org/project/pyqentangle/) is a module that allows you to calculate the Schmidt Decomposition of a Tensor.
This is going to be useful in our **data encoding**. Install it via `pip install -U pyqentangle`.

### Schmidt Decomposition for Discrete Bipartite States
An example of Discrete Bipartite States: **|01> + |10>**.  
We can write this as 
```python
import pyqentangle
import numpy as np
tensor = np.array([[0., np.sqrt(0.5)], [np.sqrt(0.5), 0.]])
```
To perform the Schmidt Decomposition, there's the handy built-in function `pyqentangle.schmidt_decomposition()`.
Use it like:
```python
pyqentangle.schmidt_decomposition(tensor)
```
This produces the output:
```python
[(0.7071067811865476, array([ 0., -1.]), array([-1., -0.])),
(0.7071067811865476, array([-1.,  0.]), array([-0., -1.]))]
```
