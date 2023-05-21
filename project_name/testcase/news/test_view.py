import unittest
from driver.start import Startpage
# from utils.logger import Logger
from utils.logger import logger
from time import sleep
from ddt import ddt, data
from page import News


@ddt
class test_view_news(unittest.TestCase):
    Newspage = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.Newspage = Startpage().start_main_page().goto_news()
        cls.Newspage.web_switch_windows(1)
        cls.Newspage.web_scroll('down')
        cls.Newspage.scroll_to_view()

    def setUp(self) -> None:

        # self.logger.info("-----开始执行测试-----")
        self.Newspage.web_switch_windows(1)
        logger.info("-----开始执行测试-----")

    def tearDown(self) -> None:
        logger.info("-----用例执行完毕，关闭浏览器-----")
        self.Newspage.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.Newspage.quit()

    @data(*News.view_list)
    def test_view_news(self, locator):
        news = self.Newspage

        sleep(3)
        # text1=news.find_area_pic().text[:3]
        text1 = news.locator(locator).text[:3]
        # text1 = news.return_text()
        news.click(locator)
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)


if __name__ == '__main__':
    unittest.main()
