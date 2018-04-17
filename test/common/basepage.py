#封装basepage类，封装一些基本方法，且继承于Browser,继承其方法等
from test.common.browser import Browser
from selenium.common.exceptions import NoSuchElementException
from utils.log import Logger


class BasePage(Browser):
    logger = Logger('BasePage').get_log()
    def get_driver(self):
        return self.driver
    def find_element(self,*args):
        try:
            return self.driver.find_element(*args)
        except NoSuchElementException:
            self.logger.debug('没有找到相关元素')
            #print('没有找到相关元素')
    def find_elements(self,*args):
        try:
            return self.driver.find_elements(*args)
        except NoSuchElementException:
            self.logger.debug('没有找到相关元素')
            #print('没找到相关元素')
    def click(self,element):
        try:
            self.find_element(element).click()
        except NameError:
            self.logger.debug('点击元素失败，发生异常')
            #print('点击元素失败，发生异常')
    def page_title(self):
        return self.driver.title
    def page_url(self):
        return self.driver.current_url


# if __name__=='__main__':
#     page = BasePage(browser_name='firefox')
#     page.open_browser(url='http://39.106.135.146:8089/Kindergarten//YouErYuan/login_in.html')
#     page.save_screen_picture()
#     print(page.page_title())
#     page.quit()