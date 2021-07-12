import pennylane as qml
from pennylane import numpy as np 

dev = qml.device('default.qubit', wires = 5)


def basis_state(features, wires):
	qml.templates.state_preparations.basis.BasisStatePreparation(features, wires = range(4))
	# features(grad_required = False), they are never trained and are fixed.

@qml.qnode(dev)
def variational_layers():
	pass

def circuit(features, weights):
	# wires = qml.wires.Wires(wires)
	basis_state(features, wires = range(5))

	# variational_layers()

	return qml.expval(qml.PauliZ(wires = 0))

def variational_classifier(parameter, features):
	weights = parameter[0]
	bias = parameter[1]
	return circuit(features, weights) + bias

def square_loss(labels, predictions):
	loss = 0
	for l, p in zip(labels, predictions):
		loss += (l - p) ** 2

	loss = loss / len(labels)

	return loss

def accuracy():
	# Calculate how many inputs are predicted correctly
	accuracy = 0
	threshold = 1e-5

	for l, p in zip(labels, predictions):
		if (l - p) < threshold:
			accuracy += 1

	return accuracy

# def 

features = np.array([0, 1, 1, 0])
parameters = [[1, 4, 5, 8], 0.0]

print(variational_classifier(parameters, features))

drawer = qml.draw(circuit)
print(drawer(features))