# Write a program to find the factors of a number.

def factor(num):
    l = []
    for x in range(1, num + 1):
        if num % x == 0:
            l.append(x)
    return l

num = int(input('Enter the number to find the factors : '))
list = factor(num)
print('The factor of {} is as follows ---'.format(num))
for m in list:
    print(m, end = '  ')

# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\findFactorofNumber.py
# Enter the number to find the factors : 360
# The factor of 360 is as follows ---
# 1  2  3  4  5  6  8  9  10  12  15  18  20  24  30  36  40  45  60  72  90  120  180  360
