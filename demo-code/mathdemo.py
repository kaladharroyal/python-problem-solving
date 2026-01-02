#1 Calculate the square root of the sum of two numbers.import math
import math
a = int(input("enter value of a: "))

b = int(input("enter b value: "))

c = a+b

d = math.sqrt(c)

print(f" the square root of the sum {c} is {d}") 

#2 Calculate the circumference and area of a circle.
radius = float(input("enter the radius of the circle: "))

area = 2*math.pi*radius

circumference = math.pi*radius**2

print(f" the area is {area} and circumference {circumference}")

# 3 Calculate the trigonometric functions of an angle.

angle = float(input("enter the value in degrees: "))
radians = math.radians(angle)

print("math.sin()",math.sin(radians))

print("math.cos()",math.cos(radians))

print("math.tan()",math.tan(radians))