import math
case=int(input())
for i in range(case):
    num=0
    inp=int(input())
    for i in range(1, int(math.sqrt(inp)) + 1):
        if inp%i==0:
            if inp//i==i:
                num+=1
            else:
                num+=2
    print(num)