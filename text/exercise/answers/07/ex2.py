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

wagon = Car("Wagon", 3)

for i in range(1, 6):
  wagon.move()
