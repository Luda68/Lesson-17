class House:
    def _init_(self, number_of_floor=0):
        self.numberOfFloor = number_of_floor

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloor = floors
        print(self.numberOfFloor)

h1 = House()
h1.setNewNumberOfFloors(3)