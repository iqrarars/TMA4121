import numpy as np
import matplotlib.pyplot as plt

lengde = 100 
steg = 1000
alpha = 0.5

delta_h = 2
delta_t = (delta_h ** 2) / 2
gamma = delta_h / (delta_t ** 2)

u_initial = 0.0

u = np.zeros((steg, lengde, lengde))  # Initialize the 3D array with the correct shape
u_top = 100
u_left = 0
u_right = 0
u_bottom = 0 

# Apply boundary conditions
u[:, 0, :] = u_top
u[:, -1, :] = u_bottom
u[:, :, 0] = u_left
u[:, :, -1] = u_right

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u[0], cmap=plt.cm.jet, shading='auto', vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Solve the heat equation iteratively and update the plot
for t in range(0, steg-1):  # Time steps
    for j in range(1, lengde-1):  # Spatial points (rows)
        for k in range(1, lengde-1):  # Spatial points (columns)
            u_xx = (u[t, j+1, k] - 2*u[t, j, k] + u[t, j-1, k]) / delta_h**2
            u_yy = (u[t, j, k+1] - 2*u[t, j, k] + u[t, j, k-1]) / delta_h**2
            u[t+1, j, k] = alpha * (u_xx + u_yy) * delta_t + u[t, j, k]

    pcm.set_array(u[t].flatten())  # Update color mesh with new temperature values
    plt.pause(0.001)  # Pause to display the plot

plt.show()