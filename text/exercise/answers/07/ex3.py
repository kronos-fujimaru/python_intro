class Car:
  def __init__(self, name, gas):
    self.name = name
    self.gas = gas

  def move(self):
    if(self.gas != 0):
      self.gas -= 1
      print("Move")
    else:
      print("Stop")

class FireTruck(Car):
  def __init__(self, name, gas, water):
    super().__init__(name, gas)
    self.water = water

  def splay_water(self):
    self.water -= 1
    print("Spray Water")

fire_truck = FireTruck("fire_truck", 10, 10)

for i in range(1, 3):
  fire_truck.move()

fire_truck.splay_water()
