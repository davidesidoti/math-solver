import math

a = int(input("A -> "))
b = int(input("B -> "))
c = int(input("C -> "))

delta = ((b ** 2) - 4 * a * c)

x1 = ((b + math.sqrt(delta)) / (2 * a))
x2 = ((b - math.sqrt(delta)) / (2 * a))
print(x2)
