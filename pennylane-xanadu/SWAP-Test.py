'''
	SWAP Test is used to measure the fidelity of Quantum States.
	Fidelity refers to the overlap of states. It can be calculated using the inner product of the states.
	Inner Product == SWAP Test == Fidelity

	If states overlap (equal), probability of state 0 is 1
	If states do not overlap (orthogonal), probability of state 0 is 0.5
'''

import pennylane as qml
from pennylane import numpy as np

dev = qml.device('default.qubit', wires = 3)

@qml.qnode(dev)
def circuit():
	qml.BasisState(np.array([0, 1, 0]), wires = [0, 1, 2])    # Initializes the quantum state
	qml.Hadamard(wires = 0)    # Auxiliary qubit/wire
	qml.CSWAP(wires = [0, 1, 2])
	qml.Hadamard(wires = 0)
	return qml.probs(wires  = 0)    # Returns either [1 0] or [0.5 0.5]

print(circuit())
print(circuit.draw())