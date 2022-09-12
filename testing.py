class Hotdog:
    def __init__(self, brand, size, length):
        self.brand = brand
        self.size = size
        self.length= length
    
    def Introduce(self):
        print ("The brand of the hotdog is "+ self.brand + ".")

Hotdog1=Hotdog("Tender Juicy", 3, "Long")

Hotdog1.Introduce ()




