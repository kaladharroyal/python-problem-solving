import math # imports entire math module
from math import pi # import pi value from the math module
print ("pi is : ",pi)

def area( radius):
    return pi *radius**2
print(f"the area of the circle is : {area(5)}")
def circumference(radius):
    return 2*pi*radius
print(f"the circumference of the circle is : {circumference(5)}")