

def typechecker(var):
    if isinstance(var, str):
        print ("Variable is a string", var)
        return
    elif isinstance(var, int):
        print ("Variable is an integer", var)
        return
    elif isinstance(var, float):
        print ("Variable is a float", var)
        return
    elif isinstance(var, chr):

        print ("Variable is a chara", var)
        return

try:
    getInput=input("escribe algo: ")
    typechecker(getInput)
except ValueError:
  print("An exception occurred")
