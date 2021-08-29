import matplotlib.pyplot as plt

a = int(input("Enter Starting 1 cordinate"));
b = int(input("Enter Starting 2 cordinate"));
c = int(input("Enter ending 1 cordinate"));
d = int(input("Enter ending 2 cordinate"));
r1 = int(input("Enter ratio 1 of 1st 1/4 cordinate"));
r2 = int(input("Enter ratio 2 of 2nd 1/4 cordinate"));
r11 = int(input("Enter ratio 1 of 1/2 cordinate"));
r12 = int(input("Enter ratio 2 of 1/2 cordinate"));
r21 = int(input("Enter ratio 1 of 1st 1/4 cordinate"));
r22 = int(input("Enter ratio 2 of 2nd 1/4 cordinate"));
X1 = (1 / 4) * (a * r1 + b * r2)
Y1 = (1 / 4) * (c * r1 + d * r2)
print(f'point at (x1,y1) is ({X1},{Y1})')
X2 = (1 / 2) * (a * r11 + b * r12)
Y2 = (1 / 2) * (c * r11 + d * r12)
print(f'point at (x2,y2) is ({X2},{Y2})')
X3 = (1 / 4) * (a * r21 + b * r22)
Y3 = (1 / 4) * (c * r21 + d * r22)
print(f'point at (x3,y3) is ({X1},{Y1})')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.scatter([a, X1, X2, X3, c], [b, Y1, Y2, Y3, d], color='k')
plt.text(a, b + 0.5, '({},{})'.format(a, b))
plt.text(c, d + 0.5, '({},{})'.format(c, d))
plt.text(X1, Y1 + 0.5, '({},{})'.format(X1, Y1))
plt.text(X2, Y2 + 0.5, '({},{})'.format(X2, Y2))
plt.text(X3, Y3 + 0.5, '({},{})'.format(X3, Y3))
plt.plot([a, X1, X2, X3, c], [b, Y1, Y2, Y3, d])
plt.show()
