from matplotlib import pyplot as plt; # used  to plot graph  
import random # random number generator
from mpl_toolkits import mplot3d
from math import dist
import numpy as np

xc = []
yc = []
zc = []

# first co-ordinate
xc.append(0)
yc.append(0)
zc.append(0)

# second co-ordinate
x1 = random.uniform(5, 6)

xc.append(x1)
yc.append(0)
zc.append(0)

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

xc.append(x2)
yc.append(y2)
zc.append(0)

# third co-ordinate

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

xc.append(x3)
yc.append(y3)
zc.append(z3)

print(xc)
print(yc)
print(zc)

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.scatter(xc, yc, zc) 
ax.set_title('3d Scatter plot')
plt.show()