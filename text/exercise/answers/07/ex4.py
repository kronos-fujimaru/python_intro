class Car:

  count = 0

  def __init__(self, name, gas):
    self.name = name
    self.gas = gas
    __class__.count += 1

  def move(self):
    if(self.gas != 0):
      self.gas -= 1
      print("Move")
    else:
      print("Stop")

  @classmethod
  def get_count(cls):
      return cls.count

class FireTruck(Car):
  def __init__(self, name, gas, water):
    super().__init__(name, gas)
    self.water = water

  def splay_water(self):
    self.water -= 1
    print("Spray Water")

print(Car.get_count())
wagon = Car("Wagon", 3)
print(Car.get_count())
fire_truck = FireTruck("fire_truck", 10, 10)
print(Car.get_count())
