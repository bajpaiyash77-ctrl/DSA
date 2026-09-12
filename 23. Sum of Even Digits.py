num = input("Enter a number: ")

sum = 0

for digit in num:
    if int(digit) % 2 == 0:
        sum = sum + int(digit)

print("Sum of even digits =", sum)
