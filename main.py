
class Fruit:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        pass

class Apple(Fruit):
		def taste(self):
			print(f"Яблоко сладкое")


class Banana(Fruit):
		def taste(self):
			print(f"Банан мягкий")


print(Fruit(name="fryct").get_name())


aple = Apple(name="Яблоко")
print(aple.get_name())
aple.taste()

banana = Banana(name="Банан")
print(banana.get_name())
banana.taste()
