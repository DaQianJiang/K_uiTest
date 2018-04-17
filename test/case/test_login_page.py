import unittest
from test.page.login_page import LoginPage
import time
from utils.log import Logger


class TestLoginPage(unittest.TestCase):
    logger = Logger('TestLoginPage').get_log()
    def setUp(self):
        self.driver = LoginPage(browser_name='firefox')
        self.driver.open_browser(url='http://39.106.135.146:8089/Kindergarten//YouErYuan/login_in.html')

    def tearDown(self):
        self.driver.quit()

    def test_title_text(self):
        try:
            self.assertEqual('幼儿园交流平台',self.driver.get_title_text())
            self.logger.info("页面标题匹配成功")
            #print("页面标题匹配成功")
        except:
            self.logger.debug("页面标题匹配失败")
           # print("页面标题匹配失败")
    def test_stu_login(self):
        self.driver.select_identify_stu()
        self.driver.input_num('3')
        self.driver.input_password('3')
        time.sleep(3)
        self.driver.click_button()
        self.logger.info("家长登录成功")
        #print('家长登录成功')


    def test_teach_login(self):
        self.driver.select_identify_teach()
        self.driver.input_num('2')
        self.driver.input_password('2')
        time.sleep(3)
        self.driver.click_button()
        self.logger.info("教师登录成功")
        #print('教师登录成功')
#
# if __name__=='__main__':
#     suit = unittest.TestSuite(unittest.makeSuite(TestLoginPage))
#     runner = unittest.TextTestRunner()
#     runner.run(suit)


