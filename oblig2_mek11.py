# bruker kode fra Appendiks A:
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt 

# Dette virker med versjon 7 MAT-filer

data = sio.loadmat('data.mat')
x = data.get('x')       # matrise X
y = data.get('y')       # martise Y
u = data.get('u')       # matrise U
v = data.get('v')       # matrise V
xit = data.get('xit')   # vektor XIT
yit = data.get('yit')   # vektor YIT

velocity_array= np.sqrt(u**2+v**2) # beregner hastigheten


# cmap = cm.winter is just a particular colour gradient 
plt.contourf(x,y,velocity_array)

# plotting interface between water and air
# (35,160), (70, 170)
#plt.quiver(x[34:69,159:169],y[34:69,159:169],velocity_array[34:69,159:169])
#plt.quiver(x[34:69,84:99],y[34:69,84:99],velocity_array[34:69,84:99])
#plt.quiver(x[34:69,49:59],y[34:69,49:59],velocity_array[34:69,49:59])
plt.show()  

