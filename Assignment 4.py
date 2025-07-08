# Create two variables a = 10 and b = 3. Perform and print the results of addition, 
# subtraction, multiplication, division, modulus, exponentiation, and floor division.
a=10
b=3
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)
# Compare the variables a and b using all comparison operators (==, !=, >, <, >=, <=) 
# and print the results.
x = 5
y = 8
print("x == y = ", x == y)
print("x != y = ", x != y)
print("x > y  = ", x > y)
print("x < y = ", x < y)
print("x <= y = ", x <= y)
print("x >= y = ", x >= y)
# Create two boolean variables x = True and y = False. Perform and print the results of x
# and y, x or y, and not x.
x = True
y= False
print("x and y = ", x and y)
print("x or y  = ", x or y)
print("not x   = ", not x)
# Create a variable num = 5. Use +=, -=, =, /=, %=, *=, and //= assignment operations on it 
# and print the result each time.
x = 5
print(" x = 5 =",x)
x += 5
print(" x += 5 =",x)
x -= 5
print(" x -= 5 ",x)
x *= 5
print(" x *= 5 ",x)
x /= 5
print(" x /= 5 ",x)
x //= 5
print(" x //= 5 ",x)
# Create two variables m = 100 and n = 100. Check if they are the same object using is and is not 
# and print the results.
m=100
n=100
print("m is n     =  ",m is n)
print("m is not n =  ", m is not n)
# Create a string text = "Python Programming". Check if "Python" is in the text and if "Java" 
# is not in the text.
text="python programming"
print("python is in the text=","python" in text)
print("java is not in the text=","java" not in text)
# Write a Python program to print all keywords using the keyword module.
import keyword
print("python keyword:")
print(keyword.kwlist)
# Declare three variables name = "Ali", age = 20, height = 5.9 and print their values 
# along with their data types.
name,age,height="ali",20,5.9
print(type(name),"name=",name)
print(type(age),"age=",age)
print(type(height),"height=",height)
# Write five valid variable names and three invalid ones (as comments). Explain why the 
# invalid ones are not allowed.
# Valid variable names
name = "ayesha"
_age = 16
salary2024 = 15000
programming_language = "Python"
# Create variables with special naming styles: _hidden = 5, __private = 10, MAX_SIZE = 100. Print them.
_hidden=5
_private=10
max_size=100
print("_hidden=",_hidden)
print("_private=",_private)
print("max_size=",max_size)
# Assign values x = 1, y = 2, z = 3 in a single line and print them.
x,y,z=1,2,3
print(x,y,z)
# Assign the same value 0 to three variables a, b, and c in one line and print them.
a=b=c=0
print(a,b,c)
# Create a variable temp = 100, print it, delete it using del, and then try to print it 
# again to observe the error.
temp=100
print("temp",temp)
del(temp)
print("temp",temp)
# Create a string variable using triple single quotes ('''Hello''') and print it.
string='''hello'''
print("string=",string)
# Create a multi-line string using triple double quotes ("""This is line one.\nThis is line two.""") 
# and print it.
string="""this is line one./n this is line two"""
print(string)
# Use the type() function to print the data type of each of the following: an integer, a float, 
# a string, and a boolean.
print(type(25))
print(type(19.7))
print(type("ayesha"))
print(type(False))
# Create a variable score = 85. Check if the score is greater than 50 and less than 100 using a 
# logical expression.Print the result.
score=85
print((score>50)and(score<100))
# Create a string message = "Welcome to Python". Use the in and not in operators to check the presence 
# of the word "Python".
message="welcome to python"
print("python in the message=", "python" in message)
print("python not in message=","python" not in message)
# Create a variable data = 123. Use the id() function to print its memory address.
data=123
print("memory address of the variable=",id(data))