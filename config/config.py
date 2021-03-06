import logging
import os
import time

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_file = os.path.join(prj_path,'report', now + '_aizuji.html')
data_file = os.path.join(prj_path,'data', 'TestData.xlsx')
# data_file = r'..\JinYi\data\TestData.xlsx'
filename = os.path.join(prj_path, 'log', 'log.txt')



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(funcName)s %(filename)s %(lineno)d %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    filename=filename,
    filemode='a'
)



# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '13166661519@163.com'
smtp_password = 'OQPCJZPTVDJGEGWI'

sender = smtp_user  # 发件人
receiver = 'chengyongda@woaizuji.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

