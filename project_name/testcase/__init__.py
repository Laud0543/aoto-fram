from project_name.testcase.news.test_hot_news import test_News
from project_name.testcase.news.test_finace import test_Finance_News
from project_name.testcase.news.test_area import test_area_news
from project_name.testcase.news.test_view import test_view_news
from project_name.testcase.main_page.test_main_page import test_main_page
__all__ = ['all_testcase']

all_testcase = [test_News, test_Finance_News, test_view_news, test_area_news, test_main_page]