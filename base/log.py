import logging
from logging.handlers import RotatingFileHandler
import time
from base.public import filepath
import os


class Logger:
    def __init__(
            self,
            logger_name=None,
            console_log_level='info',
            file_log_level='info'):
        self.logger_name = logger_name
        self.log_path = filepath('log')
        # self.logger = logging.getLogger(logger_name)
        # # 设置根日志记录器的级别为NOTSET，不过滤任何日志消息
        # logging.root.setLevel(logging.NOTSET)
        self.logFileName = time.strftime(
            "%Y_%m_%d_") + '{}.log'.format(logger_name)
        # 最多存放日志的数量
        self.backupCount = 5
        # 给初始化日志处理器添加标志，避免重复新增处理器的情况
        self.handlers_added = False
        console_log_level = console_log_level.upper()
        file_log_level = file_log_level.upper()
        level_list = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        # 控制台日志输出级别
        if console_log_level in level_list:
            self.consoleOutputLevel = console_log_level
        else:
            self.consoleOutputLevel = 'INFO'
            print("日志等级输入有误，请确认！")

        # 写入日志文件输出级别
        if file_log_level in level_list:
            self.fileOutputLevel = file_log_level
        else:
            self.fileOutputLevel = 'INFO'
            print("日志等级输入有误，请确认！")

    def get_logger(self):
        logger = logging.getLogger(self.logger_name)
        # 设置根日志记录器的级别为NOTSET，不过滤任何日志消息
        logger.setLevel(logging.NOTSET)
        if not self.handlers_added:
            # 创建一个控制台处理器，并设置级别
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.consoleOutputLevel)
            # 创建一个旋转文件处理器
            # maxBytes：每个日志文件的最大字节数
            # backupCount：保留的备份文件数量
            rotating_handler = RotatingFileHandler(
                os.path.join(
                    self.log_path,
                    self.logFileName),
                maxBytes=1024 * 1024 * 5,
                backupCount=self.backupCount,
                encoding='utf-8')
            rotating_handler.setLevel(self.fileOutputLevel)
            # # 创建一个文件处理器，并设置级别
            # file_handler = logging.FileHandler(
            #     os.path.join(self.log_path, self.logFileName))
            # file_handler.setLevel(self.fileOutputLevel)
            # 定义日志格式
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
            console_handler.setFormatter(formatter)
            rotating_handler.setFormatter(formatter)
            # 将处理器添加到日志记录器
            logger.addHandler(console_handler)
            logger.addHandler(rotating_handler)
            # 标记处理器已添加
            self.handlers_added = True
        return logger


# def logger(logger_name=None,
#            console_log_level='debug',
#            file_log_level='error'):
#     print(Logger(logger_name, console_log_level, file_log_level).get_logger())
#
# if __name__ == '__main__':
#     logger = Logger('demo', 'aaa', 'sss').get_logger()
#     logger.error('错误日志.....')
