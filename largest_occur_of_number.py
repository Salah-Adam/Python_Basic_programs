number = eval(input("Enter a number (0: for end of input): "))
max = 0
count = 0

if number != 0:
    while number != 0:
        if number > max:
            max = number
            count = 1
        elif number == max:
            count += 1

        number = eval(input("Enter a number (0: for end of input): "))

    print("The largest number is ", max)
    print("The occurence count of the largest number is ", count)

else:
    print("No number is entered except 0")