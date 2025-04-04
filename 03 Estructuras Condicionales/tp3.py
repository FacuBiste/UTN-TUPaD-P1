from statistics import mode, median, mean
import random
'''

edad = float(input('edad: '))

if edad >= 18:
    print('mayor de edad')
else:
    print('no es mayor de edad')


nota = float(input('nota: '))

if nota >= 6:
    print('aprobado')
else:
    print('desaprobado')


numero = float(input('numero par: '))

if numero % 2 == 0:
    print('es par')
else:
    print('no es par')


edad = float(input('edad: '))

if edad < 12:
    print('ninio')
elif edad >= 12 and edad < 18:
    print('adolecente')
elif edad >= 18 and edad < 30:
    print("adulto joven")
else:
    print("adulto")


contra = input('contra: ')

if len(contra) >= 8 and len(contra) <= 14:
    print('ha ingresado una contrasena correcta')
else:
    print('ingrese contrasena de entre 8 y 14 caracteres')



numerosAleatorios = [random.randint(1, 100) for i in range (50)]

print (numerosAleatorios)
mean = mean(numerosAleatorios)
mode = mode(numerosAleatorios)
median = median(numerosAleatorios)

print(mode)
print(median)
print (mean)



palabra = input('palabra: ')

if palabra.endswith(("a", "e", "i", "o", "u")):
    print(palabra + " !")
else:
    print(palabra)



nombre = input('nombre :')
numero = float(input('numero: '))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())

'''

magnitud = float(input('magnitud: '))

if magnitud < 3:
    print('muy leve')
elif magnitud >= 3 and magnitud < 4:
    print('leve')
elif magnitud >= 4 and magnitud < 5:
    print("moderado")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("muy fuerte")
elif magnitud >= 7:
    print("extremo")

hemisferio = input('hemisferio: ')
mes = float(input('mes: '))
dia = float(input('dia: '))
if hemisferio == 'norte':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('invierno')
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('primavera')
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('verano')
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print('otonio')

elif hemisferio == 'sur':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print('verano')
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print('otonio')
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print('invierno')
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print('primavera')