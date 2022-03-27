#通話費率
money,time=input("輸入月駔費形式及通話時間:").split(",")
time=int(time)
if money=="186":
    money2=time*0.09
    if 186>money2>=186*2:
        print("通話費為:",round(money2*0.9,1))
    elif money>186*2:
        print("通話費為:%.1f"%(money2*0.8))
    else:
        print(money2)
elif money=="386":
    money2=time*0.08
    if 386>money2>=386*2:
        print("通話費為:%.1f"%(money2*0.8))
    elif money2>286*0.2:
        print("通話費為:%.1f"%(money2*0.7))
    else:
        print(money2)
elif money=="586":
    money2=money*0.07
    if 586>money2>=586*2:
        print("通話費為:%.1f"%(money2*0.7))
    elif money2>586*2:
        print("通話費為:%.1f"%(money2*0.6))
    else:
        print(money2)
elif money=="986":
    money2=money*0.06
    if 986>money2>=986*2:
        print("通話費為:%.1f"%(money2*0.6))
    elif money2>986*2:
        print("通話費為:%.1f"%(money2*0.5))
    else:
        print(money2)