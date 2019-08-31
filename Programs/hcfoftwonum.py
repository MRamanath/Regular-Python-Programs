# Python program to find the H.C.F. of two numbers.

def hcf_of_two_num(x, y):
    if x > y:
        sm = y
    else:
        sm = x
    for m in range(1, sm + 1):
        if x % m == 0 and y % m == 0:
            hcf = m
    return hcf

num1, num2 = [int(x) for x in input('Enter two number : ').split()]
print('HCF of {} and {} is {}'.format(num1, num2, hcf_of_two_num(num1, num2)))

# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\hcfoftwonum.py
# Enter two number : 23 57
# HCF of 23 and 57 is 1
# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\hcfoftwonum.py
# Enter two number : 18 36
# HCF of 18 and 36 is 18
# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\hcfoftwonum.py
# Enter two number : 54 24
# HCF of 54 and 24 is 6