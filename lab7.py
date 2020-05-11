import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 2.5, 0.1)
y = -x*np.exp(-x)+np.exp(-x)
y1 = -x*np.exp(-x)+np.exp(-x)+0.5
y2 = -x*np.exp(-x)+np.exp(-x)+0.1
y3 = -x*np.exp(-x)+np.exp(-x)+0.2
y4 = -x*np.exp(-x)+np.exp(-x)+0.3
y5 = -x*np.exp(-x)+np.exp(-x)+0.4
fig1=plt.figure()
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
ax1=plt.subplot()
data = np.loadtxt("y.txt")
ax1.plot(data[:,0],data[:,1],'r.')
ax1.plot(data[:,0],data[:,1],lw=2)



x1 = np.arange(0, 2.5, 0.1)
y11 = x*np.exp(-x)+0.2*x+0.2
y22 = x*np.exp(-x)+0.3*x+0.3
y33 = x*np.exp(-x)+0.4*x+0.4
y44 = x*np.exp(-x)+0.6*x+0.6
y55 = x*np.exp(-x)+0.1*x+0.1
fig2=plt.figure()
plt.plot(x1, y11)
plt.plot(x1, y22)
plt.plot(x1, y33)
plt.plot(x1, y44)
plt.plot(x1, y55)
ax2=plt.subplot()
data2 = np.loadtxt("y1.txt")
ax2.plot(data2[:,0],data2[:,1],'r.')
ax2.plot(data2[:,0],data2[:,1],lw=2)


plt.show()