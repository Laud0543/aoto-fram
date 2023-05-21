import unittest
from driver.start import Startpage
# from utils.logger import Logger
from time import sleep
from ddt import ddt
from config import p
from project_name.testcase.base_unitest import BaseUnitest

@ddt
class test_main_page(BaseUnitest):
    mainpage = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.mainpage = Startpage().start_main_page()
        cls.driver = cls.mainpage.driver
        # cls.Newspage.web_switch_windows(1)
        # cls.Newspage.web_scroll(direction='down')
        # cls.Newspage.web_scroll_to_ele(cls.Newspage.finance)

    # def setUp(self) -> None:
    #
    #     # self.logger.info("-----开始执行测试-----")
    #
    #     logger.info("-----开始执行测试用例-----")

    # def tearDown(self) -> None:
    #     logger.info("-----测试用例已执行完成-----")
        # self.Newspage.close()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.mainpage.quit()


    @unittest.skipIf(p >=1, '运行P0级别的用例')
    def test_baidu_search_01(self):
        mainpage=self.mainpage
        mainpage.input_words()
        mainpage.click_search()
        # mainpage.web_switch_windows(1)
        assert mainpage.python_assert_text() == 'python'
        # mainpage.close()
        mainpage.web_back()
        sleep(2)

    def test_login_02(self):
        mainpage=self.mainpage
        mainpage.click_login_btn()
        mainpage.input_username()
        mainpage.input_user_password()
        mainpage.click_login_sub()
        sleep(8)
        self.assertEqual_new(mainpage.get_login_assert_text(), '小小手LY',self.driver)
        mainpage.move_to_user()
        sleep(2)
        mainpage.click_quit_login()
        mainpage.click_quit_btn()
        sleep(2)
        self.assertEqual_new(mainpage.find_login_btn().text, '111登录',self.driver)
        # assert mainpage.find_login_btn().text == '登录'


    # @data(*News.finance_list)
    # def test_finance_news1(self,locator):
    #     news = self.Newspage
    #
    #     sleep(3)
    #     # text1=news.find_area_pic().text[:3]
    #     text1 = news.locator(locator).text[:3]
    #     # text1 = news.return_text()
    #     news.click(locator)
    #     news.web_switch_windows(2)
    #     assert text1 in news.web_title(loadtime=2)

if __name__ == '__main__':
    unittest.main()
