# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Importing other libraries
import math
import random
import numpy as np

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()

##################################################

numOfQubits = 4
readoutBits = numOfQubits
qreg = QuantumRegister(numOfQubits)
creg = ClassicalRegister(readoutBits)

gen = QuantumCircuit(qreg, creg)
#================================================#

#*************************************************
#Build initial rotation gates
def initRot(qc):
    qc.rx(math.pi, qreg[0:numOfQubits+1])
    qc.rx(math.pi, qreg[0:numOfQubits+1])
    qc.rz(math.pi, qreg[0:numOfQubits+1])
    qc.barrier()
    
#*************************************************
#Build All-to-All qubit connectivity 
paramList = []
def connectAllQubits(qc):  
    for controlQubit in range(numOfQubits-1):
        qc.h(qreg[controlQubit])
        for targetQubit in range(controlQubit+1,numOfQubits):
            rot = random.random()
            qc.crx(rot, qreg[controlQubit], qreg[targetQubit])
            paramList.append(rot)
        qc.barrier()
    return paramList
#*************************************************  


#*************************************************
def buildCircuit(qc=gen, layerNum=1):
    for layer in range(layerNum):
        initRot(qc)
        connectAllQubits(qc)
    qc.measure(qreg[0:numOfQubits], creg[0:readoutBits])
#*************************************************

if __name__ == '__main__':
    buildCircuit()