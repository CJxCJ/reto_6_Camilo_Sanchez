import math
def Valorprestamo(C:float,i:float,n:float) -> float:
  prestamoFinal = C*(1+(i/100))**n
  return prestamoFinal

if __name__ == "__main__":
  C = float(input("Valor del prestamo adquirido: "))
  i = float(input("Porcentaje del interes: "))
  n = float(input("Meses a los que se saco el prestamo: "))
  valorfinal = Valorprestamo(C,i,n)
  valorfinalimit = "{:.2f}".format(valorfinal)

  print("el valor del prestamo es " + str(valorfinalimit))