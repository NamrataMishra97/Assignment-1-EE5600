import matplotlib.pyplot as plt
import numpy as  np
# X vector contain X1,X2
X=np.array([-6,8])
# Y vector contain Y1,Y2
Y=np.array([8,-6])
m=3
n=1
c= float(m/(m+n))
d= float(n/(m+n))
a_arr=c*np.array([-6,8])
b_arr=d*np.array([8,-6])
out_arr= np.add(a_arr, b_arr)
print(out_arr)
print(a_arr)
r=1
s=1
p= float(r/(r+s))
q= float(s/(r+s))
e_arr=p*np.array([-6,8])
f_arr=q*np.array([8,-6])
out_arr= np.add(e_arr, f_arr)
print(out_arr)
u=1
v=3
i= float(u/(u+v))
j= float(v/(u+v))
k_arr=i*np.array([-6,8])
l_arr=j*np.array([8,-6])
out_arr= np.add(k_arr, l_arr)
print(out_arr)



X=([-6,-2.5,1,4.5,8])
Y=([8,4.5,1,-2.5,-6])
plt.plot(X,Y,color='green',marker='o')
# plt.scatter(a_arr,e_arr,k_arr)
# plt.scatter(b_arr,f_arr,l_arr)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()
