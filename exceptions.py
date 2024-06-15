try:
    age = int(input("enter your age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown")


'''
# adding zero devision error it means to prevent to enter 0 as age
try:
    age = int(input("enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
'''
