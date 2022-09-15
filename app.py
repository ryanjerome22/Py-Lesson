class Warrior:
    def __init__(self, name, health, mana):
        self.name= name
        self.health= health
        self.mana= mana
        print ("The warrior is created. -----> " + self.name)

Warrior1= Warrior("RJ", 100, 50)
print (Warrior)
