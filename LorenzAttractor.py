import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

T = 40.0
inct = 0.01

rho = 28.0
sigma = 10.0
beta = 8.0/3.0

def dFun(state,t):
	x, y, z = state
	return sigma*(y-x),x*(rho-z)-y,x*y-beta*z

state0 = [1.0,1.0,1.0]
t = np.arange(0.0,T,inct)

states = odeint(dFun,state0,t)

# # Steady plot
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(states[:,0],states[:,1],states[:,2])
# plt.show()

# Transient plot
fig = plt.figure()
ax = fig.gca(projection='3d')
fig.show()
for it,i in enumerate(t):
 	ax.clear()
 	ax.plot(states[0:it,0],states[0:it,1],states[0:it,2])
 	plt.pause(inct)
plt.close()

