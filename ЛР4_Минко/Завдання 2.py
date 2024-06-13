class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.speed = 0
  def accelerate(self):
    self.speed += 5
  def brake(self):
    if self.speed >= 5:
      self.speed -= 5
    else:
      self.speed = 0

  def get_speed(self):
    return self.speed

my_car = Car("Toyota", "Corolla", 2022)
print("Розгін:")
for _ in range(5):
  my_car.accelerate()
  print(f"Поточна швидкість: {my_car.get_speed()}")

print("\nГальмування:")
for _ in range(5):
  my_car.brake()
  print(f"Поточна швидкість: {my_car.get_speed()}")
class Buffer:
    def __init__(self):
        self.buffer = []
        self.sum = 0

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            for i in range(5):
                self.sum += self.buffer.pop(0)
            print(self.sum)
            self.sum = 0

    def get_current_part(self):
        return self.buffer
buffer = Buffer()
buffer.add(1, 2, 3)
buffer.get_current_part()
buffer.add(4, 5, 6, 7, 8)
buffer.get_current_part()
buffer.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buffer.get_current_part()