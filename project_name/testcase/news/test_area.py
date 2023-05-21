import unittest
from driver.start import Startpage
# from utils.logger import Logger
from utils.logger import logger
from time import sleep
from ddt import ddt,data,unpack,file_data


class test_area_news(unittest.TestCase):
    Newspage = Startpage().start_main_page().goto_news()

    @classmethod
    def setUpClass(cls) -> None:
     # cls.Newspage()
         pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.Newspage.quit()


    def setUp(self) -> None:

        # self.logger.info("-----开始执行测试-----")
        self.Newspage.web_switch_windows(1)
        logger.info("-----开始执行测试-----")



    def tearDown(self) -> None:
        self.Newspage.close()
        logger.info("-----用例执行完毕，已关闭新打开的页面-----")



    def test_area_news1(self):
        news = self.Newspage
        news.scroll_to_area()

        sleep(3)
        # text1=news.find_area_pic().text[:3]
        text1 = news.find_area_news1().text[:3]
        # text1 = news.return_text()
        news.click_area_news1()
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)

    def test_area_pic2(self):
        news = self.Newspage
        news.scroll_to_area()

        sleep(3)
        # text1=news.find_area_pic().text[:3]
        text1 = news.find_area_pic().text[:3]
        # text1 = news.return_text()
        news.click_area_pic()
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)

    def test_area_info(self):
        news = self.Newspage
        news.scroll_to_area()

        sleep(3)
        # text1=news.find_area_pic().text[:3]
        text1 = news.find_area_info().text[:3]
        # text1 = news.return_text()
        news.click_area_info()
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)

    def test_switcharea_and_checknews(self):
        news = self.Newspage
        news.scroll_to_area()

        sleep(3)
        news.click_switch_area_btn()
        sleep(5)
        text1=news.find_switch_to_shanghai().text
        news.click_switch_to_shanghai()
        assert text1 == news.find_area_name().text
        text2=news.find_area_news1().text[:3]

        news.click_area_news1()
        news.web_switch_windows(2)
        assert text2 in news.web_title(loadtime=2)






if __name__ == '__main__':
    unittest.main()


