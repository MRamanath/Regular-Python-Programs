# Factorial of a number.

def fact(num):
    fact = 1
    while num >= 1:
        fact = fact * num
        num = num - 1
    return fact

d = fact(0)
print('Factorial is = ', d)

# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\01factorial.py
# Factorial is =  120
# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\01factorial.py
# Factorial is =  1