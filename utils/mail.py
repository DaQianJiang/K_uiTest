import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.log import Logger
import os
import re


class Email(object):
    logger = Logger('Email').get_log()
    def __init__(self,path):
        self.sender = '1404482005@qq.com'
        self.receiver = '1404482005@qq.com'
        self.password = 'pfoozuyovftobaca'
        self.message = '幼儿园交流平台测试报告'
        self.title = '测试报告结果'
        self.server = 'smtp.qq.com'
        self.path = path
        self.msgRoot = MIMEMultipart('related')

    def attach_file(self, att_file):
        if os.path.isdir(att_file):
            for f in os.listdir(att_file):
                path = os.path.join(att_file, f)
                # print('f 的类型%s',type(f))
                if f.endswith(('.xlsx', '.py')):
                    msgFile = MIMEText(open(f, "rb").read(), "base64", "utf-8")
                else:
                    msgFile = MIMEText(open(path).read())
                msgFile["Content-Type"] = 'application/octet-stream'
                msgFile["Content-Disposition"] = 'attachment; filename=' + f
                self.msgRoot.attach(msgFile)
                self.logger.info('att_file {} is '.format(path))
        elif os.path.isfile(att_file):
            fname = re.split(r'[\\|/]', att_file)
            if fname[-1].endswith(('.xlsx', '.py')):
                msgFile = MIMEText(open(att_file, "rb").read(), "base64", "utf-8")
            else:
                msgFile = MIMEText(open('%s' % att_file, 'r', encoding='utf-8').read())
                msgFile["Content-Type"] = 'application/octet-stream'
            msgFile["Content-Disposition"] = 'attachment;filename="%s"' % fname[-1]
            self.msgRoot.attach(msgFile)
            self.logger.info('att_file is {}'.format(att_file))
        else:
            raise ('附件路径存在错误或不合法')

    def send(self):
        self.msgRoot['From'] = self.sender
        self.msgRoot['To'] = self.receiver
        self.msgRoot['Subject'] = self.title

        if self.path:
            if isinstance(self.path, list):
                for f in self.path:
                    self.attach_file(f)
            elif isinstance(self.path, str):
                self.attach_file(self.path)
            else:
                raise ('配置文件path地址错误')

        try:
            stmp_server = smtplib.SMTP_SSL(self.server, 465)
        except smtplib.SMTPConnectError as e:
            self.logger.info('服务器连接失败%' % e)
        else:
            try:
                stmp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                self.logger.info('用户名密码验证失败%' % e)
            else:
                stmp_server.sendmail(self.sender, self.receiver.split(','), self.msgRoot.as_string())
            finally:
                stmp_server.quit()
                self.logger.info('发送邮件"{0}"成功!收件人"{1}"如果没有收到邮件请检查垃圾箱'
                                 '同时检查地址是否正确'.format(self.title,self.receiver))
# if __name__=='__main__':
#     email = Email(path=r'D:\python\PycharmProjects\K_uiTest\report\report.html')
#     email.send()