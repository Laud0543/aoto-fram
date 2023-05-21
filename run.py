import unittest
import time
from utils import HTMLTestRunner_cn
from project_name.suite import Case_Suite
import os
from config import REPORTPATH
from utils.mail import Email


# from news.test_hot_news import test_News
# dicsover方法查找用例
# 2.TextTestRunner运行用例
# runer = unittest.TextTestRunner()
# runer.run(suite)

suite = Case_Suite()

# nowtime=time.strftime("%Y-%m-%d %H.%M.%S")
# parent_dir= 'D:\\python_file\\auto_fram_5.9\\output\\report\\'
# filename=parent_dir+nowtime+" result.html"
# # fp=file(filepath,"wb")

report_path = REPORTPATH
now = time.strftime('%Y-%m-%d %H-%M-%S')
filename = os.path.join(report_path, now + 'report.html')

if __name__ == '__main__':
    with open(filename, 'wb') as f:
        # suite=unittest.TestSuite()
        # suite.addTest(unittest.makeSuite(test_News))

        # suite = unittest.defaultTestLoader.discover("project_name/testcase", "test*.py")
        runner = HTMLTestRunner_cn.HTMLTestRunner(
            stream=f,
            title=u"测试报告",
            description=u"测试结果如下")
        runner.run(suite)

    e = Email(title='百度搜素测试报告',
                  message='这是今天的测试报告，请查收！',
                  receiver='',
                  server='',
                  sender='',
                  password='',
                  path=filename
                  )
    e.send()


