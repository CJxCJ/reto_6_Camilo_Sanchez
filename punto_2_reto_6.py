import math

def Areacirculo(r:float) -> float:
  arcirculo = math.pi*(r**2) 
  return  arcirculo

def Perimetrocirculo(r:float) -> float:
  percirculo = (math.pi*2)*r
  return percirculo

def Perimetrorectangulo(a:float, b:float) -> float:
  perrectangulo = (a*2)+(b*2)
  return perrectangulo

def Arearectangulo(a:float,b:float) -> float:
  arrectangulo = a*b
  return arrectangulo

def Areatotal(a:float,b:float,r:float) -> float:
  aretotal = (a*b)+(math.pi*(r**2))
  return aretotal

def Perimetrototal(a:float,b:float,r:float) -> float:
  peritotal = ((math.pi*2)*r)+(a*2)+(b*2)
  return peritotal


if __name__ == "__main__":
  a = float(input("lado del rectangulo: "))
  b = float(input("base del rectangulo: "))
  r = float(input("radio del circulo: "))
  perimetroR = Perimetrorectangulo(a,b)
  areaR = Arearectangulo(a,b)
  perimetroC = Perimetrocirculo(r)
  areaC = Areacirculo(r)
  perimetroT = Perimetrototal(a,b,r)
  areaT = Areatotal(a,b,r)


  print("El area del circulo es: " + str(areaC))
  print("El perimetro del circulo es: " + str(perimetroC))
  print("El area del rectangulo es: " + str(areaR))
  print("El perimetro del rectangulo es: " + str(perimetroR))
  print("El area del total es: " + str(areaT))
  print("El perimetro del total es: " + str(perimetroT))
  