# Create a variable called greeting and store any message.print it
greeting="hello world"
print(greeting)
# change the value of greeting and print the new message.
greeting="AI HUB"
print(greeting)
# Create first_name and last_name,then print full name using f-string.
first_name="kinza"
Last_name="Amjad"
print(f"{first_name} {Last_name}")
# Print a famous quote with authors name using f-string.
quote="Education is the most powerful weapon which can use to change the world"
Author_name=" Nelson Mandela"
print(f"{quote}-Author_name")
# Store a name with extra spaces,strip them ,and print clean output.
name="   kinza  "
print(name.strip())
# Take a number, add 5,multiply by 2,subtract 3, and print the result.
a=8
result=((a+5)*2-3)
print("result:",result)
# Create a and b;print their sum, difference,product and quotient. 
a=8
b=6
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("quotient:",a/b)
# Find square and cube of a number using ** operator.
x=8
print("square:",x**2)
print("cube:",x**3)
# Add three floating point numbers and print the total.
x=12.2
y=562.4
z=785.5
total=x+y+z
print("total:",total)
# Assign x,y,z in one line and print them.
x=y=z=15
print(x,y,z)
# Create a list of 5 favourite fruits and print each one separately.
fav_fruits=["peach","banana","mango","orange","grapes"]
for x in fav_fruits:
    print(x)
# Modify the 2nd item in the list and print the updated list.
item_list=["bread","sugar","milk","butter","tea"]
item_list[1]="salt"
print(item_list)
# Append a new fruit and insert one at the begining.
fruits_name=["mango","banana","pear","watermelon"]
fruits_name.append("orange")
fruits_name.insert(0,"apple")
print(fruits_name)
# Delete items using del,pop(), and remove().
x=["salt","sugar","tea","milk","curd"]
del x[0]
print(x)
x.pop(1)
print(x)
x.remove("milk")
print(x)
# Use a sort() and sorted() the list.Show before and after.
a=[4,2,8,0,6,10]
print("before sort:",a)
a.sort()
print("after sort:",a)

b=[0,10,9,4,22,17,25]
print("before sorted:",b)
c=sorted(b)
print("after sorted:",c)
# Create list of dream travel destination:
# sort alphabetically
# Reverse the order
# Count total destination.
x=["turkey","switzerland","new zealand","japan","canada"]
sorted(x)
print("sorted alphabetically:",x)
x.reverse()
print("reverse order:",x)
print("total destinations:",len(x))
# Start with an empty guest list:
# Append 3 guests
# Insert 1 at the beginning
# Remove one using pop()
# print final list
guest_list=[]
guest_list.append("ayesha")
guest_list.append("faiza")
guest_list.append("hina")
guest_list.insert(1,"aqsa")
guest_list.pop(2)
print(guest_list)
# Access the last 3 elements of a list without negative indexing.
a=[1,3,5,7,9,11,13,15]
print(a[5:8])
# From a list of numbers, print only even numbers.
x=[0,1,2,3,4,5,6,7,8,9,10]
for num in x:
  if num % 2 == 0:
    print(num)
# Print squares of the first 10 natural numbers in a list.
squares = []
for i in range(1, 11):
  squares.append(i**2)
print(squares) 