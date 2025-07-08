# Write a program that checks if a number is positive or negative. If it is zero, print "Zero".
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("zero")
else:
   print("negative number")
# Input a number and print whether it is even or odd.   
num= int(input("Enter a number: "))
if num % 2 == 0:
   print("Even number")
else:
   print("Odd number")
# Ask the user to enter their age. If the age is 18 or above, print "Eligible to vote", 
# otherwise print "Not eligible".
age = int(input("Enter your age: "))
if age >= 18:
   print("Eligible to vote")
else:
   print("Not eligible")
# Enter a number and print whether it is divisible by 3, 5, or both.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
  print("Divisible by both 3 and 5")
elif num % 3 == 0:
  print("Divisible by 3")
elif num % 5 == 0:
  print("Divisible by 5")
else:
  print("Not divisible by 3 or 5")
# Ask for a student's marks. If marks are 90 or above, print "A+", if 80 or above, print "A", 
# if 70 or above, print "B", otherwise print "Fail".
marks = float(input("Enter student's marks: "))
if marks >= 90:
  print("A+")
elif marks >= 80:
  print("A")
elif marks >= 70:
  print("B")
else:
  print("Fail")
# Take a temperature value. If it's above 40, print "Too hot", if it's below 10, print "Too cold", 
# otherwise print "Moderate weather".   
temperature = float(input("Enter the temperature: "))
if temperature > 40:
  print("Too hot")
elif temperature < 10:
  print("Too cold")
else:
  print("Moderate weather")
# Ask the user to enter a year. Check whether the year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
# Input three numbers and print the largest one.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)
# Enter a password. If the password matches "admin123", print "Access granted", otherwise 
# print "Access denied".
password = input("Enter a password: ")
if password == "admin123":
  print("Access granted")
else:
  print("Access denied")
# Take an integer input. If the number is greater than 0, check if it is less than 100. Print appropriate 
# messages for each condition.
num = int(input("Enter an integer: "))
if num > 0:
  if num < 100:
    print("The number is greater than 0 and less than 100.")
  else:
    print("The number is greater than 0 but not less than 100.")
else:
  print("The number is not greater than 0.")