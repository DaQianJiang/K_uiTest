#封装浏览器类,定义浏览器的一些方法,打开浏览器，关闭、后退
from selenium import webdriver
import time
import os
from utils.config import BASE_PATH
from utils.log import Logger


TYPES=['firefox','ie','chrome']
REPORT_PATH = os.path.join(BASE_PATH,'report')
#DRIVER_PATH= os.path.join(BASE_PATH,'drivers')
#CHROMEDRIVER_PATH= os.path.join(DRIVER_PATH,'chromedriver.exe')
#IEDRIVER_PATH= os.path.join(DRIVER_PATH,'IEDriverServer.exe')

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self,browser_name='firefox'):
        self.logger = Logger("Browser").get_log()
        if browser_name.lower() in TYPES:
            self.browser_type=browser_name
        else:
            raise UnSupportBrowserTypeError('浏览器类型不存在，仅支持浏览器类型包括%s'%','.join(TYPES[:]))
        #确定webdriver
        if self.browser_type =='firefox':
            self.driver = webdriver.Firefox()
        elif self.browser_type=='ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
    #打开浏览器
    def open_browser(self,url,implicitly_wait=5,maxinize_window=True):
        self.driver.get(url)
        if maxinize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
    #截并保存至相应文件夹
    def save_screen_picture(self,name='screen_shot'):
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        screen_path= REPORT_PATH +r'\screen_picture_%s'%day
        if not os.path.exists(screen_path):
            os.makedirs(screen_path)
        tm = time.strftime('%H-%M-%S',time.localtime(time.time()))
        screen_picture = self.driver.get_screenshot_as_file(screen_path+'\\%s_%s.png'%(name,tm))
        return screen_picture
    #关闭页面
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()
    def forward(self):
        self.driver.forward()
    def back(self):
        self.driver.back()
    def wait(self,second):
        self.driver.implicitly_wait(second)
# if __name__=='__main__':
#     browser = Browser(browser_name='firefox')
#     browser.open_browser(url='https://www.baidu.com/',implicitly_wait=30,maxinize_window=True)
#     browser.save_screen_picture()
#     time.sleep(5)
#     #browser.close()
#     browser.quit()



