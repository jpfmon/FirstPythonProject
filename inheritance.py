class Animal:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"Wow wow!!, I'm {self.name}")


animal = Animal("Ruby")
animal.bark()

class Pet(Animal):
    def groom(self):
        print("Grooming")
    # def bark(self):
    #     print("Wow like a Pet!!!")


animal2 = Pet("Ruby 2")
animal2.bark()
animal2.groom()