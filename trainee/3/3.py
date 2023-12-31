# Импортируем модуль logging для работы с логами
import logging

# Создаем декоратор, который будет отлавливать и логгировать ошибки
logging.basicConfig(level=logging.ERROR, filename="error_3.log", format="%(funcName)s %(args)s %(exc_info)s")


def log_errors(func):
# Создаем вложенную функцию, которая будет оберткой для декорируемой функции
  def wrapper(*args, **kwargs):
#    logging.basicConfig(level=logging.ERROR, filename="error_3.log", format="%(funcName)s %(args)s %(exc_info)s")
    try:
      return func(*args, **kwargs)
# Выбрасываем ее дальше
    except ZeroDivisionError as e:
      logging.error(e, exc_info=True)
# Возвращаем обертку
  return wrapper


# ошибкой будет деление на ноль
@log_errors
def divide(x, y):
  if x == -1:
    raise ValueError("я не люблю -1")
  return x / y

print(divide(-1, 2))
