PAN = float(300)
LECHE = float(3300)
HUEVOS = float(350)

def Compra(P:float, M:float, H:float,) -> float:
    cuenta = PAN*P + LECHE*M + HUEVOS*H
    return cuenta

if __name__ == "__main__":
  P = float(input("cantidad de panes: "))
  M = float(input("cantidad de bosas de leche: "))
  H = float(input("cantidad de huevos: "))
  B = float(input("valor del billete con el que se paga: "))
  vueltas = Compra(P,M,H)

  if (B - vueltas) > 0:
     print("Sus vueltas son " + str(B - vueltas) + " COP")
    
  elif (B - vueltas) < 0:
     print("Quedo debiendo " + str(B - vueltas) + " COP")

  else:
     print("El pago fue excato")

     