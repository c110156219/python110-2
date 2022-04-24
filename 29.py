#洗刷刷
a=list(input("甲方的數字:"))
b=list(input("乙方的數字:"))
c=[]
for i in range(len(a)):
    if a[i]=="1" and b[i]=="5":
        c.append("贏")
    elif a[i]=="2" and b[i]=="1":
        c.append("贏")
    elif a[i]=="3" and b[i]=="2":
        c.append("贏")
    elif a[i]=="4" and b[i]=="3":
        c.append("贏")
    elif a[i]=="5" and b[i]=="4":
        c.append("贏")
    elif a[i]=="5" and b[i]=="1":
        c.append("輸")
    elif a[i]=="2" and b[i]=="3":
        c.append("輸")
    elif a[i]=="2" and b[i]=="3":
        c.append("輸")
    elif a[i]=="3" and b[i]=="4":
        c.append("輸")
    elif a[i]=="4" and b[i]=="5":
        c.append("輸")
    else:
        c.append("和")
ans=""
for i in range(len(c)):
    ans+=c[i]
print(ans)