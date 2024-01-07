class Vehicle(object):
  def __init__(self, color, doors, tires, brend):
    """Constructor"""
    self.color = color
    self.doors = doors
    self.tires = tires
    self.brend = brend

  def brake(self):
    """ Stop the car    """
    return "Braking"

  def drive(self):
    """   Drive the car    """
    return "I'm driving!"

car1=Vehicle("blue", 5, 4, "Mitsubisi")
print(car1.color) # один из параметров
print(car1.brake()) # метод, описаный как функция


class Track(Vehicle): # наследуем класс
  def brake(self):
    """   Override brake method   переиначим существующий метод """
    return "Thisclass is breaking slowly!"

  def open_doors(self):
    # добавим метод этому подклассу
    return "Dors are opened!"

  def close_doors(self):
    # добавим метод этому подклассу
    return "Dors are CLOSED!"

  def __init__(self,  color, doors, tires, brend, engine):
    super().__init__(color, doors, tires, brend) # вызываю метод __init__ суперкласса
    self.engine = engine # добавляю атрибут в подкласс


gruzovik=Track("Green", 5, 6, "ZAZ", 3100)
print("Добавленый в подкласс параметр ДВИГАТЕЛЬ:", gruzovik.engine)
print(gruzovik.open_doors())
print(gruzovik.close_doors())
print(gruzovik.brend)
print("\n\n При всем уважении к заданию \"Примените инкапсуляцию...\" я пока не делаю... \n это в сторону оберток-декораторов"   )


