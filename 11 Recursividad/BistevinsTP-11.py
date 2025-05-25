
def factorial(num):
    if num == 0:
        return 1
    else:
        return num* factorial(num-1)

num = int(input("numero: "))

for i in range(1, num +1):
    print(f"{i} = {factorial(i)}")





def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num -2)

max = int(input("maximo fibonacci: "))

for i in range(max + 1):
    print(f"{i} = {fibonacci(i)}")


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)

base = int(input("base: "))
exponente = int(input("exponente: "))

resultado = potencia(base, exponente)
print(f"{base} ** {exponente} es: {resultado}")




def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
    

num = int(input("numero: "))
binario = decimal_a_binario(num)
print(f"{num} en binario es: {binario}")


def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return palindromo(palabra[1:-1])


palabra = input('palabra: ')
if palindromo(palabra):
    print(f"{palabra}, es palindromo")
else:
    print(f"{palabra},no es palindromo")
    

def sumaDigitos(num):
    if num < 10:
        return num
    
    return (num% 10) + sumaDigitos(num // 10)
num = int(input('numero: '))
print(sumaDigitos(num))


def piramide(num):
    if num == 1:
        return 1
    
    return num + piramide(num -1)


num = int(input('numero: '))
print(piramide(num))


def contar(numero, digito):
    if numero == 0:
        return 0
    
    if numero % 10 == digito:
        return 1 + contar(numero // 10, digito)
    else:
        return contar(numero // 10, digito)

numero = int(input('numero: '))
digito = int(input('digito: '))
print(contar(numero, digito))