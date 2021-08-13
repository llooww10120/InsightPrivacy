import csv, os
from tqdm import tqdm

def readTable():
    with open(os.path.join('data_processing', 'table.csv'), newline='',encoding="utf-8-sig") as f:
        
        rows = csv.reader(f)
        table = []

        for row in rows:
            for element in row:
                table.append(element)
        return table

def compare(line, table):
    s = []
    output = []
    for item in range(len(table)):
        if table[item] in line:
            s.append(line.find(table[item]))
        else:
            s.append(-1)
    sorted_s = sorted(range(len(s)), key = lambda k : s[k]) 
    for num in sorted_s:
        if s[num] > 0:
            output.append(table[num])
    # print(output)
    return output


if __name__=="__main__":
    table = readTable()

    files = next(os.walk(os.path.join('cra', 'result')))[2]
    for fl in tqdm(files, desc='conver to csv'):
        # print(fl)
        with open(os.path.join('data_processing', 'csv', '{}.csv'.format(fl[:3])), 'w', newline='', encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            lines = open(os.path.join('cra', 'result', fl),'r', encoding='utf-8-sig').read().split('\n')
            # lines = lines.replace('。', '\n')
            for line in lines:
                if line == '':
                    continue
                else:
                    writer.writerow([line, compare(line, table), 0])
