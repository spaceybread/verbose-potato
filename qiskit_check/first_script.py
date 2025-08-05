from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.h(0)

state = Statevector.from_instruction(qc)
probs = state.probabilities_dict()

probs_clean = {str(k): v for k, v in probs.items()}

plot_histogram(probs_clean)
plt.show()

