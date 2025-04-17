
#funciones
def imprimir_hola_mundo():
    return print("hola mundo")


nombre = input("nombre: ")
apellido = input("apellido: ")
edad = input("edad: ")
residencia = input("residencia: ")

def saludar_usuario(nombre):
    return print(f"hola {nombre}")

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"soy {nombre} {apellido}, tengo {edad} anios y  vivo en {residencia}")

radio = int(input("radio: "))
def calcular_area_circulo(radio):
    area = 3.14 * radio **2
    return print(area)

segundos = float(input("segundos: "))
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(horas)

numero = int(input("numero: "))
def tabla_multiplicar(numero):
    print(numero * 1)
    print(numero * 2)
    print(numero * 3)
    print(numero * 4)
    print(numero * 5)
    print(numero * 6)
    print(numero * 7)
    print(numero * 8)
    print(numero * 9)
    print(numero * 10)

a=2
b=4
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    return print(suma, resta, multiplicacion, division)

peso = 70
altura = 180
def calcular_imc(peso, altura):
    imc = peso / altura**2
    return print(imc)


celsius = 18
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(fahrenheit)


a = float(input("numero1: "))
b = float(input("numero2: "))
c = float(input("numero3: "))
def calcular_promedio(a, b, c):
    promedio = (a+b+c) / 3
    return print(promedio)

#programa principal

imprimir_hola_mundo()
saludar_usuario(nombre)
informacion_personal(nombre, apellido, edad, residencia)
calcular_area_circulo(radio)
segundos_a_horas(segundos)
tabla_multiplicar(numero)
operaciones_basicas(a,b)
calcular_imc(peso, altura)
celsius_a_fahrenheit(celsius)
calcular_promedio(a, b, c)