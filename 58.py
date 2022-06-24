# 判斷串列數字大小
data = []
for i in range(10):
    data.append(int(input("請輸入第"+str(i+1)+"個數字 : ")))
data.sort()
for i in range(9,6,-1):
    if i == 9 :
        print("最大的三個數字: "+str(data[i]) ,end="")
    else :
        print(","+str(data[i]) ,end="")
print()
for i in range(2,-1,-1):
    if i == 2:
        print("最小的三個數字: "+str(data[i]) ,end="")
    else :
        print(","+str(data[i]) ,end="")

    