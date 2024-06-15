a, b, c = eval(input("Enter three edge of the triangle: "))

result = a + b + c

if a + b > c and a + c > b and b + c > a:
    print("the parameter is ", result)
else:
    print("The input is invalid.")