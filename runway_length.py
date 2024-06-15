speed = float(input("please Enter the speed:\n"))
acceleration = float(input("please Enter the acceleration:\n"))
length = round((speed ** 2) / (2 * acceleration), 3)

print("The minimum runway length for this airplane is", length, "meters")
