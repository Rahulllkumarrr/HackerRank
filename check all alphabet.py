case=int(input())
setalpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(case):
    string1=str(input())
    list=[str(i) for i in string1]
    print(list)
    list=set(list)
    print(list)
    list=sorted(list,key=str.lower)
    print(list)
    if setalpha==list:
        print("YES")
    else:
        print("NO")