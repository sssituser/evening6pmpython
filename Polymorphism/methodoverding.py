class Animal:
    def sound(self):
        print('Animals can sound')
        
class Dog(Animal):
    def sound(self):
       print("Dog Barks")
       
class Cat(Animal):
    def sound(self):
      print("Cat shout")

for animal in [Animal(),Dog(),Cat()]:
    animal.sound()
        