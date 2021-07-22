from collections import UserList
import os
import requests
from bs4 import BeautifulSoup

def cra(url, count):
    out=[]
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    sp = BeautifulSoup(html.text, 'html.parser')
    try:
        # case1: search "p" first
        output = sp.findAll("p")
        for i in output:
            out.append(''.join(i.findAll(text = True)))
        out_text = "\n".join(out)

        # case2: except case
        if(len(out_text) < 400):
            out_text = sp.text  #catch all text
            out_text = out_text.replace('。', '。\n')   # use to add new line after period

        # format file name
        with open(os.path.join('cra', 'result', 'test{:02d}.txt'.format(count)), 'w' , encoding='utf-8') as f:
            f.write(out_text)
        return out

    except:
        with open(os.path.join('cra', 'result', 'test{:02d}.txt'.format(count)), 'w' , encoding='utf-8') as f:
            f.write('error') 
        return out
        
if __name__=="__main__":
    count = 0

    # privacy link test
    fp = open(os.path.join('cra', 'privacy_link.txt'), 'r')
    for file in fp.readlines():
        url = file.strip()
        count = count + 1
        cra(url, count)

    # user input url
    # url = input()
    # if url!='exit':
    #     count = count + 1
    #     cra(url, count)
    
