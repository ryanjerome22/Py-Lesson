# Sample Class
from turtle import done


class Warrior:
    def __init__(self, name, health, mana):
        self.name= name
        self.health= health
        self.mana= mana
        print ("The warrior is created. -----> " + self.name)

Warrior1= Warrior("RJ", 100, 50)
print (Warrior)

# is instance function
name = int("20")

print(isinstance(name,int))

#Ternary Operator

def is_adult (age):
    if age > 18:
        return True
    else:
        return False

def is_adult2 (age):
    return True if age > 18 else False


done= True

def example ():
    if done:
        return ("yes")
    else:
        return ("no")