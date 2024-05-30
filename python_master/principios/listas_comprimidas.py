from random import randint

lista_1 = [randint(0,999) for x in range(20)]
lista_2 = [x for x in range(1,20) if x % 2 == 0]
print(sorted(lista_1))
lista_2.append(1)
lista_2.sort()
print(lista_2)
lista_prueba = [1, "matias", 25, "cordoba"]
lista_3 = [{"id":x, "name":x, "edad":x, "provincia":x} for x in lista_prueba]
print(lista_3)