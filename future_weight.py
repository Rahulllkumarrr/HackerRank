case=int(input())
answer=[]
for i in range(case):
    N=int(input())
    list=[]
    for i in range(N):
        inp=int(input())
        list.append(inp)
    iter = len(list)
    start=1

    for z in list:
        count = 0
        for i in range(start,iter,1):
            if list[i]<z:
                count+=1
                iter=iter-1
                start+=1
        answer.append(count)
    print(*answer)
