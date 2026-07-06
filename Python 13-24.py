#13
value11 = int(input("Enter first Value: "))
value12 = int(input("Enter second Value: "))
average = (value11 + value12) / 2
print("The average is:", average)

#14
value13 = float(input("Enter first Value: "))
value14 = float(input("Enter second Value: "))
value15 = float(input("Enter third Value: "))
average = (value13 + value14 + value15) / 3
print("The average is:", average)

#15
num1 = int(input("Enter first Value: "))
num2 = int(input("Enter second Value: "))
print("Before swapping: num1 =", num1, "num2 =", num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping: num1 =", num1, "num2 =", num2)

#16
num3 = int(input("Enter first Value: "))
num4 = int(input("Enter second Value: "))
print("Before swapping: num3 =", num3, "num4 =", num4)
num3, num4 = num4, num3
print("After swapping: num3 =", num3, "num4 =", num4)

#17
int_num = 50
print("Original number:", int_num, "| Data Type:", type(int_num))
float_num = float(int_num)
print("Converted to float:", float_num, "| Data Type:", type(float_num))

#18
float_num2 = 88.40
print("Original number:", float_num2, "| Data Type:", type(float_num2))
int_num2 = int(float_num2)
print("Converted to integer:", int_num2, "| Data Type:", type(int_num2))

#19
str_num = "123"
print("Original string:", str_num, "|  Data Type:", type(str_num))
str_num = int(str_num)
result = str_num + 100
print("after converting to integer and adding 100:", result)
print("New Data Type:", type(str_num))

#20
Name = "S.M.Riadul Karim"
Age = 18
Height = 5.8
Is_student = True
Is_Working = False
print("Name:", Name, "| Data Type:", type(Name))
print("Age:", Age, "| Data Type:", type(Age))
print("Height:", Height, "| Data Type:", type(Height))
print("Is_student:", Is_student, "| Data Type:", type(Is_student))
print("Is_Working:", Is_Working, "| Data Type:", type(Is_Working))

#21
a = int(input("Enter first Value: "))
b = int(input("Enter second Value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#22
num5 = 40
print("Initial value:", num5)
num5 += 10
print("After adding 10:", num5)
num5 -= 5
print("After subtracting 5:", num5)
num5 *= 2
print("After multiplying by 2:", num5)
num5 /= 4
print("After dividing by 4:", num5)

#23
x = int(input("Enter first Value: "))
y = int(input("Enter second Value: "))
print("(x == y)? =", x == y)
print("(x != y)? =", x != y)
print("(x > y)? =", x > y)
print("(x < y)? =", x < y)
print("(x >= y)? =", x >= y)
print("(x <= y)? =", x <= y)

#24
Age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ") == "yes"
#And Oparator
can_enter = Age >= 18 and has_id
print("Can Enter restricted area (age >= 18 and has ID)?", can_enter)
#Or Oparator
discount = (Age < 12 or Age >= 60) and has_id
print("Eligible for discount (age < 12 or age >= 60):", discount)
#Not Oparator
print("Is not eligible for discount:", not discount)