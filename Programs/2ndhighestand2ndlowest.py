# Write a program to find the 2nd highest and 2nd minimum in a list.

n = int(input('Enter how many numbers ? '))
l = []
print('Enter numbers one by one : ')
for x in range(n):
    m = int(input('Enter number : '))
    l.append(m)
    
print('Original List is : ', l)

l.sort() # modifies existing list object content
print('Sorted List is : ', l)

print('Maximum element is : {}'.format(l[-1]))
print('2nd Maximum element is : {}'.format(l[-2]))

print('Minimum element is : {}'.format(l[0]))
print('2nd minimum element is : {}'.format(l[1]))


# sorted_list = sorted(l) # creates a new object sorted_list
# print('Sorted List is : ', sorted_list) # sort in ascending order

# print('Maximum element is : {}'.format(sorted_list[-1]))
# print('2nd Maximum element is : {}'.format(sorted_list[-2]))

# print('Minimum element is : {}'.format(sorted_list[0]))
# print('2nd minimum element is : {}'.format(sorted_list[1]))




# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\2ndhighestand2ndlowest.py
# Enter how many numbers ? 6
# Enter numbers one by one :
# Enter number : 1
# Enter number : -1
# Enter number : 2
# Enter number : 90
# Enter number : 100
# Enter number : -100
# Original List is :  [1, -1, 2, 90, 100, -100]
# Sorted List is :  [-100, -1, 1, 2, 90, 100]
# Maximum element is : 100
# 2nd Maximum element is : 90
# Minimum element is : -100
# 2nd minimum element is : -1




# PS C:\Users\RAMANATH\Documents\PythonPrograms\iMPORTANT> py .\2ndhighestand2ndlowest.py
# Enter how many numbers ? 6
# Enter numbers one by one : 
# Enter number : 11
# Enter number : 21
# Enter number : 8
# Enter number : 7
# Enter number : 25
# Enter number : 100
# Original List is :  [11, 21, 8, 7, 25, 100]
# Sorted List is :  [7, 8, 11, 21, 25, 100]
# Maximum element is : 100
# 2nd Maximum element is : 25
# Minimum element is : 7
# 2nd minimum element is : 8
