#!/usr/bin/python3
import math # понадобится квадратный корень, значит подключаем модуль математики
import sys # в задании настаивают на употреблении этого модуля - употребим :)
import abc # классы - сделаем!

class Figure(abc.ABC):
    @abc.abstractmethod
    def square(self): # у всех площадь есть... остальное опишем в наследниках
        pass
	
# создаем класс Прямоугольников
class Pryamoug(Figure):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
	
    def square(self):
        return self.a * self.b

class Kvadrat(Figure):
    def __init__(self, a):
        self.a = int(a)
      	
    def square(self):
        return self.a * self.a
    def report(self):
        return a
class Treugolnik(Figure):
    def __init__(self, a, b ,c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
		
    def square(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

if (len(sys.argv) <=2):
    print("запускайте скрипт так:  ./16.py <Figure> <parametr1> [<parametr2> <parametr3>} \n")
    print(" Фигуры: kvadr - квадрат, pryamoug - прямоугольник, treug - треугольник \n")
    print("следующие параметры - длины сторон. одна для квадрата, две для прямоугольника и три для треугольника \n")
    exit
#print(sys.argv[1])


if (len(sys.argv) >= 3):
  fig = sys.argv[1]
  a_s = sys.argv[2]
  if (fig=="kvadr"):
    kv1=Kvadrat(a_s)
    print(kv1.square())

if (len(sys.argv) >= 4):
  fig = sys.argv[1]
  a_s = sys.argv[2]
  b_s = sys.argv[3]
  if (fig=="pryamoug"):
    pr1=Pryamoug(a_s, b_s)
    print(pr1.square())

if (len(sys.argv) >= 5):
  fig = sys.argv[1]
  a_s = sys.argv[2]
  b_s = sys.argv[3]
  c_s = sys.argv[4]
  if (fig=="treug"):
    tr1=Treugolnik(a_s, b_s, c_s)
    print(tr1.square())
