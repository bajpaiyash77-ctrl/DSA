num = input("Enter a number: ")

if len(num) == 1:
    result = num
else:
    result = num[-1] + num[1:-1] + num[0]

print("After swapping =", result)