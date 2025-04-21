from math import pi

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


frutas = list(precios_frutas.keys())
print(frutas)

class Persona():
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
    

Persona1 = Persona('facu', 'Argentina', '23')
Persona2 = Persona('Marcos', 'Espa;a', '89')

Persona.saludar(Persona1)
Persona.saludar(Persona2)

class Circulo():
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        print(pi * self.radio **2)

    def calcular_perimetro(self):
        print(2 * pi * self.radio)

Circulo1 = Circulo(5)

Circulo.calcular_perimetro(Circulo1)
Circulo.calcular_area(Circulo1)
print("")
print("")


def esta_balanceado(string):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in string:
        if caracter in "({[":
            pila.append(caracter)
        elif caracter in ")}]":
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    
    return len(pila) == 0


string = "[{()()()]}]"
if esta_balanceado(string):
    print("balanceado")
else:
    print("no balanceado")

print("")
print("")
print("")


cola =[]

def agregar_cliente(nombre):
    cola.append(nombre)
    print(f"cliente {nombre} agregado")

def atender_cliente():
    if cola:
        cliente = cola.pop(0)
        print(f"atendiendo al cliente: {cliente}")
    else:
        print("no hay cliente en cola")

def sig_cliente():
    if cola:
        print(f"sieguiente cliente en la fila: {cola[0]}")
    else:
        print("no hay clientees en espera")



agregar_cliente("Manuel")
agregar_cliente("Luisana")
agregar_cliente("Juan")

sig_cliente()
print(cola)

atender_cliente()
sig_cliente()

atender_cliente()
atender_cliente()
atender_cliente()

print("")
print("")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    

class lista_enlazada:
    def __init__(self):
        self.primero = None

    def poner_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def mostrar(self):
        actual = self.primero
        while actual:
            print(actual.valor)
            actual = actual.siguiente
    
    def invertir(self):
        anterior = None
        actual = self.primero

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        
        self.primero = anterior

lista = lista_enlazada()
lista.poner_inicio(1)
lista.poner_inicio(2)
lista.poner_inicio(3)
lista.poner_inicio(4)

print("elementos de lista")
lista.mostrar()

lista.invertir()
print("invertido: ")
lista.mostrar()