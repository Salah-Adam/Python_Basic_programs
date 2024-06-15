import math

number_of_sides = eval(input("please enter the number of sides: "))
length_of_side = eval(input("\nplease enter the side: "))
area_of_regular_polygon = (number_of_sides * (length_of_side ** 2)) / (4 * math.tan(math.pi / number_of_sides))

print("\nThe area of the polygon is", area_of_regular_polygon)