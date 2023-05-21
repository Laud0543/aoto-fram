from ddt import ddt,data,unpack,file_data

from logger import logger
from driver.start import Startpage
from testcase.news_page.hot_news_testdata import hot_news
import unittest
from selenium.webdriver.common.by import By




# @ddt
# class test1(unittest.TestCase):
#     @data(*hot_news)
#     # @unpack
#     def test(self,data):
#         print(data)



if __name__ == '__main__':
    # try:
    #     assert 2 == 3
    #     print(1)
    #
    # except AssertionError as e:
    #     print(2)
    #
    #     print('raise AssertionError 异常', e.__str__())

    # news = Startpage().start_main_page().goto_news()
    # news.web_switch_windows(1)
    # # logger.error('有问题')
    # news.input_search_words()
    # news.click_search()
    # try:
    #
    #     assert news.locator(news._search_assert).text == '换一换'
    #     news.screen_shot()
    #     print('断言成功22222')
    # except AssertionError as e:
    #     # logger.error('断言失败22222')
    #     news.screen_shot(n=2)
    #     print('raise AssertionError 异常', e.__str__())

    news = Startpage().start_main_page().goto_news()
    news.web_switch_windows(1)
    title = news.locator((By.XPATH, '//*[@id="baijia"]/div[2]/div/div[1]/div/a[1]')).get_attribute('title')
    news.click_baijiahao_pic1()
    # logger.error('有问题')
    # try:
    #     assert '理论新境界' in news.web_title
    #     print('断言成功111111111')
    #     news.screen_shot()
    # except AssertionError as e:
    #     print('断言失败111111111')
    #     # logger.error(e.__str__())
    #     news.screen_shot(n=2)
    news.web_switch_windows(2)
    try:
        assert '236547' in news.web_title(loadtime=2)
        print(1)
        news.screen_shot()
    except AssertionError as e:
        print(2)
        news.screen_shot(N=2)

    news.quit()