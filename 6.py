#兩數差值
num=input("輸入數值:").split(",")
num1=''
num2=''
num_int=list(map(int,num))
num_int.sort()
num_int=list(map(str,num_int))
for i in range(len(num)):
    num1+=num_int[i]
num_int=list(map(int,num_int))
num_int.reverse()
num_int=list(map(str,num_int))
for i in range(len(num)):
    num2+=num_int[i]
num1,num2=int(num1),int(num2)
print("最大值數列與最小值數列差值為",num2-num1)