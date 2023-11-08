
def okruglyator(p: float):
  p = round(float(p), 2)
  return str(p)

def formater(p: float):
  p = format(float(p), '.2f')
  return str(p)


print("введите число типа float и не стесняйтесь добавить много цифр после точки")
pp=input()

print(okruglyator(pp), " первый вариант\n")
print(formater(pp), " второй вариант\n")
