from matplotlib import pyplot as plt; # used  to plot graph  
import random # random number generator
from math import dist
import numpy as np

delta = 0.0001

c = []
rows, cols = (3, 4)

for i in range(0,cols):
    A = []
    for j in range(0,rows):
        A.append(0)
    c.append(A)

ep = float(input("Enter epsilon (in J): "))
si = float(input("Enter sigma (in A): "))

# first co-ordinate
c[0][0] = 0
c[0][1] = 0
c[0][2] = 0

# second co-ordinate
x1 = random.uniform(5, 6)

c[1][0] = x1
c[1][1] = 0
c[1][2] = 0

# third co-ordinate
r = random.uniform(5, 6)
t = random.uniform(0, 2)

x2 = r * np.sin(t * np.pi)
y2 = r * np.cos(t * np.pi)

distance = dist([x2,y2],[x1,0])

while distance <= 5 or distance >= 6 :
    r = random.uniform(5, 6)
    t = random.uniform(0, 2)
    x2 = r * np.sin(t * np.pi)
    y2 = r * np.cos(t * np.pi)
    distance = dist([x2,y2],[x1,0])

c[2][0] = x2
c[2][1] = y2
c[2][2] = 0

# fourth co-ordinate
x3 = random.uniform(-1, 6)
y3 = random.uniform(-6, 6)
z3 = random.uniform(0, 6) 

distance1 = dist([x3,y3,z3],[0,0,0])
distance2 = dist([x3,y3,z3],[x1,0,0])
distance3 = dist([x3,y3,z3],[x2,y2,0])

while (distance1 <= 5 or distance1 >= 6) or (distance2 <= 5 or distance2 >= 6) or (distance3 <= 5 or distance3 >= 6):
    x3 = random.uniform(-1, 6)
    y3 = random.uniform(-6, 6)
    z3 = random.uniform(0, 6)
    distance1 = dist([x3,y3,z3],[0,0,0])
    distance2 = dist([x3,y3,z3],[x1,0,0])
    distance3 = dist([x3,y3,z3],[x2,y2,0])

c[3][0] = x3
c[3][1] = y3
c[3][2] = z3 

print(c)

# for i in range(0,4):
#     for j in range(i+1,4):
#         print(dist([c[i][0],c[i][1],c[i][2]], [c[j][0],c[j][1],c[j][2]]))


def potential_energy(c):
    totalEnergy = 0
    for i in range(0,4):
        for j in range(i+1,4):
            r = dist([c[i][0],c[i][1],c[i][2]],[c[j][0],c[j][1],c[j][2]])
            Energy = 4*ep*((si/r)**12 - (si/r)**6)
            totalEnergy += Energy
    return totalEnergy
        
def calculate_gradient(c, i, j):
    gradient = 0
    for p in range(0,4):
        if (p != i) :
            r = dist([c[i][0],c[i][1],c[i][2]],[c[p][0],c[p][1],c[p][2]])
            gradient += ( (6*(si**6)/(r**8)) - (12*(si**12)/(r**14)) ) * (c[i][j] - c[p][j])
    gradient = 4 * ep * gradient
    return gradient

def steepest_gradient_change_pos(c):
    steepest = 0
    cor1 = 0
    cor2 = 0
    for i in range(0, 4):
        for j in range(0, 3):
            grad = calculate_gradient(c, i, j)
            if (abs(grad) > steepest):
                steepest = grad
                cor1 = i
                cor2 = j

    c[cor1][cor2] = c[cor1][cor2] - delta * (grad / abs(grad)) 
    return c

U = []
x = []
for steps in range(1, 100000):
    x.append(steps)
    pot = potential_energy(c)
    U.append(pot)
    c = steepest_gradient_change_pos(c)

plt.plot(x, U)
plt.ylabel("Potential Energy")
plt.xlabel("Number of steps")
plt.show()
plt.savefig("3.2.png")