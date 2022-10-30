# USING @staticmethod

class Hero:
    def __init__(self, asuperhero, aage, auniverse):
        self.superhero = asuperhero
        self.age = aage
        self.universe = auniverse

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])

    @staticmethod
    def info(string):
        print(f"{string}, with great power comes great responsibility")


tony = Hero("Iron Man", 50, "Marvel")
peter = Hero.from_str("Spider Man-18-Marvel")
peter.info("Peter")
peter.info("Tony")
Hero.info("Adam")


# ------------------------------------------------------------------------------
# Peter, with great power comes great responsibility
# Tony, with great power comes great responsibility
# Adam, with great power comes great responsibility