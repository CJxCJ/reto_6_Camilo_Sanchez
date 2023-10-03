import math 



def Volumenesfera(r1:float) -> float:
  volesfera = (4/3)*math.pi*(r1**3) 
  return  volesfera

def Areaesfera(r1:float) -> float:
  aresfera = 4*math.pi*(r1**2) 
  return  aresfera

def Volumencono(r2:float, h:float) -> float:
  volcono = (math.pi*(r2**2)*h)/3
  return  volcono

def Areacono(r2:float, h:float) -> float:
  arcono = ((math.pi*r2)*(math.sqrt(h**2+r2**2))+math.pi*(r2**2))
  return  arcono

def Volumentotal(r1:float, r2:float, h:float) -> float:
  voltotal = ((4/3)*math.pi*(r1**3)) + ((math.pi*(r2**2)*h)/3)
  return  voltotal 

def Areatotal(r1:float, r2:float, h:float) -> float:
  artotal = ((math.pi*r2)*(math.sqrt(h**2+r2**2))+math.pi*(r2**2)) + 4*math.pi*(r1**2) 
  return  artotal 


if __name__ == "__main__":
  r1 = float(input("radio de la esfera: "))
  r2 = float(input("radio del cono: "))
  h = float(input("altura del cono: "))
  volumenE = Volumenesfera(r1)
  areaE = Areaesfera(r1)
  volumenC = Volumencono(r2,h)
  areaC = Areacono(r2,h)
  volumenT = Volumentotal(r1,r2,h)
  areaT = Areatotal(r1,r2,h)


  print("El volumen de la esfera es: " + str(volumenE))
  print("El area de la esfera es: " + str(areaE))
  print("El volumen del cono es: " + str(volumenC))
  print("El area del cono es: " + str(areaC))
  print("El volumen del cono y la efera juntos es: " + str(volumenT))
  print("El area del cono y la efera juntos es: " + str(areaT))