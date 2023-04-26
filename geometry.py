from geom2d import *
from geom2d.point import Point

l = []

for i in range(-5, 6):
    l.append(Point(i,i*i))

l2 = []

for el in l:
    l2.append(Point(el.x, -el.y))

print(l2)
print(l)