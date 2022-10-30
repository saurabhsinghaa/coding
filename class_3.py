# USING __init__

class Hero:
    def __init__(self, asuperhero, aage, auniverse):
        self.superhero = asuperhero
        self.age = aage
        self.universe = auniverse


tony = Hero("Iron Man", 50, "Marvel")
adam = Hero("Black Adam", 5000, "DC")
print(tony.universe)


# --------------------------------------------
# Marvel