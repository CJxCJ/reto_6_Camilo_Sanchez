# Reto 6 Camilo Sanchez

## Los codigos tambien estan adjuntos como archivo con el trabajo.

## Punto 1
Realizar una funcion para encontrar areas y volmen de un cono y una esfera

````python
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
````

## Punto 2
Realizar un codigo para encontrar area y perimetro de un rectangulo y 2 circulos:

````python
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
````

## Punto 3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

````python
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
````

## Punto 4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

````python
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
````

## Punto 5
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

````python
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
````

## Punto 6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

````python
def Contagios(C:float,D:float) -> float:
  nuevosContagios = C*(2**(D-1))
  return nuevosContagios

if __name__ == "__main__":
  C = float(input("Numero de contagiados actuales: "))
  D = float(input("Dias transcurridos: "))
  contagiosfinal = Contagios(C,D)

  print("el numero de contagiados en " + str(D) + " dias es de " + str(contagiosfinal))
````

## Punto 7
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  - El promedio
  - La mediana 
  - El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  - Ordenar los números de forma ascendente
  - Ordenar los números de forma descendente
  - La potencia del mayor número elevado al menor número
  - La raíz cúbica del menor número

````python
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

````

## Punto 8
Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

````python
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
````

## Punto 9

pip (Package installer for Python) es una herramienta que viene instalada por defecto cuando se descarga e instala el interprete de python en el sistema. Se utiliza mediante el comandos los cuales son utiles, estos se pueden llamar desde la consola o terminal escribiendo "pip" se enfoca para instalar bibliotecas de codigo abierto para su uso y prporcionar mas herramientas al momento de desarrolar codigo, ademas de sus comandos mayormente estan enfocados en la admisnitracion y manejo de paquetes instalados en el sistema, esto con el fin de poder ordenarlos, conocerlos y utilizarlos de manera eficiente.


## Punto 10

- request: El módulo Requests se utiliza para enviar todo tipo de peticiones HTTP al servidor. Permite enviar peticiones HTTP. Se instala mediante el comando "pip install requests" 



- Numpy: Nos permite trabajar con arrays multidimensionales. La implementación de arrays no existe en Python. Principalmente los desarrolladores utilizan numpy en sus proyectos de aprendizaje automático. Se instala mediante el comando "pip install numpy"


- Pandas: es un módulo de análisis de datos. Podemos filtrar los datos de la forma más eficaz. Ofrece diferentes tipos de estructuras de datos con las que es práctico trabajar. También proporciona manejo de archivos con diferentes formatos de archivo, se instala con "pip install pandas"


- Matplotlib: Podemos generar imágenes de las figuras en diferentes formatos. Trazamos diferentes tipos de diagramas como gráficos de barras, gráficos de error, histogramas, diagramas de dispersión, etc., Puede instalar matplotlib utilizando el siguiente comando, basicamente trazos 2D, se instala con "pip install matplotlib".
