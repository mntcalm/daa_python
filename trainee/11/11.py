import random
import time
random_number = random.randint(1, 10)
#print(random_number)

def sleeper(paus):
  start_time=time.time()
  time.sleep(paus)
  end_time=time.time()
  return end_time - start_time

print("Функция спала ", sleeper(random_number), "секунд")
