import requests
from bs4 import BeautifulSoup

def cra(url):
    out = []
    USER_AGENT_VALUE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent': USER_AGENT_VALUE}
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    sp = BeautifulSoup(html.text, 'html.parser')
    try:
        # case1: search "p" first
        output = sp.findAll("p")
        for i in output:
            out.append(''.join(i.findAll(text=True)))
        out_text = "\n".join(out)
        out_text = out_text.replace('。', '。\n')
        final_out_text = out_text.split('\n')

        # case2: except case
        if(len(out_text) < 700):
            # print('case2')
            out_text = sp.body.text  # catch all text
            # add new line after period
            out_text = out_text.replace('。', '。\n')
            final_out_text = out_text.split('\n')
        
        # remove empty row
        try:
            while True:
                final_out_text.remove('')
        except ValueError:
            pass
        # remove only one space row
        try:
            while True:
                final_out_text.remove(' ')
        except ValueError:
            pass

        try:
            while True:
                final_out_text.remove('\r')
        except ValueError:
            pass

        try:
            while True:
                final_out_text.remove('\t')
        except ValueError:
            pass

        return final_out_text

    except:
        final_out_text = 'error'

        return final_out_text

# if __name__ == "__main__":
#     list = cra('https://www.lungyengroup.com.tw/Page/privacypolicy')
#     table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     count = 0
#     for i in range(0, len(list)):
#         if table[i] == 1:
#             count = count + 1
#             print(count, list[i])
