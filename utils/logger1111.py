#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import logging
import sys
from logging import handlers
import os

#项目路径
pro_path = os.path.dirname(os.path.dirname(__file__))

class Logger:

    _instance = None
    logger = None
    log_path = os.path.join(pro_path,("output\\log" + os.sep + "log.txt"))

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        if self.logger is None:
            self.logger = self.create_logger()

    def create_logger(self):
        logger = None
        formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(pathname)s : %(funcName)s:%(lineno)d , %(message)s'
        )
        logger = logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        fileHandle = handlers.TimedRotatingFileHandler(
            self.log_path,when="h",interval=24,backupCount=1,encoding="utf8")
        consoleHandle = logging.StreamHandler()
        fileHandle.setLevel(logging.INFO)
        consoleHandle.setLevel(logging.DEBUG)
        fileHandle.setFormatter(formater)
        consoleHandle.setFormatter(formater)
        logger.addHandler(fileHandle)
        logger.addHandler(consoleHandle)
        return logger

    def info(self,msg):
        self.logger.info(msg)

    def debug(self,msg):
        self.logger.debug(msg)

    def warn(self,msg):
        self.logger.warn(msg)

    def erro(self,msg):
        self.logger.error(msg)

if __name__ == '__main__':


    logger = Logger()
    logger.info("test logger")


try:
    with open('file_not_exists.log') as f:
        lines = f.readlines()
        print(lines)
except Exception as err:
    logging.error(err, exc_info=True)

































