num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i

    sum = sum + factorial
    num = num // 10

if sum == original:
    print("Strong Number")
else:
    print("Not a Strong Number")