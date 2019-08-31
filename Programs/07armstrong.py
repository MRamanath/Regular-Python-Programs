# Armstrong number check

def armstrong(num):
    order = len(str(num))
    temp = num
    rev = 0
    while temp != 0:
        rem = temp % 10
        rev = rev + rem ** order
        temp = temp // 10
    if rev == num:
        return rev
    else:
        return 0

x, y = [int(i) for i in input('Enter lower and upper range : ').split()]
for m in range(x, y+1):
    if armstrong(m) != 0:
        print(m)

# Enter lower and upper range : 100 2000
# 153
# 370
# 371
# 407
# 1634