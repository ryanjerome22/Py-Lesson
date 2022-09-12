#Creating Class
class Character :
    qname = "Name"  #creating objects
    qhp = 100
    qmp = 50
    qatk = 12
    qlvl = 1


class MainCharacter:
    def __init__(self, name, hp, mp, atk, lvl): #constructor
         self.name = name
         self.hp = mp
         self.atk = atk
         self.lvl = lvl
         print ("Created " + self. name)

MainCharacter1= MainCharacter("RJ", 22, 3, 23, 4)
MainCharacter2= MainCharacter("Nisa", 24, 25, 26, 25)

class animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice
    
    def speak (self):
        print (self.voice)

aone= animal ("Dog", "ARF!")

aone.speak ()