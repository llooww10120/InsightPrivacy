import re
li=[]
with open("cra/result/021.txt","r",encoding='utf-8') as f:
    a=f.readlines()
for i in a:
    if  "圖片" in i or "照片" in i:
        li.append(a.index(i))

print(li)
