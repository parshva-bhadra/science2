import math

ep = float(input("Enter epsilon: "))
si = float(input("Enter sigma: "))

x = []
y = []
z = []

x1 = float(input("Enter x co-ordinates of 1st particle: "))
y1 = float(input("Enter y co-ordinates of 1st particle: "))
z1 = float(input("Enter z co-ordinates of 1st particle: "))

x2 = float(input("Enter x co-ordinates of 2nd particle: "))
y2 = float(input("Enter y co-ordinates of 2nd particle: "))
z2 = float(input("Enter z co-ordinates of 2nd particle: "))

x.append(x1)
x.append(x2)

y.append(y1)
y.append(y2)

z.append(z1)
z.append(z2)


r = math.sqrt((x[0]-x[1])**2+(y[0]-y[1])**2+(z[0]-z[1])**2)
Energy = 4*ep*((si/r)**12 - (si/r)**6)
print(f"Interaction energy between the particles is: {Energy}")