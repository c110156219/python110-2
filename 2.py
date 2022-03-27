#2計算電費
a=int(input("輸入度數:"))
if a<=120:
    print("Summer months:%.2f"%(a*2.10))
    print("Non-summer minths:%.2f"%(a*2.10))
elif 121<=a<=330:
    print("Summer months:%.2f"%(120*2.10+(a-120)*3.02))
    print("Non-summer minths:%.2f"%(120+2.10+(a-120)*2.68))
elif 331<=a<=500:
    print("Summer months:%.2f"%(120*2.10+(330-120)*3.02+(a-330)*4.39))
    print("Non-summer minths:%.2f"%(120*2.10+(330-120)*2.68+(a-330)*3.61))
elif 501<=a<=700:
    print("Summer months:%.2f"%(120*2.10+(330-120)*3.02+(500-330)*4.39+(a-500)*4.97))
    print("Non-summer minths:%.2f"%(120*2.10+(330-120)*2.68+(500-330)*3.61+(a-500)*4.01))
else:
    print("Summer months:%.2f"%(120*2.10+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a-700)*5.63))
    print("Non-summer minths:%.2f"%(120*2.10+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(a-700)*4.50))