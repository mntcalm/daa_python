def func33(sps):
  for i in range (0, len(sps)):
    if sps[i] == 777:
      return "три семерки нашлись в " + str(i) + "-м элементе"
    if i >= 99:
      raise ValueError("не находятся три семерки в первой сотне элементов...")

sps_of=[int(222) for i in range(702)]
sps_of[170]=int(777)

#print(sps_of)
print(func33(sps_of))

