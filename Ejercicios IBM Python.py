print("Hello World")       #No se pone >>> por ser un lenguaje interpretado
"""Con help() poniendo dentro la función o elemento que se quiera se obtiene más info.
...Ponerla vacía También sirve para info general y recursos
"""
def descomponer_en_factores(numerox):
    factores = []
    divisor = 2
    while numerox > 1:
        while numerox % divisor == 0:
            factores.append(divisor)
            numerox //= divisor
        divisor += 1
    return factores

# Ejemplo de uso
numerox = 84
print("Factores de", numerox, ":", descomponer_en_factores(numerox))

# Dados dos números, escriba un código Python para encontrar el mínimo de estos números.
a = 2
b = 4
def f1_dar_el_menor(): 
    if a<b:
        print (a)
    elif a==b:
        print ("los números son iguales")
    else: print (b)
f1_dar_el_menor()
a = -1
b = -4
f1_dar_el_menor()

# Invertir palabras de una cadena dada
str = "código de práctica de prueba de geeks"
lista1 = str.split()   #Se separa cada palabra con split(). Al no indicar separador usa el espacio. 
lista1.reverse()
print (lista1)

# Realizar una suma de los elementos de una tupla
tupla1 = (7, 8, 9, 1, 10, 7)
suma = sum(tupla1)
print ("La suma de los elementos de la tupla es", suma)

#Escribe un código que sume los elementos de una lista de números proporcionados
def suma_numeros_dados():
    listapedida = input ("Escribe una lista de números: ")
    lista_en_int = [int(listapedida) for listapedida in listapedida.split()]  #Con [] se crea una nueva lista que se almacena en lista_en_int. Con X.split() se separa la cadena srt en subcadenas de str, según el separador que se indique ["1", "2", etc]. 
    suma2 = sum(lista_en_int)                                                   #Con for in se itera en cada elemento de la lista hecha con split, con cada iteración listapedida coge uno de los valores de cada elemetno de la lista. Con int se pasa a número entero cada elemento de listapedida. 
    print ("La suma de los elementos de la lista es", suma2)
suma_numeros_dados()

#Escribe un código que desordene al azar una lista
lista2 = ["patata", "cebolla", "boniato", "berenjena", "pimiento"]
def desordenar_lista(): 
    import random   #Hay que importar el módulo random para usarlo en la siguiente línea
    lista_random = random.sample(lista2, len(lista2))  #Crea una lista donde se almacena la aleatorización de los elementos de lista2, usando len() para que abraque todos los elementos de la lista. 
    print (lista_random)
desordenar_lista()

#Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.
archivo = input("Escribe la dirección de un archivo al que contar el número de Mayúsculas: ")
with open(archivo, 'r') as fh:   #abre el archivo especificado por la variable archivo en modo lectura ('r'). Utilizar with asegura que el archivo se cierre correctamente después de su uso. Dentro de este bloque with, el archivo se referencia con el nombre fh
    count = 0   #se inicializa la variable count con el valor 0. Esta variable se utilizará para contar el número de caracteres en mayúsculas.
    text = fh.read()    #lee todo el contenido del archivo (fh) y lo almacena en la variable text como una cadena de caracteres.
    for character in text:  #Se inicia un bucle for que itera sobre cada caracter de la cadena text.
        if character.isupper():   # En cada iteración, se verifica si el caracter actual (character) es una letra mayúscula utilizando el método isupper() de las cadenas en Python. Si el caracter es una letra mayúscula, la condición se evalúa como verdadera.
            count += 1  #Si el caracter es una letra mayúscula, se incrementa el contador count en 1.
print("El número de mayúsculas en el archivo es", count)

#Escriba un programa para producir la serie Fibonacci en Python. Es decir, cadena de números que sume los dos anteriores. 
def calculo_fibonacci(): 
    num1 = 0
    num2 = 1
    lista_fibonacci = [num1, num2]
    while num2<500:
        suma1y2 = num1 + num2
        lista_fibonacci.append(suma1y2)
        num1 = num2
        num2 = suma1y2
    print(lista_fibonacci)
calculo_fibonacci()

#Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.
is_num_capicua = input("introduzca un número a comprobar si es capicúa: ")
b = is_num_capicua[::-1]
if b == is_num_capicua:
    print (is_num_capicua, "es capicúa")
else: 
    print (is_num_capicua, "no es capicúa")

#Ejemplo de código para errores. 
try: 
    if "1" != 1: 
        raise ValueError("algún error")
    else: 
        print("no se ha producido ningún error")
except ValueError: 
    print("Se ha producido algún error")