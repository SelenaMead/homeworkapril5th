from math import pi


def square_footage():
    width = int(input("What is the width of the room?"))
    length = int(input("What is the length of the room?"))

    print(width * length)

def circumference():
    radius = input("What is the radius of the circle?")
    print(int(radius) * 2 * pi)