lista1 = list(range(4,101,4))
print(lista1)

lista2 = ["camion", "auto", "moto", "avion","bicicleta"]
print(lista2[-2])

lista3 = []
lista3.append("mundo")
lista3.append(43)
lista3.append("juego")
print(lista3)

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)


#5) max(numeros) busca el numero mayor de la lista y lo borra

lista4 = list(range(10, 31, 5))
print(lista4[0:2])

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["ram", "ford"]
print(autos)

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)