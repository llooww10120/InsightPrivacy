from UsageTest import UsageTest as bert
from cra import cra as ca
from FinalOutputInApp import main as Fop
from PhotoOutput import photo as ph
from data_processing import data_processing as dp
import Upload2Imgur as upi
def ImageOutput(url):
    li=ca.cra(url)
    bert_li=bert.usagetest(li)
    Fop.getListToCreatePic(li,bert_li)
    ph.CreatePic(dp.data_processing(li))
    return [upi.upload2imgur("Output.jpg","Output"),upi.upload2imgur("result.jpg","result")]
if __name__=="__main__":
    link=ImageOutput("https://www.irentcar.com.tw/privacy.html")
    print(link[0])