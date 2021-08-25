from UsageTest import UsageTest as bert
from cra import cra as ca
from FinalOutputInApp import main as Fop
from PhotoOutput import photo as ph
from data_processing import data_processing as dp
li=ca.cra('https://policies.google.com/privacy?hl=zh-TW')
# a=bert.usagetest(li)
# ph.CreatePic(dp.data_processing(li))
print(li)
