import math

POLLITOS = float(1)
GALLINAS = float(6)
GALLOS = float(7)

def Carnetotal(N:float, M:float, K:float) -> float:
  pesocarne = GALLINAS*N + GALLOS*M + POLLITOS*K
  return pesocarne

if __name__ == "__main__":
  N = float(input("cantidad de gallinas: "))
  M = float(input("cantidad de gallos: "))
  K = float(input("cantidad de pollos: "))   
  pesototal  = Carnetotal(N,M,K)

  print("el peso total de las carnes es: " + str(pesototal) + " KG")