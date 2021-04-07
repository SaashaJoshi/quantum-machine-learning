'''
Amplitude Embedding:
	Adjusts the amplitude of the states |0> and |1> i.e. a and b in:
		a|0> + b|1>
	
	Rotation gate is used to rotate the state to adjust the amplitude.
	S_x  = R_x(x)|0>
	S_x' = R_x(x')|1> (CHECK!)
'''

import pennylane as qml
from pennylane import numpy as np 
from pennylane.wires import Wires
from pennylane.ops import QubitStateVector

dev = qml.device('default.qubit', wires = 2)

@qml.template
def AmplitudeEmbedding(features, wires):
	'''
		Args:
			wires: wires in the circuit (iterable format)
			features: normalized array of features of size 2^wires

		Raises:
			ValueError: if dimension of feature vector is not 2^wires
	'''
	wires = Wires(wires)
	if len(features) == 2**len(wires):
		QubitStateVector(features, wires = wires)
	else:
		raise ValueError("Features {} should have the dimension ({},)".format(np.shape(features), 2**len(wires)))

@qml.qnode(dev)
def circuit(features):
	AmplitudeEmbedding(features, wires = range(2))
	# qml.Hadamard(wires = 0)
	return qml.probs(wires = 0)

features = np.array([1/2, 1/2, 1/2, 1/2])

circuit(features)
print(dev.state)

drawer = qml.draw(circuit)
print(drawer(features = features))

# norm = qml.math.sum(qml.math.abs(features) ** 2)
# print(norm)

# features = features/np.sqrt(norm)
# features = np.array(features)
# print(features)

# print(qml.math.shape(features))
# if qml.math.shape(features) == 1:
# 	print(True)
# elif qml.math.shape(features) != 1:
# 	print(False)