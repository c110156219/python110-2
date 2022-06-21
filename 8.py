#檢查數值有無重複
num = int(input("輸入第一行正整數:"))
num1 = input("第二行中數列的數字:").split()
tmp=[]
for i in range(num):
    c = 0
    for j in range(num):
        if num1[i] == num1[j]:
            c += 1
    tmp.append(c)
if sum(tmp) == num:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數為",num1[tmp.index(max(tmp))])
    print()
    print("出現次數為",max(tmp))
