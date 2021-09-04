
def data_processing(list):
    table = [
        ['聯絡資訊', '住址', '工作地址', '以前地址', '住家電話號碼', '行動電話'],
        [ '即時通帳號', '網路平臺申請之帳號', '通訊及戶籍地址','相片', '指紋'],
        [ '電子郵遞地址', '電子簽章', '憑證卡序號', '憑證序號'],
        [ '提供網路身分認證或申辦查詢服務之紀錄', '電子信箱'],
        ['財務資訊', '金融機構帳戶之號碼與姓名'],
        [ '信用卡或簽帳卡之號碼', '保險單號碼', '個人之其他號碼或帳戶'],
        ['姓名', '生日', '名字'],
        ['身分證號', '統一編號', '身分證統一編號', '統一證號', '稅籍編號', '保險憑證號碼'],
        ['殘障手冊號碼', '退休證之號碼', '證照號碼', '護照號碼', '身分證字號'],
        ['瀏覽資訊IP位址', '設備資訊', '藍芽聯絡人', '郵遞區號', '手機製造商', '手機型號', 'UDID']
    ]
    count = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    output_list = [
        [],
        [],
        [],
        [],
        []
    ]
    for line in list:
        for row in range(0, len(table)):
            for col in range(0, len(table[row])):
                if table[row][col] in line:
                    count[row][col] = count[row][col] + 1

    for row in range(0, len(count)):
        for col in range(0, len(count[row])):
            if count[row][col] > 0:
                output_list[row].append(table[row][col])
    
    return output_list
    


# if __name__ == "__main__":
#     print(data_processing())