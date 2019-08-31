# Sum of digits of a number.

def sumOfDigit(num):
    temp = num
    rev = 0
    while temp != 0:
        rem = temp % 10
        rev = rev + rem
        temp = temp // 10
    return rev

num = int(input('Enter a number : '))
print(sumOfDigit(num))

# Enter a number : 12223
# 10