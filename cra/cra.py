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

        return final_out_text

    except:
        final_out_text = 'error'

        return final_out_text

if __name__ == "__main__":

    cra(input())
    
    # privacy link test
    # fp = open(os.path.join('cra', 'privacy_link.txt'), 'r')
    # for file in tqdm(fp.readlines(), desc='Browsing'):
    #     url = file.strip()
    #     count = count + 1
    #     with open(os.path.join('cra', 'result', '{:03d}.txt'.format(count)), 'w' , encoding='utf-8') as f:
    #         # print(count)
    #         f.write(cra(url))

    # user input url
    # url = input()
    # if url!='exit':
    #     count = count + 1
    #     cra(url, count)
