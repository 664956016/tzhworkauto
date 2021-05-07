import os
from openpyxl import Workbook
from datetime import datetime

os.chdir(r"F:\2021零件申购")
today = str(datetime.today().date()).replace('-', '.')
if not os.path.exists(today):
    os.mkdir(today)
    print(f"{today} dir exists")
print(f"mkdir: {today}")

os.chdir(today)
print(f"当前工作区：${os.getcwd()}")
if not os.path.exists('报价'):
    os.mkdir('报价')

title_list = ['低温车间设备物料申请c', '常温车间设备物料申请c', '中控车间设备物料申请c', '立库外围设备物料申请c', '公用工程间设备物料申请c']
title_lists = [today+i+'.xlsx' for i in title_list]
print(title_lists)

for filename in title_lists:
    wb = Workbook()
    if not os.path.exists(filename):
        wb.save(filename)
        print(f"新建excel file{filename}") 
    print(f"{filename}已经存在")
input("good, ke按任何键结束。。。。。。。。。。")
    


