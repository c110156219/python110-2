# 摩斯密碼
sa = list(input("請輸入密碼 : ").split())
data = {
    '-----':'0',
    '.----':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
}
for i in range(len(sa)):
    if sa[i] in data:
        print(data[sa[i]],end="")
    else:
        print("錯誤")