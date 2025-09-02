#Autor: Sergio Gabriel Chaves Mosquera

#Escribir un programa que imprima por pantalla los cuadrados de los 30 primeros números naturales.

numero = 1
for numero in range (1, 31):
    print(numero, "x", numero, "=", numero**2)
    numero +=1