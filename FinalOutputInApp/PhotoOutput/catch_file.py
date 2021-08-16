import csv, os

if __name__ == "__main__":
    # 開啟 CSV 檔案
    files = next(os.walk(os.path.join('data_processing', 'csv')))[2]
    for fl in files:
        with open(os.path.join('data_processing', 'csv', '{}.csv'.format(fl[:3])), 'r', newline='', encoding="utf-8-sig") as f:
            print(format(fl[:3]))
            # 讀取 CSV 檔案內容
            rows = csv.reader(f)
            for row in rows:
                if (row[1] != '[]'):
                    #把string的樣子lsit轉成真的list
                    print(eval(row[1]))
