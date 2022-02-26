# All Imports
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, execute, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
# Importing other relevant libraries
import numpy as np
import math

#---------------------------------------------------------------------
# Constants
pi = math.pi

# Variables to be updated when used
atom_dict = {"00":"H", "01":"C", "10":"O", "11":"N"}
shots = 1024

num_of_atom_bits = 2
num_of_coord_bits = 5
num_of_total_bits = num_of_atom_bits+3*num_of_coord_bits
#---------------------------------------------------------------------

# Converts binary integer into decimal number 
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal  

# Identifies atom based on the input bit string and the atom dictionary defined above 
def whichAtom(atom, num_of_qubits, dictionary):
    return dictionary[atom]

# Calculates the coordinate distance w.r.t. the number of qubits per coordinate (defined earlier)
def calcDistance(coord_dist, num_of_qubits):
    distance = binaryToDecimal(coord_dist)/(2**(num_of_qubits-2))
    return distance

# Runs a simulation of the quantum circuit in the QASM Simulator
# (built only for initial testing purposes)
# To use, must specify the quantum circuit as well as the shots
def experiment(quantum_circuit, shots):
    backend = Aer.get_backend('qasm_simulator')
    job = execute(quantum_circuit,backend, shots = shots)
    result = job.result()

    counts = result.get_counts()
    return counts

# Shows the histogram for the counts in a simulation
# (built only for initial testing purposes)
def plotCounts(counts):
    plot_histogram(counts)

# Returns the identified atom and corresponding x, y, z coordinates 
# Range of values depends on number of qubits representing each coordinate
# Note all coordinates (AKA distances) are in Angstroms
def atomsAndCoordinates(generatedVector):
    genVec = list(generatedVector)

    atom_bit_str = genVec[:num_of_atom_bits]
    #print(atom,"\n")

    x_coord = int(genVec[num_of_atom_bits:num_of_atom_bits+num_of_coord_bits])
    #print(x_coord,"\n")

    y_coord = int(genVec[num_of_atom_bits+num_of_coord_bits:num_of_atom_bits+2*num_of_coord_bits])
    #print(y_coord,"\n")

    z_coord = int(genVec[num_of_atom_bits+2*num_of_coord_bits:num_of_atom_bits+3*num_of_coord_bits])
    #print(z_coord,"\n")

    the_atom = whichAtom(atom_bit_str, num_of_atom_bits, atom_dict)
    the_x_dist = calcDistance(x_coord, num_of_coord_bits)
    the_y_dist = calcDistance(y_coord, num_of_coord_bits)
    the_z_dist = calcDistance(z_coord, num_of_coord_bits)

    return the_atom, the_x_dist, the_y_dist, the_z_dist
    #print(the_atom,"has a distance of (",the_x_dist,",",the_y_dist,",",the_z_dist,")")