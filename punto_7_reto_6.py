import math


def Promedio(v:float,w:float,x:float,y:float,z:float) -> float:
  prom = float(v + w + x + y + z)/5
  return prom


def Mediana(v:float,w:float,x:float,y:float,z:float) -> float:
  medi = [v,w,x,y,z]
  return sorted(medi)[2]

def PromedioMultiplicativo(v:float,w:float,x:float,y:float,z:float) -> float:
  promultiplicativo = (v * w * x * y *z) ** (1/5)
  return promultiplicativo

def Ordenascendente(v:float,w:float,x:float,y:float,z:float) -> float:
  ascen = [v,w,x,y,z]
  return sorted(ascen)
  

def Ordendescendente(v:float,w:float,x:float,y:float,z:float) -> float:
  descen = [v,w,x,y,z]
  return sorted(descen, reverse=True)

def Mayor(v:float,w:float,x:float,y:float,z:float) -> float:
  may = [v,w,x,y,z]
  return sorted(may)[4]

def Menor(v:float,w:float,x:float,y:float,z:float) -> float:
  men = [v,w,x,y,z]
  return sorted(men)[0]

def Potmayorxmenor(v:float,w:float,x:float,y:float,z:float) -> float:
  pot = [v,w,x,y,z]
  return sorted(pot)[4] ** sorted(pot)[0]
  

def Raizcubicamenor(v:float,w:float,x:float,y:float,z:float) -> float:
  cub = [v,w,x,y,z]
  return sorted(cub)[0] ** 1/3





