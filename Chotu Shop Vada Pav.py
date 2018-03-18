case=int(input())
list=[]
for i in range(case):
    inp=input()
    list.append(inp)
list=sorted(list, key=str.lower)
set=set(list)
set=sorted(set,key=str.lower)
print(set)
print(len(set))
for z in set:
    print(z)