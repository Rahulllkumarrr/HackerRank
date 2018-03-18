case=int(input())
for i in range(case):
    prince,hurdles=map(int,input().strip().split())
    maxjumplist=[int(x) for x in input().split()]
    maxjumper=max(maxjumplist)
    hurdle=[int(x) for x in input().split()]
    maxhurdle=max(hurdle)
    winner=0
    while True:
        if maxjumper<maxhurdle:
            hurdle.remove(max(hurdle))
            maxhurdle=max(hurdle)
        else:
            break
    for i in maxjumplist:
        if i >= maxhurdle:
            break
        else:
            winner += 1
    print(winner)
