def suma (a, b, c):
  return a + b

def resta (a, b):
  return a - b   

def multiplicacion (a, b):
   return a * b 

def division (a, b):
  if b !=0:
    return a/b
  else:
    raise ValueError("No se puede dividir por cero")