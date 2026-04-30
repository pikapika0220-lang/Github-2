def ft_to_cm(f, i):
    return f*30.48 + i*30.48/12#1 フィート = 12 インチ = 30.48 cm
assert round(ft_to_cm(5, 2) - 157.48, 6) == 0 #

import math

def qe_disc(a, b, c):
    return b**2 - 4*a*c

def qe_solution1(a, b, c):
    return (-b + math.sqrt(qe_disc(a, b, c)))/(2*a)

def qe_solution2(a, b, c):
    return (-b - math.sqrt(qe_disc(a, b, c)))/(2*a)

a = float(input("aの値"))
b = float(input("bの値"))
c = float(input("cの値"))

print(f'方程式の答え: {qe_solution1(a, b, c)},{qe_solution2(a, b, c)}')

