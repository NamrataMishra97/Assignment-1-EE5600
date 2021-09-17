
import numpy as np
import matplotlib.pyplot as plt

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Line Plot
A = np.array([-6,8])
B = np.array([8,-6])
D=(1/(1+3))*(np.column_stack((B,A))@np.array([1,3]).T)
E=(1/(1+1))*(np.column_stack((B,A))@np.array([1,1]).T)
F=(1/(3+1))*(np.column_stack((B,A))@np.array([3,1]).T)
print(D,E,F)
#Generating all lines
x_AD = line_gen(A,D)
x_DE = line_gen(D,E)
x_EF = line_gen(E,F)
x_FB = line_gen(F,B)

#Plotting all lines
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
plt.plot(x_FB[0,:],x_FB[1,:],label='$FB$')
plt.plot(A[0], A[1], 'm')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.03) , 'A')
plt.plot(B[0], B[1], 'm')
plt.text(B[0] * (1 - 0.021), B[1] * (1+0.03) , 'B')
plt.plot(D[0], D[1], 'm')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'm')
plt.text(E[0] * (1 - 0.2), E[1] * (1 - 0.4) , 'E')
plt.plot(F[0], F[1], 'm')
plt.text(F[0] * (1 -0.1), F[1] * (1 + 0.1) , 'F')
#plt.text(1.0,0.08,'l')
#plt.text(3.0, 0.08, 'k')
#plt.text(1.8, 0.75, 'm')
#plt.text(1.7, 2.59, 'k+l')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()







