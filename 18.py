#撲克牌13點
a=list(input("輸入五張牌:").split())
sum=0
for i in range(len(a)):
    if a[i]=="A":
        sum+=1
    elif a[i]=="J":
        sum+=11
    elif a[i]=="Q":
        sum+=12
    elif a[i]=="K":
        sum+=13
    else:sum+=int(a[i])
print(sum)