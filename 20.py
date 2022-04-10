#電影票購買計算
a=int(input("組數為:"))
for i in range(a):
    b=list(input("第"+str(i+1)+"組:").split())
    print("第"+str(i+1)+"組應收費用:",int(b[0])*250+int(b[1])*175)