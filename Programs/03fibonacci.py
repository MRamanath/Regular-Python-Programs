def fibonacci(nterm):
    if nterm <= 1:
        return nterm
    else:
        return fibonacci(nterm - 1) + fibonacci(nterm - 2)

nterm = int(input('How many terms ? '))
if nterm <= 0:
    print('Please Enter a positive integer')
else:
    for i in range(nterm):
        print(fibonacci(i))


# PS C:\Users\RAMANATH\Documents\PythonPrograms\function> py .\15fibonacci.py
# How many terms ? 10
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# PS C:\Users\RAMANATH\Documents\PythonPrograms\function> py .\15fibonacci.py
# How many terms ? -19
# Please enter a positive integer