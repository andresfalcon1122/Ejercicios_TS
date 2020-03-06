import numpy as np

print ('Que operacion desea hacer?')
print ('a) sumar')
print ('b) divide')
print ('c) multiplica')

opcion = input ( 'eliga opcion: ')


def suma():
    a = int(input("insertar primer numero: "))
    b = int(input("insertar segundo numero: "))

    c = (a + b)
    print(c)
    return


def divide():
    a = int(input("insertar primer numero: "))
    b = int(input("insertar segundo numero: "))

    c = (a / b)
    print(c)
    return

def multiplica():
    a = int(input("insertar primer numero: "))
    b = int(input("insertar segundo numero: "))

    c = (a * b)
    print(c)
    return

if (opcion == "a"):
         suma()
if (opcion == "b"):
         divide()
if (opcion == "c"):
         multiplica()






