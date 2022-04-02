#字元出現次數
from tkinter import E


while True:
    a=0
    b=input("檢測的字元(end結束):")
    if b=="end":
        print("檢測結束")
        break
    else:
        b=list(b)
        c=input("檢測的字元:")
        for i in range(len(b)):
            if c==b[i]:
                a+=1
        print("字元",c,"出現的次數為:",a)