
class Vehicle:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year= year

	def get_info(self):
		info = f"Марка: {self.make}, Модель: {self.model}, Год: {self.year}"
		return info

	def speak(self):
		pass

class Car(Vehicle):
		def start_engine(self):
			print(f"Машина завелась!")


class Bicycle(Vehicle):
		def ring_bell(self):
			print(f"Звенит звонок велосипеда!")

car1 = Vehicle("Toyota Camry", 201, 1998)
print(car1.get_info())


Car("Toyota Camry", 201, 1998).start_engine()
Bicycle("Toyota Camry", 201, 1998).ring_bell()
