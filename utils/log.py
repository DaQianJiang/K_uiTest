import logging
from utils.config import BASE_PATH
import os
import time
from logging.handlers import TimedRotatingFileHandler

LOG_PATH = os.path.join(BASE_PATH,'log')
class Logger(object):
    def __init__(self,logger_name = 'test_logger'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.file_level = logging.WARNING
        self.consol_level = logging.DEBUG
        self.backup = 5
        self.file_name = time.strftime("%Y-%m-%d")+'.log'
        self.log_path = os.path.join(LOG_PATH,self.file_name)
        self.partten = '%(asctime)s-%(name)s-%(levelname)s-%(message)s'

    def get_log(self):
        self.consol_hander = logging.StreamHandler()
        self.consol_hander.setLevel(self.consol_level)
        self.file_handle = TimedRotatingFileHandler(self.log_path,when='D',
                                                    backupCount=self.backup,delay=False,
                                                    encoding='utf-8')
        self.file_handle.setLevel(self.file_level)
        self.logger.addHandler(self.consol_hander)
        self.logger.addHandler(self.file_handle)
        self.formatter = logging.Formatter(self.partten)
        self.consol_hander.setFormatter(self.formatter)
        self.file_handle.setFormatter(self.formatter)
        return self.logger

# if __name__=='__main__':
#     logger = Logger(logger_name='LoggerClass').get_log()
#     logger.debug('debuge123')
#     logger.warning('warning1234')








