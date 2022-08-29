channel = "PinoyFreecoder"
channel_num= 35
is_active= False
average = 3.5

print (channel)


def addnumber(num1,num2):   #defining a function
    total= num1 + num2
    return (total)

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
print("Total: ", addnumber(num1, num2))


class Student:
    def check_pass_fail (self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
            self.name = name
            self.marks = marks

student1 = Student ("Harry", 85)
student2 = Student ("Janet", 30)
did_pass = student1.check_pass_fail()

print(did_pass)
