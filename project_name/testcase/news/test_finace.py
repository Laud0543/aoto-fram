import unittest
from driver.start import Startpage
# from utils.logger import Logger
from utils.logger import logger
from time import sleep
from ddt import ddt, data
from page import News


@ddt
class test_Finance_News(unittest.TestCase):
    Newspage = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.Newspage = Startpage().start_main_page().goto_news()
        cls.Newspage.web_switch_windows(1)

        for i in range(1,6):
            sleep(1)
            print('第{}次'.format(i))
            cls.Newspage.web_scroll(direction='down')
            # sleep(2)
            # # cls.Newspage.web_scroll(direction='down')
            # cls.Newspage.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # sleep(3)
            # cls.Newspage.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # sleep(3)
            # cls.Newspage.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # sleep(3)
            # cls.Newspage.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        cls.Newspage.web_scroll_to_ele(cls.Newspage.finance)

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

    @data(*News.finance_list)
    def test_finance_news1(self,locator):
        news = self.Newspage

        sleep(3)
        # text1=news.find_area_pic().text[:3]
        text1 = news.locator(locator).text[:3]
        # text1 = news.return_text()
        news.click(locator)
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)



    def test_Stock_inquiry2(self):
        news = self.Newspage

        news.web_switch_frame(news.finance_guzhiqihuo_iframe)
        news.web_element_hover(news.finance_ganggu)

        news.web_switch_default_content()
        news.click(news.finance_input_gupiao)

        news.input(news.finance_input_gupiao,news.finace_gupiaodaima)

        news.click(news.finance_chazhao_gupiao)
        news.web_switch_windows(2)
        logger.info('进入新浪财经页面')
        assert '新浪财经' in news.web_title(loadtime=3)
        logger.info('断言成功')
        news.click(news.finance_duanyan_handler3)
        news.close()
        news.web_switch_windows(2)
        assert '美年健康' == news.locator(news.finace_duanyan_hander4).text




if __name__ == '__main__':
    unittest.main()
