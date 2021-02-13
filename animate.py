#%%
from celluloid import Camera
from matplotlib import pyplot as plt
import numpy as np
# %%

fig = plt.figure()
camera = Camera(fig)

loc = (np.random.rand(5, 50) - 1/2)
loc[4,:] = 0
loc[4, 6] = 1
loc[[2,3],:] = loc[[2,3],:]/100
for i in range(60):
    for j in range(50):
        #plotting
        col = 'black'
        if loc[4,j] == 1: col = 'red'
        plt.plot(loc[0,j], loc[1,j], '.' ,color = col)

        #checking velocities
        if np.abs(loc[0,j]) > 0.5:
            loc[2,j] = -loc[2,j]
        if np.abs(loc[1,j]) > 0.5:
            loc[3,j] = -loc[3,j]

    camera.snap()
    mov = (np.random.rand(2, 50) - 1/2)/150
    loc[[2,3],:] = loc[[2,3],:] + mov
    loc[[0,1],:] = loc[[2,3],:] + loc[[0,1],:]

animation = camera.animate()
animation.save('my_animation.gif')

def infected(peeps)
    sz = np.sum(peeps[4,:])
    ret = np.zeroes(5,sz)
    np.where()
    for i in range(50):
        ret[:,sz] = peeps

def check()

# %%
