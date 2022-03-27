#字根與字串
s1=input("輸入s1:")
s2=input("輸入s2:")
if len(s1)>len(s2):
    if (s1 in s2) or (s2 in s1):
        print("yes")
    else:
        print("no")
if len(s1)<len(s2):
    if (s1 in s2) or (s2 in s1):
        print("yes")
    else:
        print("no")
if len(s1)==len(s2):
    if (s1 in s2) or (s2 in s1):
        print("yes")
    else:
        print("no")