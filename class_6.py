# class method AS ALTERNATIVE CONSTRUCTOR

class Hero:
    def __init__(self, asuperhero, aage, auniverse):
        self.superhero = asuperhero
        self.age = aage
        self.universe = auniverse

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])


tony = Hero("Iron Man", 50, "Marvel")
adam = Hero("Black Adam", 5000, "DC")
peter = Hero.from_str("Spider Man-18-Marvel")
print(peter.age)
print(tony.age)

# ----------------------------------------------------------
# 18
# 50