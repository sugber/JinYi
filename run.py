import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email
logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover("./")

fp = open(report_file, 'wb')
runner = HTMLTestRunner(stream=fp,
                        title='爱租机接口自动化测试',
                        description='运行环境：MySQL(PyMySQL), Requests, unittest ')
runner.run(suite, rerun=0, save_last_run=False)
fp.close()

send_email(report_file)  # 发送邮件
logging.info("================================== 测试结束 ==================================")