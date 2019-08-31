# Prime number check

def prime(num):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
        else:
            flag = 0
    return flag

x = int(input('Enter a number to check prime or not: '))
if prime(x) == 0:
    print('{} is prime number'.format(x))
else:
    print('{} is not prime number'.format(x))

# Enter a number to check prime or not: 7
# 7 is prime number
# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\02primenum.py
# Enter a number to check prime or not: 11
# 11 is prime number
# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\02primenum.py
# Enter a number to check prime or not: 9
# 9 is not prime number