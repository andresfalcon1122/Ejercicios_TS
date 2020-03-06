import numpy as np
while True:
   print ('\nQue operacion desea hacer?\n')
   print ('s) Salir\n')
   print ('a) Sumar')
   print ('b) Dividir')
   print ('c) Multiplicar\n')

   opcion = input ( 'Eliga opcion: ')


   class sumas:
      def suma(self):
          print("Elegiste Sumar\n")
          a = int(input("insertar primer numero: "))
          b = int(input("insertar segundo numero: "))
          c = (a + b)
          print("\nResultado =",c)
          return

   class divides:
      def divide(self):
          print("Elegiste Dividir\n")

          a = int(input("insertar primer numero: "))
          b = int(input("insertar segundo numero: "))
          if b !=0:
             c = (a / b)
             print("\nResultado =",c)
          else:
             print("error, no se puede dividir  entre 0")
          return
   class multiplicas:
      def multiplica(self):
          print("Elegiste Multiplicar\n")
          a = int(input("insertar primer numero: "))
          b = int(input("insertar segundo numero: "))

          c = (a * b)
          print("\nResultado =",c)
          return

   sumar = sumas()
   dividir = divides()
   multiplicar = multiplicas()

   if (opcion == "a"):
         sumar.suma()
   if (opcion == "b"):
         dividir.divide()
   if (opcion == "c"):
         multiplicar.multiplica()
   if (opcion == "s"):
         break
   else:
      print("\n*****Elige la opción correcta*****\n")