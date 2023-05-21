#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author:
# CreatDate:
# Version:
# ====#====#====#====
# import os
from selenium import webdriver
from utils.logger import logger


class DriverFactory:
    """
        # singleton
        单例模式，保证全局只有有一个driver
    """
    _instance = None
    _dirver = None

    # Chrome_driver_path = os.path.join(os.path.dirname(__file__),"drivers" + os.sep + "chromedriver.exe")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls, browers="chrome"):
        if cls._dirver is None:
            cls._dirver = cls.create_driver(browers)
            logger.info("创建" + browers + "driver")
        return cls._dirver

    @classmethod
    def create_driver(cls, browers):
        driver = None
        if browers.lower() == "chrome":
            option = webdriver.ChromeOptions()
            option.binary_location = r'C:\Users\Laud\AppData\Local\Google\Chrome\Application\chrome.exe'
            driver = webdriver.Chrome(r'C:\Users\Laud\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        elif browers.lower() == "firfox":
            driver = webdriver.Chrome()
        elif browers.lower() == "ie":
            driver = webdriver.Ie()
        elif browers.lower() == "Safari":
            driver = webdriver.Safari()
        else:
            logger.warn("您传入的参数browers异常")
            # print("您传入的参数browers异常")
        return driver


if __name__ == '__main__':
    driver = DriverFactory.get_driver()
    driver.get("http://www.baidu.com")
    from time import sleep

    sleep(2)
    driver.quit()
