#迴文問題
a=input("輸入一字元為:")
if a[::-1]==a:
    print("YES")
else:
    print("NO")