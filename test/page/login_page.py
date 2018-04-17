from test.common.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.log import Logger

class LoginPage(BasePage):
    logger = Logger( "LoginPage").get_log()
    page_title=(By.XPATH,'//div[@class="form_center"]//h2')
    select_button =(By.ID,'userType')
    number_input= (By.XPATH,'//input[@id="userAccount"]')
    password_input = (By.XPATH,'//input[@id="password1"]')
    login_button = (By.ID,'login_btn')
    error_message = (By.XPATH,'//div[@class="dialog_content"]/span[@class="message_info"]')
    #获取页面标题
    def get_title_text(self):
        return self.find_element(*self.page_title).text
    #选择家长下拉框
    def select_identify_stu(self):
        try:
            stu = Select(self.find_element(*self.select_button))
            stu.select_by_visible_text('家长')
            self.logger.info('家长按钮选择成功')
            #print('家长按钮选择成功')
        except Exception as e:
            self.logger.debug("Exception is",format(e))
            #print("Exception is",format(e))
    #选择教师下拉框
    def select_identify_teach(self):
        try:
            stu = Select(self.find_element(*self.select_button))
            stu.select_by_visible_text('教师')
            self.logger.info('教师按钮选择成功')
            #print('教师按钮选择成功')
        except Exception as e:
            self.logger.debug("Exception is", format(e))
            #print("Exception is",format(e))
    #输入学号/职工号
    def input_num(self,usernum):
        self.find_element(*self.number_input).send_keys(usernum)
    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_input).send_keys(password)
    #点击登录按钮
    def click_button(self):
        self.find_element(*self.login_button).click()
    #获取错误提示信息
    def get_erro_message(self):
        return self.find_element(*self.error_message).text



