from geom2d import *
from geom2d.point import Point

l = []

for i in range(-5, 6):
    l.append(Point(i,i*i))

print(l)