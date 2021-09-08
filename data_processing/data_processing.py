
def data_processing(list):
    # table = [
    #     [ '聯絡資訊', '住址', '工作地址', '以前地址', '住家電話號碼', '行動電話'],
    #     [ '即時通帳號', '網路平臺申請之帳號', '通訊及戶籍地址', '相片', '指紋'],
    #     [ '電子郵遞地址', '電子簽章', '憑證卡序號', '憑證序號'],
    #     [ '提供網路身分認證或申辦查詢服務之紀錄', '電子信箱'],
    #     [ '財務資訊', '金融機構帳戶之號碼與姓名'],
    #     [ '信用卡或簽帳卡之號碼', '保險單號碼', '個人之其他號碼或帳戶'],
    #     [ '姓名', '生日', '名字'],
    #     [ '身分證號', '統一編號', '身分證統一編號', '統一證號', '稅籍編號', '保險憑證號碼'],
    #     [ '殘障手冊號碼', '退休證之號碼', '證照號碼', '護照號碼', '身分證字號'],
    #     [ '瀏覽資訊IP位址', '設備資訊', '藍芽聯絡人', '郵遞區號', '手機製造商', '手機型號', 'UDID']
    # ]
    table = [
        ['電話號碼', '個人檔案', '顯示姓名', '個人圖片', '生日'],
        [ '文字', '圖片', '影片','通訊錄', '使用頻率','裝置類型','購買紀錄位置資訊'],
        [ '辨識裝置/瀏覽器用的廣告識別碼', '作業系統'],
        [ '語言', '時區','應用程式(Apps)版本','電信營運商名稱'],
        [ '使用位置', '造訪紀錄','造訪相關網站的紀錄'],
        ['瀏覽器類型','IP位置','Cookie識別碼'],
        ['封面照片', '狀態消息', '用戶ID', 'LINE ID'],
        ['外部社群媒體帳號識別碼'],
        
    ]
    count=[]
    output_list=[]
    for i in range(len(table)):
        count.append([0 for _ in range(len(table[i]))])
        output_list.append([])
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
    


if __name__ == "__main__":
    print()