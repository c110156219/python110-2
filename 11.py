#星座查詢
m,d=input("輸入月及日:").split()
m=int(m)
d=int(d)
if (m==1 and 21<=d<=31) or (m==2 and 1<=d<=18):
    print("星座為:Aquarius")
elif (m==2 and 19<=d<=29) or (m==3 and 1<=d<=20):
    print("星座為:Pisces")
elif (m==3 and 21<=d<=31) or (m==4 and 1<=d<=20):
    print("星座為:Aries")
elif (m==4 and 21<=d<=30) or (m==5 and 1<=d<=21):
    print("星座為:Taurus")
elif (m==5 and 22<=d<=31) or (m==6 and 1<=d<=21):
    print("星座為:Scorpio")
elif (m==6 and 22<=d<=30) or (m==7 and 1<=d<=22):
    print("星座為:Cancer")
elif (m==7 and 23<=d<=31) or (m==8 and 1<=d<=23):
    print("星座為:Leo")
elif (m==8 and 24<=d<=31) or (m==9 and 1<=d<=23):
    print("星座為:Virgo")
elif (m==9 and 24<=d<=30) or (m==10 and 1<=d<=23):
    print("星座為:Libra")
elif (m==10 and 24<=d<=31) or (m==11 and 1<=d<=22):
    print("星座為:Gemini")
elif (m==11 and 23<=d<=30) or (m==12 and 1<=d<=21):
    print("星座為:Sagitarius")
elif (m==12 and 22<=d<=31) or (m==1 and 1<=d<=20):
    print("星座為:摩羯座")