# bruker kode fra Appendiks A:
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib
# Dette virker med versjon 7 MAT-filer

data = sio.loadmat('data.mat')
x = data.get('x')       # matrise X
y = data.get('y')       # martise Y
u = data.get('u')       # matrise U
v = data.get('v')       # matrise V
xit = data.get('xit')   # vektor XIT
yit = data.get('yit')   # vektor YIT

#print(y[100,0])
print(u, len(v[:,0]))    

# zero matrix with same shape as 
# vel_field = np.matlib.zeros((194,201))


