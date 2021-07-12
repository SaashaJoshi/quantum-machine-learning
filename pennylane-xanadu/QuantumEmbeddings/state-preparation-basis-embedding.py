'''
	State Preparation or Data Encoding encodes any input x into a quantum state
	S_x  -> |phi(x)>
	S_x' -> |phi(x')>

	Somewhat performs a feature embedding in quantum computer
	input -> feature vector in Hilbert Space

	This stste preperation procedure is a Feature Map.
	and
	feature map gives rise to a Kernel!
'''

import pennylane as qml
from pennylane import numpy as np 
from pennylane.wires import Wires
# from pennylane.templates.decorator import template

dev = qml.device('default.qubit', wires = 7)

@qml.template
def BasisEmbedding(features, wires):
	'''
	Basis Embedding:
		Helps in construction of computational basis state e.g. |01>.

	Args:
		wires: wires in the circuit in iterable format.
		features: input array of shape (n,).

	Raises: 
		ValueError: if wires and features do not have same shape.
	'''
	wires = Wires(wires)
	if len(wires) == len(features):
		for wire, bit in zip(wires, features):
			if bit == 1:
				qml.PauliX(wires = wire)
	else:
		raise ValueError("Features [{}] and Wires [{}] have different shapes".format(np.shape(features)[0], np.shape(wires)[0]))

@qml.qnode(dev)
def circuit(features):
	BasisEmbedding(features, wires = range(7))
	return qml.probs(wires = 0)

# wires = range(7)    # Iterable format of wires argument 
features = np.array([0, 0, 0, 1, 1, 0, 1])

print(circuit(features))
# print(circuit.draw())
drawer = qml.draw(circuit)
print(drawer(features = features))

'''
qml.templates.state_preparation.basis.BasisStatePreparation and qml.templates.BasisEncoding
are essentially the same functions. 
Also, the use of PauliX gate requires these functions to be first only.
'''