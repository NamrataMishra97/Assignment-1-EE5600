import matplotlib.pyplot as plt
import numpy as  np
# X vector contain X1,X2
X=np.array([-6,8])
# Y vector contain Y1,Y2
Y=np.array([8,-6])
m=1
n=3
c= float(m/(m+n))
d= float(n/(m+n))

a_arr=c*np.array([-6,8])
b_arr=d*np.array([8,-6])
out_arr= (a_arr + b_arr)
print(out_arr)
r=1
s=1
p= float(r/(r+s))
q= float(s/(r+s))
e_arr=p*np.array([-6,8])
f_arr=q*np.array([8,-6])
out_arr=(e_arr + f_arr)
print(out_arr)
u=3
v=1
i= float(u/(u+v))
j= float(v/(u+v))
k_arr=i*np.array([-6,8])
l_arr=j*np.array([8,-6])
out_arr= (k_arr + l_arr)
print(out_arr)


X=([-6,-2.5,1,4.5,8])
Y=([8,4.5,1,-2.5,-6])
plt.plot(X,Y,color='blue',marker='o')
# plt.scatter(a_arr,e_arr,k_arr)
# plt.scatter(b_arr,f_arr,l_arr)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
for i,j in zip(X,Y):
    plt.text(i,j+0.5,'({},{})'.format(i,j))
plt.grid()
plt.show()
