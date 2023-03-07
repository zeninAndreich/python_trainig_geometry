from math import sqrt


def solve (a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print("Решений нет")
    elif d == 0:
        x = -b / (2*a)
        print("Первое решение " + str(x))
    else:
        x1= (-b + sqrt(d))/(2*a)
        x2= (-b - sqrt(d))/(2*a)
        print("Второе решение " + str(x1) + " И " + str(x2))

solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)