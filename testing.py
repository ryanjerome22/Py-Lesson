class Hotdog:
    def __init__(self, brand, size, length):
        self.brand = brand
        self.size = size
        self.length= length
    
    def Introduce(self):
        print ("The brand of the hotdog is "+ self.brand + ".")

Hotdog1=Hotdog("Tender Juicy", 3, "Long")

Hotdog1.Introduce ()



class FB:
    def __init__(self, FirstName, LastName, FbLikes, FbFriends):
        self.FirstName= FirstName
        self.LastName= LastName
        self.FbLikes= FbLikes
        self.Fbfriends= FbFriends

    def NewAccount (self):
            print ("FB Account: ")
            print(" My Name is : " + self.FirstName + self.LastName)
            print(" FB Likes: " + str(self.FbLikes))
            print (" FB Friends: ")

            for friend in self.Fbfriends:
                print ("   --" + friend)

FB1 = FB ("Ryan Jerome ", "Valencia ", 23, ["Christine Nisa", "Norely M. Valencia"])
FB2 = FB ("Christine Nisa ", "Velasco", 100, ["Ryan Jerome", "Norely"])

FB1.NewAccount()
FB2.NewAccount()




