# UsefulAnsatz.md
### Explanation of Code

#### Imports
Pretty straightforward, nothing really to explain here.  
Just a bunch of useful modules (default).

```python
import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()
```

**Hard-coded value of** ```num_qubits = 4```

#### UsefulAnsatz Function
```python
def UsefulAnsatz(num_qubits, params): #defines function
    index = 0 #to iterate through all values in params
    qc = QuantumCircuit(num_qubits) #creates a quantum circuit with num_qubits qubits
    for i in range(num_qubits): #just your everyday python for loop
        qc.rx(params[index], i) #rx gate on ith qubit with angle params[index]
        index += 1 #increase index by 1
    for i in range(num_qubits):
        qc.rz(params[index], i) #rz gate on ith qubit with angle params[index]
        index += 1 #increase index by 1
    for i in range(0, num_qubits, 2): #for staggered ZZ layer
        qc.rzz(params[index], i, i+1) #rzz gate on ith and (i+1)th qubit with angle params[index]
        index += 1 #increase index by 1
    for i in range(1, num_qubits-1, 2): #for staggered ZZ layer
        qc.rzz(params[index], i, i+1) #rzz gate on ith and (i+1)th qubit with angle params[index]
        index += 1 #increase index by 1
    return qc #return the quantum circuit
```
*Staggered ZZ Layer = ZZ gates on each qubit pair in* \[\[0,1\], \[2,3\] ... \[n-2,n-1\]\]
*followed by ZZ gates on each qubit pair in* \[\[1,2\], \[3,4\] ... \[n-4,n-3\]\]
*where n is the number of qubits.*
   
   
