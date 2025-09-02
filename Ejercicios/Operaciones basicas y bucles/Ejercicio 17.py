#Autor: Sergio Gabriel Chaves Mosquera

#Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.
numero = 0
for cuadrado in range (1, 101):
    numero = numero + cuadrado ** 2
    print(numero)
    
    