class student:
    def __init__(self, Firstname, Lastname, Course, Friends):
        self.Firstname= Firstname
        self.Lastname = Lastname
        self.Course = Course
        self.Friends = Friends
        print ("User Created Name: " + self.Firstname)

    def introduce (self):
        print(f"Good Morning! My name is { self.Firstname + self.Lastname }")

    def fullprofile (self):
        print ("Full Name : " + self.Firstname + " " + self.Lastname)
        print ("Course : " + self.Course)
        print ("Friends: ")
        for friend in self.Friends:
            print(" -- " + friend)

studentone = student("Ryan Jerome", " Valencia", "BS ECE", ["Nisa", "Albert", "Agee", "Louise"] )
studentone.introduce()
studentone. fullprofile()

class User(student):
    def __init__(self,Firstname, Lastname, Course, Friends, grades):
        super().__init__(Firstname, Lastname, Course, Friends,)
        self.grades= grades

    def introduce (self):
        print(f"Good Morning! My name is { self.Firstname + self.Lastname + self.grades }")


p0ne = student("Christine Nisa ", "Velasco", "BSMLS", ["RJ", "Leo", "Jojit"])
p0ne.introduce()


uone = User("Norely ", "Valencia", "BSEDUC", ["JR", "Mia", "Mylene"], int(25))
uone.introduce()