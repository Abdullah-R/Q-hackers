#%%
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi
import qiskit

# %%
# from qiskit_textbook.widgets import binary_widget
# binary_widget(nbits=5)
# # %%
# n = 8
# n_q = n
# n_b = n
# qc_output = QuantumCircuit(n_q,n_b)

# # %%
# for j in range(n):
#     qc_output.measure(j,j)

# # %%
# qc_output.draw()

# %%
# counts = execute(qc_output,Aer.get_backend('qasm_simulator')).result().get_counts()
# plot_histogram(counts)
# # %%
# qc_encode = QuantumCircuit(n)
# qc_encode.x(7)

# qc_encode.draw()

# # %%
# qc = qc_encode + qc_output
# qc.draw()

# # %%
# counts = execute(qc,Aer.get_backend('qasm_simulator')).result().get_counts()
# plot_histogram(counts)

# # %%
# qc_cnot = QuantumCircuit(2)
# qc_cnot.cx(0,1)
# qc_cnot.draw()

# # %%
# qc = QuantumCircuit(2,2)
# qc.x(0)
# qc.cx(0,1)
# qc.measure(0,0)
# qc.measure(1,1)
# qc.draw()

#%%
qc = QuantumCircuit(1,1)
qc.rx(pi/(pi/.6435),0)
qc.measure(0,0)
qc.draw('mpl')

counts = execute(qc,Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()

print(int(list(counts.keys())[0]))

#plot_histogram(counts)


# # %%
# qc_ha = QuantumCircuit(4,2)
# qc_ha.x(0)
# qc_ha.x(1)

# qc_ha.barrier()
# qc_ha.cx(0,2)
# qc_ha.cx(1,2)
# qc_ha.ccx(0,1,3)

# qc_ha.barrier()
# qc_ha.measure(2,0)
# qc_ha.measure(3,1)

# qc_ha.draw()
# # %%
# counts = execute(qc_ha,Aer.get_backend('qasm_simulator')).result().get_counts()
# plot_histogram(counts)
# %%
