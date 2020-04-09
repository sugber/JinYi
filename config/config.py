import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(funcName)s %(filename)s %(lineno)d %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    filename=r'C:\Users\dell\PycharmProjects\JinYi\log\log.txt',
    filemode='a'
)


data_file = r'C:\Users\dell\PycharmProjects\JinYi\data\TestData.xlsx'


# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '13166661519@163.com'
smtp_password = 'OQPCJZPTVDJGEGWI'

sender = smtp_user  # 发件人
receiver = 'chengyongda@woaizuji.com'  # 收件人
subject = '接口测试报告'  # 邮件主题