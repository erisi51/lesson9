def calculate_area(width, length):
    return width * length

    def calculate_perimeter (width, length):
     return  2 * (width + length)

      width=5
      length=6

     area = calculate_area(width, length)
    perimeter = calculate_perimeter(width, length)

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_area(self):
        return self.width + self.length
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

my_rectangle = Rectangle(5,3)

    area = my_rectangle.calculate_area()
    perimeter = my_rectangle.calculate_perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def greet(self):
            print(f"Hello i am {self.name} and i am {self.age} years old)

        person1= Person("Eris", 17)
        person2= Person("Vini Jr", 24)


 person1.greet()




