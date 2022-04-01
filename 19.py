a=int(input("測試的資料量(大寫):"))
for i in range(a):
    b,c,d=input("輸入血型").split()
    if b=="O" or c=="O":
        if d=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif b=="O":
        if c=="A":
            if d=="A" or d=="O":
                print("YES")
            else:
                print("IMPOSSIBLE")
        elif c=="B":
            if d=="B" or d=="O":
                    print("YES")
            else:
                print("IMPOSSIBLE")
        elif c=="AB":
            if d=="A" or d=="B":
                    print("YES")
            else:
                print("IMPOSSIBLE")
    elif b=="A":
        if c=="A":
            if d=="A" or d=="O":
                    print("YES")
            else:
                print("IMPOSSIBLE")
        elif c=="B":
            print("YES")
        elif c=="AB":
            if d=="A" or d=="B" or d=="AB":
                    print("YES")
            else:
                print("IMPOSSIBLE")
    elif b=="B":
        if c=="B":
            if d=="O" or d=="B":
                    print("YES")
            else:
                print("IMPOSSIBLE")
        elif c=="AB":
            if d=="A" or d=="B" or d=="AB":
                    print("YES")
            else:
                print("IMPOSSIBLE")
    elif b=="AB":
        if c=="AB":
            if d=="A" or d=="B" or d=="AB":
                    print("YES")
            else:
                print("IMPOSSIBLE")