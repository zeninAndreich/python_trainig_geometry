from geom2d import *
from geom2d.point import Point

l = [Point(i,i*i) for i in range(-5, 6) ]

l = list(map(lambda i : Point(i,i*i), range(-5, 6)))


l2 = list(map(lambda p: Point(p.x, -p.y), l))



print(l2)
print(l)