radius = float(input("please Enter the radius of a cylinder: \n"))
length = float(input("please Enter the length of a cylinder: \n"))
area = round(radius **2 * 3.14159, 4)
volume = round(area * length, 1)

print("the area is ", area)
print("the volume is ", volume)