#販賣機
a = int(input("請輸入小明現在有多少錢:"))
b = int(input("請輸入販賣機有幾種飲料:"))
price = []
can = 0
for i in range(b):
    price.append(int(input("請輸入第"+str(i+1)+"種飲料的價錢")))
    if price[i] <= a :
        can += 1

print("小明可以買",can,"種飲料")
