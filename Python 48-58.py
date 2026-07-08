#48
num1 = float(input("Enter the first number\t: "))
num2 = float(input("Enter the second number\t: "))
num3 = float(input("Enter the thrid number\t: "))

if num1 >= num2 and num1 >=num3:
    print("largest number is ",num1)
elif num2 >= num1 and num2 >= num3:
    print("largest number is ", num2)
else:
    print("largest number is ",num3)

#49
num1 = float(input("Enter the first number\t: "))
num2 = float(input("Enter the second number\t: "))
num3 = float(input("Enter the second number\t: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest Number is",num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest Number is",num2)
else:
    print("Smallest Number is",num3)

#50
y = int(input("Enter a Year\t: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print(y,"Is a Leap Year.")

else:
    print(y,"Isn\'t a Leap Year.")

#51
m = int(input("Enter a Marks (0-100)\t: "))

if m<0 or m>100:
    print("Invalid Marks !")

elif m>=80:
    print("Grade | A+")
elif m>=70:
    print("Grade | A")
elif m>=60:
    print("Grade | A-")
elif m>=50:
    print("Grade | B")
elif m>=40:
    print("Grade | C")
elif m>=33:
    print("Grade | D")

else:
    print("Grade | F (FAIL)")

#52
m = int(input("Enter a Marks\t: "))

pm = 33

if m < 0 or m > 100:
	print("Invalid Marks !")

elif m>=pm:
	print("Congratulations! You Passed")
else:
	print("Sorry! You Failed")

#53
a = int(input("Enter Your Age\t:" ))

if a>=18:
    print("You are eligible to vote")
else:
    yl = 18-a
    print("Your are not eligible to vote.")
    print("Please wait for",yl,"more year")

#Shorcut
print("Eligible" if int(input("Age: ")) >= 18 else "Not eligible")

#54
c = input("Enter a Single Character : ")

if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    print(c,"is an Alphabet")
else:
    print(c,"is not an Alphabet")
 
#55
c = input("Enter a single character: ")

if '0'<= c <= '10':
    print(c,"is a digit.")
else:
    print(c,"is not a digit")

#56
c = input("Enter an Alphabet Character:")

lo_c = c.lower()

if lo_c in ['a','e','i','o','u']:
    print(c,"is a vowel")
elif lo_c.isalpha():
    print(c,"is a consonant")
else:
    print("Invalid Input please enter an alphabet....")

#57
c = input("Enter a Character\t: ")

if 'a' <= c <= 'z':
    print(c,"is a lower case character.")
elif 'A' <= c <= 'Z':
    print(c,"is a Upper Case Character.")

#58
a = float(input("Enter a first side : "))
b = float(input("Enter a second side : "))
c = float(input("Enter a third side : "))

if (a+b>c) and (b+c>a) and (a+c>b):
    print("Trangle is Valid")
else:
    print("Trangle is not Valid")
