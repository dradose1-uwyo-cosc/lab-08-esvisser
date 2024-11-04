# ezra visser
# UWYO COSC 1010
# Submission Date11/4/2024
# Lab 08
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def int_convert (string):
    num=0
    input=string
    if input[0]=="-":
       input=input.removeprefix('-')
       num=num-int(input)
       return num
    elif input.isdigit():
        num=num+int(input)
        return num
    else:
        return False
      

print("*" * 75)
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def equation(m,b,lower,upper):
    y=0
    for num in range(lower,upper):
        y= (m*num)+b
        print(y)

while True:
    user_input=input("enter the m and b for a y=mx+b equation, as well as the upper and lower bound for it to be evaluated on seperated by commas(ex.3,5,7,12). enter exit to stop ")
    if user_input =='exit':
        break
    nums=user_input.split(',')
    m=int_convert(nums[0])
    b=int_convert(nums[1])
    upper=int_convert(nums[2])
    lower=int_convert(nums[3])
    
    if upper==False or lower==False:
       print("invalid input")
    else:
        equation(m,b,upper,lower)
    

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadform_plus(a,b,c):
    y=(-b+((b**2)+(4*a*c))**0.5)/(2*a)
    print(y)
def quadform_minus(a,b,c):
    y=(-b-((b**2)+(4*a*c))**0.5)/(2*a)
    print(y)
while True:
    user_input=input("enter values for the variables in the quadratic formula seperated by comas(ex. 2,5,3).enter exit to stop ")
    if user_input=='exit':
        break
    nums=user_input.split(',')
    a=int_convert(nums[0])
    b=int_convert(nums[1])
    c=int_convert(nums[2])
    quadform_plus(a,b,c)
    quadform_minus(a,b,c)
def sqrt(x):
    if x>0:
        print(x**0.5)
    else:
        return False
while True:
    user_input=input("enter a number to square rooted. enter exit to stop ")
    if user_input=="exit":
        break
    num=int_convert(user_input)
    sqrt(num)