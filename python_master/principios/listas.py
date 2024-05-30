lista = [1, 2, 3, 4, 56, "Argentina", 2, 3, 4]
#Indices 0  1  2  3  4      5      6  7  8
lista[1]= 58
# print(lista)
lista_2 = [1, 2, 3, 4, ["a", "b", "c", [1, 2, 3]], "fin"]
# print(lista_2[4][3][1])
lista_tridimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for x in range(3):
    for y in range(3):
        print(f"{lista_tridimensional[x][y]}", end=" ")
    else:
        print("")

a = [1, 2, 3]
a = a + [4, 5, 6]
print(a)
a = a + list("abc")
print(a)
b = [1, 2, 3, 4]
b.insert(0,0)
print(b)