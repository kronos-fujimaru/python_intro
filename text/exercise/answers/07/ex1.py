class Car:
  def __init__(self, name):
    self.name = name

  def move(self):
    print("Move")

wagon = Car("Wagon")
wagon.move()
