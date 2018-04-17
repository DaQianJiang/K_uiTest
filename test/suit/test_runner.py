import os
from utils.config import BASE_PATH
import unittest
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email

REPORT_PATH = os.path.join(BASE_PATH,'report')
report = REPORT_PATH+r'\report.html'
fp = open(report,'wb')
case_path = os.path.join(BASE_PATH,r'test\case')
suite = unittest.TestLoader().discover(case_path)

if __name__=='__main__':

    runner = HTMLTestRunner (stream=fp,verbosity=2,title='幼儿园交流平台测试报告',description='登录测试')
    runner.run(suite)
    email = Email(path=report)
    email.send()

