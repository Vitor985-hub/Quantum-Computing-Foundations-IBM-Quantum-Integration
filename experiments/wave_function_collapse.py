from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

backend = AerSimulator()
job = backend.run(qc, shots=1)
result = job.result()
print(f'resultado após colapso: {result.get_counts(qc)}')

fig = plot_histogram(result.get_counts(qc))
plt.show()