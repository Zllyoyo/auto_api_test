from base.log import Logger
import threading


class LoggerFactory:
    loggers = {}
    lock = threading.Lock()

    @staticmethod
    def get_logger(
            logger_name=None,
            console_log_level='info',
            file_log_level='info'):
        with LoggerFactory.lock:
            if logger_name not in LoggerFactory.loggers:
                logger = Logger(logger_name, console_log_level, file_log_level)
                LoggerFactory.loggers[logger_name] = logger
        return LoggerFactory.loggers[logger_name].get_logger()
