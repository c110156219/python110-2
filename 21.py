#學生資料搜尋
a=input("輸入查詢學號為:")
b=[["123","Tom DTGD"],["456","Cat CSIE"],["789","Nana ASIE",["321","Lim DBA"],"654","Won","FDD"]]
for i in range(len(b)):
    if a==b[i][0]:
        print("學生資料為",a,b[i][1])