import datetime

def tmzoner(t: int):
  utc_now = datetime.datetime.utcnow() # Получаем текущую дату и время в UTC
  offset = datetime.timedelta(hours=t) # Создаем объект timedelta с заданным числом часов
  now_res = utc_now + offset
  return now_res.strftime("[%H:%M:%S] - %d, %B of %Y")

print(tmzoner(-2))



