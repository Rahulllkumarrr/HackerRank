list1 = [".", "a", "d", "g", "j", "m", "p", "t", "w", "_"]
list2 = [",", "b", "e", "h", "k", "n", "q", "u", "x", "0"]
list3 = ["?", "c", "f", "i", "l", "o", "r", "v", "y"]
list4 = ["!", "2", "3", "4", "5", "6", "s", "8", "z "]
list5 = ["1", "7", "9"]
case = int(input())
for i in range(case):
    time = 0
    string = input()
    key=1
    list =[str(i) for i in str(string)]
    for i in range(len(list)):
        if list[i] in list1:
            if key==1:
                time+=1
            else:
                key=1
                time+=2
        elif list[i] in list2:
            if key==2:
                time+=2
            else:
                key=2
                time+=3
        elif list[i] in list3:
            if key==3:
                time+=3
            else:
                key=3
                time+=4
        elif list[i] in list4:
            if key==4:
                time+=4
            else:
                key=4
                time+=5
        elif list[i] in list5:
            if key==5:
                time+=5
            else:
                key=5
                time+=6
        print(time)
    print(time)
