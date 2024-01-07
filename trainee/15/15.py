import abc

#@abc.ABC
class Animal(abc.ABC):
  # создаем абстрактные методы say, run и jump
  # абстрактный класс для меня - не класс, а вроде ограничителя...
  # я все еще не ведаю, что творю
  @abc.abstractmethod
  def say(self):
    pass

  @abc.abstractmethod
  def run(self):
    pass

  @abc.abstractmethod
  def jump(self):
    pass

# создаем класс Cat, который наследует от Animal
class Cat(Animal):
# реализуем абстрактные методы say, run и jump если можно - без __init__ ...
  def say(self):
    print("Мяу!")

  def run(self):
    print("Коты бегают, но не особо это любят")

  def jump(self):
    print("Кошки очень даже прыгают")

# создаем класс Dog, который наследует от Animal
class Dog(Animal):
# реализуем абстрактные методы say, run и jump
  def say(self):
    print("Гав!")

  def run(self):
    print("Собаки отлично бегают")

  def jump(self):
    print("Прыгают собаки неохотно")


cat1 = Cat()
dog1 = Dog()


cat1.run()
dog1.run()
cat1.say()
dog1.say()
cat1.jump()
dog1.jump()


