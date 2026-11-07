class Superhero:
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1=attribute1
        self.attribute2=attribute2
        self.attribute3=attribute3
    def superhero(self):
        print("The hero is using their power:", self.attribute1)
        print("Their name is:", self.attribute2)
        print("He wears a:", self.attribute3)


Hero= Superhero("Flying", "Hero", "Cape")
Hero.attribute1="Telekenisis"
Hero.superhero()