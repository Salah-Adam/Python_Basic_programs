line_num = input("Height: ")

while line_num.isalpha() or line_num == "" or int(line_num) < 1 or int(line_num) > 8:
    line_num = input("height: ")
    
else:
    for i in range(1, int(line_num) + 1):
        for j in range(int(line_num), 0, -1):
            if j <= i:
                print("#", end= "")
            else:
                print(" ", end= "")
            print(j if j <= i else " ", end =" ")
        print()