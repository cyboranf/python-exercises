print(True and False)

print(True and 1)
# ^ to wyrażenie będzie ewaluowane, ale będzie rodzajem maski bitowej

print(True and (2 < 3))

print((2 < 3) and (5 == 7))

a = 5
b = 10

print(a < b and b == a)

print((a < a and a < b) or True)

print(a == a or a < b)

print((a == a or a < b) and (a == a or a == b))

print(not True)

print(not False)

print(not a == b)

print(not a < b)

print(not ((a == a or a < b) and (a == a or a == b)))

print(not not True)