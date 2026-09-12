num = input("Enter a number: ")

result = ""

for digit in num:
    if digit != '0':
        result = result + digit

print("After removing zeros =", result)