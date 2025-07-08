# Declare a variable student_id with a value of 101 (integer) and a variable grades with a list containing
# three integers: 85, 90, 92. Print the value and type of both variables using the type() function.
student_id:int = 101
grades:list=[85,90,95]
print(student_id,type(student_id))
print(grades,type(grades))
# Create a variable price with a value of 19.99 (float) and a variable dimensions with a tuple containing
# two floats: 5.5, 3.2. Print the value and type of both variables.
price:float=19.99
dimension:tuple=(5.5,3.2)
print(type(price),"price=",price)
print(type(dimension),"dimension=",dimension)
# Declare a variable complex_value with a complex number 2 + 3j and a variable numbers with a range 
# from 1 to 5 (i.e., range(1, 5)). Print the value and type of both variables.
complex_value:complex=2+3j
number:range=range(1,5)
print(type(complex_value),"complex_value=",complex_value)
print(type(number),"number=",number)
# Create a variable is_active with a boolean value True and a variable unique_ids with a set 
# containing three integers: 1, 2, 3.Print the value and type of both variables.
is_active:bool=True
unique_ids:set={1,2,3}
print(type(is_active),"is_active is",is_active)
print(type(unique_ids),"unique_ids is",unique_ids)
# Declare a variable status with a string "Active" using single quotes and a variable fixed_colors
# with a frozenset containing two strings: "red", "blue". Print the value and type of both variables.
status:str='Active'
fixed_colors:frozenset=frozenset(["red","blue"])
print(type(status),"status=",status)
print(type(fixed_colors),"fixed_colors=",fixed_colors)
# Create a variable country with a string "Canada" using double quotes and a variable cities with a list 
# containing two strings: "Toronto", "Vancouver". Print the value and type of both variables.
country:str="canada"
cities:list=["toronto","vancouver"]
print(type(country),"country=",country)
print(type(cities),"cities=",cities)
# Declare a variable motto with a string "Keep it simple" using triple single quotes and a variable coordinates 
# with a tuple containing three integers: 10, 20, 30. Print the value and type of both variables.
motto:str='''keep it simple'''
coordinates:tuple=(10,20,30)
print(type(motto),"motto=",motto)
print(type(coordinates),"coordinates=",coordinates)
# Create a variable quantity with a value of 50 (integer) and a variable tags with a set containing two 
# strings: "urgent", "new". Print the value and type of both variables.
quantity:int=50
tags:set={"urgent","new"}
print(type(quantity),"quantity=",quantity)
print(type(tags),"tags=",tags)
# Declare a variable distance with a value of 42.5 (float) and a variable steps with a range from 0 to 10
# with a step of 2 (i.e., range(0, 10, 2)). Print the value and type of both variables.
distance:float=42.5
steps:range=range(0,10,2)
print(type(distance),"distance=",distance)
print(type(steps),"steps=",steps)
# Create a variable note with a multi-line string using triple double quotes: Meeting at 9 AM Bring
# notebook and a variable locked_values with a frozenset: {100, 200, 300}. 
# Print the value and type of both variables.
note: str = """Meeting at 9 AM
Bring notebook"""
locked_values: frozenset = frozenset({100, 200, 300})
print(type(note),"note=",note)
print(type(locked_values),"locked_values=",locked_values)
