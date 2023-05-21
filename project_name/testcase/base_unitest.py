#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from utils.logger import logger
# import 截图
from utils.save_screen_shot import screen_shot

class BaseUnitest(unittest.TestCase):
    driver = None

    close_browser_current_tab_on_tear_down = False

    def input_log_and_save_screenshot(self,exc,driver):
        logger.error(f"断言失败" + exc)
        screen_shot(driver, n=2)

    def assertEqual_new(self, first, second,driver, msg=None):
        try:
            self.assertEqual(first,second,msg)
            logger.info('断言成功')
        except Exception as e:
            # logger.info('失败')
            self.input_log_and_save_screenshot(str(e),driver)
            raise

    def asserIn_new(self, first, second, msg, driver):
        try:
            self.assertIn(first,second,msg)
            logger.info('断言成功')
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def assertIs_new(self, first, second, msg, driver):
        try:
            self.assertIs(first,second,msg)
            logger.info('断言成功')
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def assertisNone_new(self,exp,msg,driver):
        try:
            self.assertIsNone(exp,msg)
            logger.info('断言成功')
        except Exception as e:
            self.input_log_and_save_screenshot(str(e), driver)
            raise

    def setUp(self) -> None:
        logger.info("-----开始执行测试用例-----")


    def tearDown(self):
        """
        每个测试结束时执行的动作.

        :return:
        """
        logger.info("-----测试用例已执行完成-----")

        screen_shot(self.driver, n=1)

        if self.close_browser_current_tab_on_tear_down is True:
            self.driver.close()
    @classmethod
    def tearDownClass(cls):
        """
        测试全部结束时执行的动作.

        :return:
        """
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()




