# Uwaga, w języku Python istnieją operatory & i |, jednak działają one na bitach

a = 5
b = 10

print(a & b)  # binarnie 0101 & 1010 co daje 0000

print(a | b)  # binarnie 0101 | 1010 co daje 1111

print(~a)  # zanegowano wszystkie bity, w tym bit znaku, stąd zmiana znaku

print(~a & 255)  # tutaj zastosowano maskę, którą usunęła efekt negacji znaku
#      oraz jednocześnie zareprezentowała liczbę w obrębie jednego bajta

print(a ^ b)

print(a << 1) # 101 -> 1010

print(a << 2) # 101 -> 10100

print(a >> 1) # 101 -> 10

print(a >> 2) # 101 -> 1
