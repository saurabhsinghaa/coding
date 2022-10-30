class Hero:
    def printDetails(self):
        return f"Superhero is {self.superhero}, Age is {self.age} and universe is {self.universe}"


tony = Hero()
adam = Hero()
tony.superhero = "Iron Man"
adam.superhero = "Black Adam"
tony.age = 50
adam.age = 5000
tony.universe = "Marvel"
adam.universe = "DC"
print(tony.printDetails())
print(adam.printDetails())


# --------------------------------------------------------------------
# Superhero is Iron Man, Age is 50 and universe is Marvel
# Superhero is Black Adam, Age is 5000 and universe is DC