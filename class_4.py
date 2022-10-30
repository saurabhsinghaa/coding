# WHEN @classmethod IS NOT USED

class Hero:
    race = "black"

    def __init__(self, asuperhero, aage, auniverse):
        self.superhero = asuperhero
        self.age = aage
        self.universe = auniverse
    
    # @classmethod
    def change_race(cls, newRace):
        cls.race = newRace


tony = Hero("Iron Man", 50, "Marvel")
adam = Hero("Black Adam", 5000, "DC")
tony.change_race("white")
print(tony.race)
print(adam.race)


# -------------------------------------------------
# white
# black