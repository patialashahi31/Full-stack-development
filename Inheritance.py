class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys



mike = Child("John","green",3)
print(mike.number_of_toys)
print(mike.last_name)