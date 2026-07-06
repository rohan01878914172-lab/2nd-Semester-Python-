#37
base = float(input("Enter the base of the triangle: "))
prependicular = float(input("Enter prependicular height: "))

area = (0.5 * base * prependicular)
print("The area of triangle is:", round(area, 2))
#38
import math

radius = float(input("Enter the radius of the circle: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius ** 2 * height
print("The volume of the cylinder is:", round(volume, 2))
#39
side = float(input("Enter the length of the side of the square: "))

volume = side ** 3
print("The volume of the cube is:",round(volume, 2))
#40
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9
print("The temperature in Celsius is:", round(celsius, 2))
#41
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", round(fahrenheit, 2))
#42
killomiter = float(input("Enter the distance in kilometers: "))

meter = killomiter * 1000
print("The distance in meters is:", round(meter, 2))
#43
meter = float(input("Enter the distance in meters:"))

kilometer = meter / 1000
print(meter, "meters is equal to",kilometer, "kilometers.")
#44
Random_num = int(input("Enter a Number:"))

if Random_num % 2 == 0:
    print(Random_num, "is an Even Number.")
else:
    print(Random_num, "is an Odd Number.")
#45
Random_num = float(input("Enter a Number:"))

if Random_num> 0:
    print(Random_num, "is a Positive Number.")
elif Random_num < 0:
    print(Random_num, "is a Negative Number.")
else:
    print(Random_num, "is Zero.")
#46
Number1 = int(input("Enter the first number:"))
Number2 = int(input("Enter the second number:"))

if Number1 > Number2:
    print(Number1, "is the largest number.")

elif Number2 > Number1:
    print(Number2, "is the largest number.")

else:
    print("Both numbers are equal.")
#47
Number1 = int(input("Enter the first Number:"))
Number2 = int(input("Enter the second Number:"))

if Number1 < Number2:
    print(Number1, "is the smallest number.")
elif Number2 < Number1:
    print(Number2, "is the smallest number.")
else:
    print("Both numbers are equal.")
    