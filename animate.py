#%%
from celluloid import Camera
from matplotlib import pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi


def infected(peeps):
    sz = int(np.sum(peeps[4,:]))
    inf = np.zeros([5,sz])
    ind = np.where(peeps[4,:]==1)
    for i in range(sz):
        inf[:,i] = peeps[:,ind[0][i]]
    return inf

def qc_check(p):
    qc = QuantumCircuit(1,1)
    theta = 2*np.arcsin(sqrt(p))
    qc.rx(theta,0)
    qc.measure(0,0)
    qc.draw('mpl')

    counts = execute(qc,Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()

    return(int(list(counts.keys())[0]))
# %%
pn=150
fig = plt.figure()
camera = Camera(fig)

loc = (np.random.rand(5, pn) - 1/2)
loc[4,:] = 0
loc[4, 6] = 1
loc[[2,3],:] = loc[[2,3],:]/100
for i in range(50):

    inf = infected(loc)

    for j in range(pn):
        #plotting
        col = 'black'
        if loc[4,j] == 1: col = 'red'
        plt.plot(loc[0,j], loc[1,j], '.' ,color = col)

        #check for infection
        minDist = 10
        if loc[4,j] == 0:
            for k in range(inf[1,].size):
                dist = np.linalg.norm(loc[[0,1],j]-inf[[0,1],k])
                if dist < minDist: minDist = dist
            
            if minDist < 0.05:
                loc[4,j] = qc_check(0.1)

        #checking velocities
        if np.abs(loc[0,j]) > 0.5:
            loc[2,j] = -loc[2,j]
        if np.abs(loc[1,j]) > 0.5:
            loc[3,j] = -loc[3,j]


    camera.snap()
    mov = (np.random.rand(2, pn) - 1/2)/150
    loc[[2,3],:] = loc[[2,3],:] + mov
    loc[[0,1],:] = loc[[2,3],:] + loc[[0,1],:]

animation = camera.animate()
animation.save('my_animation.gif')



# # %%
# loc = (np.random.rand(5, 50) - 1/2)
# loc[4,:] = 0
# loc[4, [6,45,12,41,24,47,26]] = 1
# loc[[2,3],:] = loc[[2,3],:]/100

# def infected(peeps):
#     sz = int(np.sum(peeps[4,:]))
#     inf = np.zeros([5,sz])
#     ind = np.where(peeps[4,:]==1)
#     for i in range(sz):
#         inf[:,i] = peeps[:,ind[0][i]]
#     return inf

# inf = infected(loc)
# print(inf)

# %%
