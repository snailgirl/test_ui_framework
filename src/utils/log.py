import logging
from logging.handlers import TimedRotatingFileHandler
from utils.settings import LOG_PATH

"""
logging配置
    日志就级别
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0 #不设置
"""
import os
import logging.config
# 定义三种日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

logfile_name = 'test.log'  # log文件名
logfile_path=os.path.join(LOG_PATH, logfile_name) # log文件的全路径

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'WARNING', #日志输出级别
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG', #日志输出级别
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5, #每天重新创建一个日志文件，最多保留backup_count份
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  #日志输出级别
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

class Logger():
    def __init__(self, logger_name='Test_framework'):
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
        self.logger = logging.getLogger(logger_name)  # 生成一个log实例
    def get_logger(self):
        return self.logger #logger.info('It works!')  # 记录该文件的运行状态
logger = Logger().get_logger()

if __name__ == '__main__':
    logger.info('fefeef')
