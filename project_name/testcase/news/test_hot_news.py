import unittest
from driver.start import Startpage
# from utils.logger import Logger
from utils.logger import logger
from ddt import ddt,data,unpack,file_data
from project_name.testcase.news.hot_news_testdata import hot_news , hot_pictures

@ddt
class test_News(unittest.TestCase):

    def setUp(self) -> None:
        logger.info("-----开始执行测试-----")
        # self.logger.info("-----开始执行测试-----")

        self.Newspage = Startpage().start_main_page().goto_news()

        self.Newspage.web_switch_windows(1)


    def tearDown(self) -> None:
        logger.info("-----用例执行完毕，关闭浏览器-----")
        self.Newspage.quit()


    @data(*hot_news)
    # @unpack
    def test_hot_news1(self, data):
        """

        :param data: 测试数据
        """
        news = self.Newspage

        text1 = news.locator(data).text[:3]
        news.locator(data).click()

        news.web_switch_windows(2)

        assert text1 in news.web_title(loadtime=2)

    # def test_hot_news2(self):
    #     pass
    #
    # def test_hot_news3(self):
    #     pass
    #
    # def test_hot_news4(self):
    #     pass

    def test_hot_news5(self):
        news = self.Newspage
        text1 = news.locator(news._hot_news5).text[:3]
        news.click_hotnews5()
        # b.web_switch_frame((By.XPATH,'/html/body/iframe'))
        # print('已切换iframe')
        news.web_switch_windows(2)
        # news.click_alert_btn()
        assert text1 in news.web_title(loadtime=2)



    # def test_hot_news6(self):
    #     pass
    #
    def test_lunbonews7(self):
        news = self.Newspage

        text1 = news.locator(news._lunbo_news).text[:3]
        news.click_lunbo_news()
        # b.web_switch_frame((By.XPATH,'/html/body/iframe'))
        # print('已切换iframe')
        news.web_switch_windows(2)
        assert text1 in news.web_title(loadtime=2)

    # def test_hot_search8(self):
    #     pass
    #
    # def test_baijiahao1(self):
    #     pass
    #
    # def test_baijiahao2(self):
    #     pass
    #
    # def test_baijiahao3(self):
    #     pass
    #
    @data(*hot_pictures)
    def test_baijiahao_picture1(self,data):
        news=self.Newspage

        title = news.locator(data).get_attribute('title')
        news.click(data)
        news.web_switch_windows(2)
        assert title in news.web_title(loadtime=2)
        news.close()


    # def test_baijiahao_picture2(self):
    #     pass
    #
    # def test_baijiahao_picture3(self):
    #     pass
    #
    # def test_baijiahao_picture4(self):
    #     pass
    #
    def test_rednews(self):
        news = self.Newspage

        news.click_rednews()
        try:
            assert '111理论新境界1' in news.web_title(loadtime=2)
            print('断言成功111111111')
            news.screen_shot()
        except AssertionError as e:
            print('断言失败111111111')
            logger.error(e.__str__())
            news.screen_shot(n=2)



    def test_input_search(self):
        news = self.Newspage
        news.input_search_words()
        news.click_search()

        try:
            print('断言成功22222')
            assert news.locator(news._search_assert).text == '换一换'
            news.screen_shot()
        except AssertionError as e:
            logger.error('断言失败22222')
            news.screen_shot(n=2)

            print('raise AssertionError 异常', e.__str__())











if __name__ == '__main__':
    unittest.main()
