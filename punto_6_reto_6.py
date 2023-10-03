def Contagios(C:float,D:float) -> float:
  nuevosContagios = C*(2**(D-1))
  return nuevosContagios

if __name__ == "__main__":
  C = float(input("Numero de contagiados actuales: "))
  D = float(input("Dias transcurridos: "))
  contagiosfinal = Contagios(C,D)

  print("el numero de contagiados en " + str(D) + " dias es de " + str(contagiosfinal))