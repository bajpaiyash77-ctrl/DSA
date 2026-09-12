num = int(input("Enter a number: "))

while num >= 10:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    num = sum

print("Digital Root =", num)