def my_generator(a, b):
  es = []
  for i in range(a, (b + 1)):
#    print(i)
    es.append(i)
  return es

for i in my_generator(4, 9):
        print(i)
#print(my_generator(3, 7))


