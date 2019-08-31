# Sum of list of elements.

n = int(input('How many elements ? '))
list = []

for x in range(n):
    print('Enter elements : ', end = ' ')
    list.append(int(input()))
print(list)

sum = 0
for i in list:
    sum = sum + i
print(sum)

# How many elements ? 5
# Enter elements :  12
# Enter elements :  23
# Enter elements :  11
# Enter elements :  45
# Enter elements :  90
# [12, 23, 11, 45, 90]
# 181