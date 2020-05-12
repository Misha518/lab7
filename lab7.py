import numpy as np
import matplotlib.pyplot as plt
fig1=plt.figure()

ax1=plt.subplot()
data = np.loadtxt("y.txt")
data1 = np.loadtxt("faza.txt")
ax1.plot(data1[:,0],data1[:,1],lw=2)
ax1.plot(data[:,0],data[:,1],'r.')
ax1.plot(data[:,0],data[:,1],lw=2)




fig2=plt.figure()
ax2=plt.subplot()
data2 = np.loadtxt("y1.txt")
data3 = np.loadtxt("faza.txt")
ax2.plot(data3[:,0],data3[:,1],lw=2)
ax2.plot(data2[:,0],data2[:,1],'r.')
ax2.plot(data2[:,0],data2[:,1],lw=2)


plt.show()
