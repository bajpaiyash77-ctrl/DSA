import math

num = int(input("Enter a number: "))

next_num = num + 1
root = int(math.sqrt(next_num))

if root * root == next_num:
    print("Sunny Number")
else:
    print("Not a Sunny Number")