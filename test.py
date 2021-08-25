from UsageTest import UsageTest as bert
from cra import cra as ca
from FinalOutputInApp import main as Fop
from PhotoOutput import photo as ph
from data_processing import data_processing as dp
li=ca.cra('https://www.irentcar.com.tw/privacy.html')
bert_li=bert.usagetest(li)
Fop.getListToCreatePic(li,bert_li)

