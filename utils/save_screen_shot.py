import os
import time


from selenium.webdriver.remote.webdriver import WebDriver
from config import TESTCASE_SUCCESS_DIR, ASSERT_FAILED_DIR, LOCATOR_FAILED_DIR
# from ..config import
from utils.logger import logger



def screen_shot(driver: WebDriver, imgreport: bool = False, n: int = 1 ) -> str or None:
    """
    截取当前界面图片
    :type driver: WebDriver
    :param driver:
    :param n: int 默认为1，用例成功截图为1，失败为2，元素定位不到为3
    :param imgreport:  str 图片追加到测试报告 默认添加到报告
    :return:

    """

    # if not os.path.exists("./image"):
    #     os.makedirs("./image")
    # filename = str(round(time.time() * 1000)) + ".png"
    # if len(filename) >= 200:
    #     filename = str(round(time.time() * 1000)) + ".png"
    # if n == 1:
    #     filepath = os.path.join(TESTCASE_SUCCESS_DIR, filename)
    # elif n == 2:
    #     filepath = os.path.join(ASSERT_FAILED_DIR, filename)
    # elif n == 3:
    #     filepath = os.path.join(LOCATOR_FAILED_DIR, filename)
    # else:
    #     logger.error('n不在1,2,3取值范围内，默认为1')
    #     filepath = os.path.join(TESTCASE_SUCCESS_DIR, filepath)
    #     driver.save_screenshot(filepath)

    filename = str(round(time.time() * 1000)) + ".png"
    if len(filename) >= 200:
        filename = str(round(time.time() * 1000)) + ".png"

    if n == 1:
        filepath = os.path.join(TESTCASE_SUCCESS_DIR, filename)
        driver.save_screenshot(filepath)
        logger.info(f"用例执行完毕截图已存入: {filepath}")
    elif n == 2:
        filepath = os.path.join(ASSERT_FAILED_DIR, filename)
        driver.save_screenshot(filepath)
        logger.info(f"断言失败截图已存入: {filepath}")
    elif n == 3:
        filepath = os.path.join(LOCATOR_FAILED_DIR, filename)
        driver.save_screenshot(filepath)
        logger.info(f"元素定位截图已存入: {filepath}")
    else:
        logger.info('n不在1,2,3取值范围内，默认为1')
        filepath = os.path.join(TESTCASE_SUCCESS_DIR, filename)
        driver.save_screenshot(filepath)
        logger.info(f"截图成功已存入: {filepath}")



    if imgreport:
        pass
        # allure.attach(self.driver.get_screenshot_as_png(),
    #                   name=filename,
    #                   attachment_type=allure.attachment_type.PNG)
    # logger.debug(f"截图成功已经存储在: {filepath}")
    #   return filepath