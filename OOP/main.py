# Backpack Class Assignment by Sami

# Task 1
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

# Methods

    def openBag(self):
        self.open = True
        print("Backpack is now Open.")
    
    def closeBag(self):
        self.open = False
        print("Backpack is now Closed.")

    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(item + " is now inside the backpack.")

    def takeout(self, item):
        if self.open == True and item in self.items:
            self.items.remove(item)
            print(item + " has been removed from inside the backpack.")
        else:
            print(item + " is not inside the backpack or the backpack is closed.")

# Task 2

bag1 = Backpack("Blue", "Small")
bag2 = Backpack("Red", "Medium")
bag3 = Backpack("Green", "Large")

# Task 3

bag1.openBag()
bag1.putin("Lunch")
bag1.putin("Jacket")
bag1.closeBag()
bag1.openBag()
bag1.takeout("Jacket")
bag1.closeBag()