#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains

import ClassCongregation
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [AfterLogicWebMailArbitraryFileContains.medusa(Url,RandomAgent,ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="AfterLogicWebMail plugin progress"):
            WriteFile.Write(str(i))
    except:
        pass