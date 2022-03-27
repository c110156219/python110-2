#階層判斷
m=int(input("請輸入階層值M:"))
total=i=1
while (m>total):
    i+=1
    total*=i
print("超過M為",m,"的最小階層N值為:",i)