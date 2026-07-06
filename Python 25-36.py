#25
list1 = [20,40,60,80,100]
list2 = [20,40,60,80,100]
list3 = list1

print("list1==list2 (Same values?):", list1 == list2)
print("list1 is list2 (Same object?):", list1 is list2)
print("list1 is list3 (Same object?):", list1 is list3)

print("list1 id:", id(list1))
print("list2 id:", id(list2))
print("list3 id:", id(list3))
#26
Cars = ["Toyota", "Ford", "BMW", "Mercedes"] 
text = "Bugatti is a fasttest car in the world"

print("Is 'Toyota' in Cars list?:", "Toyota" in Cars) 
print("Is 'Honda' in Cars list?:", "Honda" in Cars)

print("Is 'Bugatti' inside text?:", "Bugatti" in text) 
print("Is 'Slowest' NOT in text?:", "Slowest" not in text)
#27
a = 44
b = 50

print("Bitwise AND (a & b):", a & b)
print("Bitwise OR (a | b):", a | b)
print("Bitwise XOR (a ^ b):", a ^ b)

print("Bitwise NOT (~a):", ~a)
print("Left Shift (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)
#28
Base = float(input("Enter the base number: "))
Power = float(input("Enter the power number: "))

result = Base ** Power
print("The Result is ", result)
#29
total_sec = int(input("Enter the total seconds: "))

min = total_sec // 60
re_sec = total_sec % 60

print(total_sec, "seconds is equal to", min, "minutes and", re_sec, "seconds.")
#30
candy = int(input("Enter the number of candies: "))
children = int(input("Enter the number of children: "))

per_child = candy // children
remaining_candies = candy % children

print("Each child will receive:", per_child, "candies")
print("candies left:", remaining_candies)
#31
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
print("The area of the rectangle is:", area)
#32
length = int(input("Enter the length of the rectangle: "))  
width = int(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)
#33
side = float(input("Enter the length of the side of the square: "))
area = side ** 2

print("The area of the square is:", area)
#34
import math

redius = float(input("Enter the radius of the circle: "))
area = math.pi * (redius ** 2)
print("The area of the circle is:", round(area, 2))
#35
import math

redius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * redius
print("The circumference of the circle is:", round(circumference, 2))
#36
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height
print("The area of triangle is:", round(area, 2))
