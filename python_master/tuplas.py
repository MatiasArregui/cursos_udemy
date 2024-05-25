nuestra_tupla = 1, 2, 3, 4, 5, 6, 7
# a, b, c, d = 1, 2, 3, 4
# _, _, _, _, = (1, 2, 3, 4)
a, b, c, d, _, e,*_= nuestra_tupla
print(f"{a} {b} {c} {d} {e}")
g, h, f = nuestra_tupla[2:5]
print(f"{g} {h} {f}")
# a, b, c, d = 0, 0, 0, 0
p, o, i = (1, 2, 3)
