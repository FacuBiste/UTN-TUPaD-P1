

"""
for i in range(101):
    print(i)


numero = int(input('numero entero: '))
print(numero)

contador = 0
while numero > 0:
    numero = numero // 10
    contador = contador + 1

print(contador)


num1 = int(input('numero1: '))
num2 = int(input('numero2: '))

suma = 0
for i in range(num1 +1, num2):
    suma = suma + i

print(suma)


num = 1
suma = 0
while num != 0:
    num = int(input('numero: '))
    suma = suma + num
    print(suma)



intento = 0
numCorrecto = 8
numero = 0

while numero != numCorrecto:
    intento += 1
    numero = int(input('numero: '))
    print(f'intentos: {intento}')



for i in range(100, 0, -2):
    print(i)



suma = 0
numLimite = int(input('numero limite: '))

for i in range(0, numLimite +1):
    suma += i

print(suma)


numPar = 0
numImpar = 0
numero = 0

for i in range(8):
    numero = int(input('numero: '))
    if numero % 2 == 0:
        numPar +=1
    else:
        numImpar += 1

print(f'numeros pares: {numPar}')
print(f'numero impares: {numImpar}')


numero = 0
promedio = 0
suma = 0
for i in range(3):
    numero = int(input('numero: '))
    suma += numero

promedio = suma / 3
print (promedio)
"""

numero = int(input('numero: '))
numInv = 0
while numero > 0:
    ultDigito = numero % 10
    numInv = numInv * 10 + ultDigito
    numero //= 10   

print(numInv)
