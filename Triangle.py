import math

a = float(input("Length of first side: "))
b = float(input("Length of second side: "))
c = float(input("Length of third side: "))

s = (a + b + c) / 2

heron = s * (s - a) * (s - b) * (s - c)
print(math.sqrt(heron))
