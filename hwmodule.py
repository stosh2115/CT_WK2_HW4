import math
def area():
    length = float(input("What is the length of your house?"))
    width = float(input("What is the width of your house?"))
    square_footage = length * width
    return square_footage


        
     


def circumference():
    radius = float(input("What is the radius of your circle?"))
    circle = 2 * math.pi * radius
    return circle