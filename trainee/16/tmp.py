import math # понадобится квадратный корень, значит подключаем модуль математики

print("введите форму комнаты (треугольник, прямоугольник, круг): ")
frm = input()

if frm == "треугольник":
  print("введите длины трех сторон:")
  a = float(input())
  b = float(input())
  c = float(input())
  p = (a + b + c) / 2
  squ = math.sqrt(p * (p - a) * (p - b) * (p - c))

elif frm == "прямоугольник":
  print("введите длины двух сторон:")
  a = float(input())
  b = float(input())
  squ = a * b

elif frm == "круг":
  print("введите радиус (НЕ ДИАМЕТР, а РАДИУС!!!)")
  r = float(input())
  squ = 3.14 * r

else:
  print("Фигура не опознана...")

print("Площадь комнаты:")
print(squ)


