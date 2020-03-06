import re
escrito = input ( 'Escriba algo: ')

x = escrito.split(' ')
n= len(x)
print(x)
print(n)
for i in range (n):

      try:
          a=int (x[i])
          print("Es entero ",a)
      except:

        try:

          a=float (x[i])
          print("Es flotante ",a)
        except:

          try:
            a = str(x[i])


            if len(a)==1:
              print ("Es Char",a)
            else:
              print("Es str ",a)

          except:
              print("")