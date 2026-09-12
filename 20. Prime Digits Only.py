num = input("Enter a number: ")

prime_digits = "2357"
flag = True

for digit in num:
    if digit not in prime_digits:
        flag = False
        break

if flag:
    print("All Digits are Prime")
else:
    print("Not All Digits are Prime")