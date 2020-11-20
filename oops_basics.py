class MotorBike:
    pass

honda = MotorBike()
ducati = MotorBike()

honda.speed = 50
ducati.speed = 500

print(honda)
print(ducati)

print(honda.speed)
print(ducati.speed)

# class Car:
#     def __init__(self):
#         print("Car created")

class Car:
    def __init__(self,speed):
        self.speed = speed
        print(f"Car created with speed: {self.speed}")



coche = Car(50)
print(coche.speed)
