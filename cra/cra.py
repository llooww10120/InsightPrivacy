from os import write
import requests
from bs4 import BeautifulSoup
import re

# def savetxt(output):
#     out=[]
#     if output.find('隱私') != -1 or output.find('隐私') != -1:
#         head = max(output.find('隱私'), output.find('隐私'))
#     else:
#         head = 0

#     if output.rfind('聯絡') != -1 or output.rfind('聯繫') != -1 or output.rfind('通知'):
#         tail = max(output.rfind('聯絡'), output.rfind('聯繫'), output.rfind('通知'))    
#     else:
#         tail = len(output)
#     for i in output:
#         out.append(str(i)[3:-4])

def cra(url):
    out=[]
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    sp = BeautifulSoup(html.text, 'html.parser')
    try:
        output = sp.find_all("p")
        for i in output:
            out.append(i.string)
        a=list(filter(None,out))
        with open('test.txt' , 'w' , encoding='utf-8') as f:
            f.write("\n".join(a))
        return a
    except:
        print("error") 
        return out
        
if __name__=="__main__":
    url = input()
    if url!='exit':
        cra(url)
    
