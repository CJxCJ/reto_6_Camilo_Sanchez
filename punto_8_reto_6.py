from punto_7_reto_6 import *


if __name__ == "__main__":
  v = float(input("ingrese el primer numero: "))
  w = float(input("ingrese el segundo numero: "))
  x = float(input("ingrese el tercer numero: "))
  y = float(input("ingrese el cuarto numero: "))
  z = float(input("ingrese el quinto numero: "))

  a = Promedio(v,w,x,y,z)
  b = Mediana(v,w,x,y,z)
  c = PromedioMultiplicativo(v,w,x,y,z)
  d = Ordenascendente(v,w,x,y,z)
  e = Ordendescendente(v,w,x,y,z)
  f = Mayor(v,w,x,y,z)
  g = Menor(v,w,x,y,z)
  h = Potmayorxmenor(v,w,x,y,z)
  i = Raizcubicamenor(v,w,x,y,z)
  
  print("El promedio es: " + str(a))
  print("Ea mediana es: " + str(b))
  print("El promnedio multiplicativo es : " + str(c))
  print("El orden ascendete es: " + str(d))
  print("El orden descendete es: " + str(e))
  print("El mayor numero de los ingresados es: " + str(f))
  print("El menor numero de los ingresados es: " + str(g))
  print("El numero mayor elevado al menor es: " + str(h))
  print("La raiz cubica del menor es: " + str(i))