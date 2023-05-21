from selenium.webdriver.common.by import By

from page.basepage import BasePage


class News(BasePage):

    # 热点
    _hot_news1 = (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a')
    _hot_news2 = (By.XPATH, '//*[@id="pane-news"]/ul[1]/li[1]/a')
    _hot_news3 = (By.XPATH, '//*[@id="pane-news"]/ul[2]/li[1]/a')
    _hot_news4 = (By.XPATH, '//*[@id="pane-news"]/ul[3]/li[1]/a')  # 需要关闭弹窗
    _hot_news5 = (By.XPATH, '//*[@id="pane-news"]/ul[4]/li[1]/a')  # 需要关闭弹窗
    _alert_btn = (By.ID, 'TANGRAM__PSP_4__closeBtn')  # 关闭弹窗的按钮
    _hot_news6 = (By.XPATH, '//*[@id="pane-news"]/ul[5]/li[1]/a')
    _lunbo_news = (By.XPATH, '//*[@id="imgTitle"]/a/strong')
    _hot_search = (By.XPATH, '//*[@id="news-hotwords"]/div[2]/ul/li[1]/a')
    _baijiahao1 = (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[1]/li[1]/a'),
    _baijiahao2 = (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[2]/li[1]/a')
    _baijiahao3 = (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[3]/li[1]/a')
    _baijiahao_picture1 = (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[1]/div/a[1]')  # 断言需获取元素title
    _baijiahao_picture2 = (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div/a[1]')  # 断言需获取元素title
    _baijiahao_picture3 = (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div[2]/a[1]')  # 断言需获取元素title
    _baijiahao_picture4 = (By.XPATH, '//*[@id="baijia-aside-recommend"]/div/div/div/div/a[1]')  # 断言需获取元素title
    _rednews = (By.XPATH, '//*[@id="focus-top"]/div[2]/div[1]/ul/a')  # 回退浏览器
    _input_search_words = (By.ID, 'ww')  # 顶部搜索输入框
    _click_search = (By.ID, 's_btn_wr')  # 点击搜索
    _search_assert = (By.XPATH, '//*[@id="1"]/div/div/div[1]/div/a/span')
    # =================================================================================================================
    # 视野
    view = (By.XPATH, '//*[@id="guonei"]/div[1]/div/h2')

    view_news1 = (By.XPATH, '//*[@id="guonei"]/div[2]/ul[1]/li[1]/a')
    view_news2 = (By.XPATH, '//*[@id="guonei"]/div[2]/ul[2]/li[1]/a')
    view_guonei_pic = (By.XPATH, '//*[@id="guonei"]/div[3]/div/div[2]/div/div[1]/div/a[2]')
    view_pic_info = (By.XPATH, '//*[@id="aside-civil-pic"]/div[2]/div/div/div[1]/a[2]')
    view_hot_hit = (By.XPATH, '//*[@id="civil-aside-tophit"]/div[2]/ol/li[1]/a')

    view_list = [view_news1, view_news2, view_hot_hit, view_pic_info, view_pic_info]

    # =================================================================================================================
    # 财经
    finance = (By.XPATH, '//*[@id="caijing"]/div[1]/div/h2')
    finance_news1 = (By.XPATH, '//*[@id="caijing"]/div[2]/ul[1]/li[1]/a')
    finance_news2 = (By.XPATH, '//*[@id="caijing"]/div[2]/ul[2]/li[1]/a')
    finance_pic_news = (By.XPATH, '//*[@id="caijing"]/div[3]/div/div[2]/div/div[1]/div/a[2]')
    finance_guzhiqihuo_iframe = (By.ID, 'stock_frame')
    finance_ganggu = (By.XPATH, '/html/body/div/div[2]/a[2]')
    finance_input_gupiao = (By.ID, 'wd2')
    finance_chazhao_gupiao = (By.XPATH, '//*[@id="sf2"]/input[2]')
    finance_duanyan_handler3 = (By.XPATH, '/html/body/div[4]/div[3]/label/a')
    finace_duanyan_hander4 = (By.XPATH, '//*[@id="stockName"]/i')
    finace_gupiaodaima = '002044'

    finance_list=[finance_news1, finance_news2, finance_pic_news]





    # =================================================================================================================


    def input_search_words(self):
        self.input(self._input_search_words, 'python')


    def click_alert_btn(self):
        self.click(self._alert_btn)

    def click_search(self):
        self.click(self._click_search)

    def click_hotnews1(self):
        self.click(self._hot_news1)

    def click_hotnews2(self):
        self.click(self._hot_news2)

    def click_hotnews3(self):
        self.click(self._hot_news3)

    def click_hotnews4(self):
        self.click(self._hot_news4)

    def click_hotnews5(self):
        self.click(self._hot_news5)

    def click_hotnews6(self):
        self.click(self._hot_news6)

    def click_lunbo_news(self):
        self.click(self._lunbo_news)

    def click_hot_search(self):
        self.click(self._hot_search)

    def click_baijiahao1(self):
        self.click(self._baijiahao1)

    def click_baijiahao2(self):
        self.click(self._baijiahao2)

    def click_baijiahao3(self):
        self.click(self._baijiahao3)

    def click_baijiahao_pic1(self):
        self.click(self._baijiahao_picture1)

    def click_baijiahao_pic2(self):
        self.click(self._baijiahao_picture2)

    def click_baijiahao_pic3(self):
        self.click(self._baijiahao_picture3)

    def click_baijiahao_pic4(self):
        self.click(self._baijiahao_picture4)

    def click_rednews(self):
        self.click(self._rednews)

    # =====================================================================================================
    # 区域

    def find_area_news1(self):  # 新闻
        return self.locator((By.XPATH, '//*[@id="localnews-focus"]/li[1]/a'))

    def click_area_news1(self):
        self.find_area_news1().click()

    def find_area_pic(self):  # 新闻图片
        return self.locator((By.XPATH, '//*[@id="localnews-pic"]/div/a[2]'))

    def click_area_pic(self):
        self.find_area_pic().click()

    def find_area_info(self):  # 新闻咨询
        return self.locator((By.XPATH, '//*[@id="localnews-zixun"]/ul/li[1]/a'))

    def click_area_info(self):
        self.find_area_info().click()

    def find_switch_area_btn(self):  # 切换区域控件
        return self.locator((By.XPATH, '//*[@id="change-city"]'))

    def click_switch_area_btn(self):
        self.find_switch_area_btn().click()

    def find_switch_to_shanghai(self):
        return self.locator((self.xpath, '//*[@id="city_view"]/div[1]/a[2]'))

    def click_switch_to_shanghai(self):
        self.find_switch_to_shanghai().click()

    def find_area_name(self):
        return self.locator((By.XPATH, '//*[@id="city_name"]/a/b'))

    def scroll_to_area(self):
        self.web_scroll_to_ele((By.XPATH, '//*[@id="city_name"]'))

    # ======================================================================================================
    # 视野
    def scroll_to_view(self):
        self.web_scroll_to_ele(self.view)

    def find_view_news1(self):
        return self.locator(self.view_news1)

    def click_view_news1(self):
        self.find_view_news1().click()

    def find_view_news2(self):
        return self.locator(self.view_news2)

    def click_view_new2(self):
        self.find_view_news2().click()

    def find_view_picinfo(self):
        return self.locator(self.view_pic_info)

    def click_view_picinfo(self):
        self.find_view_picinfo().click()

    def find_view_guonei_pic(self):
        return self.locator(self.view_guonei_pic)

    def click_view_guonei_pic(self):
        self.find_view_guonei_pic().click()

    def find_hot_hit(self):
        return self.locator(self.view_hot_hit)

    def click_hot_hit(self):
        self.find_hot_hit().click()

    # =====================================================================================================
    # 天下

    # =====================================================================================================

    # 体育

    # =====================================================================================================

    # 财经

    # =====================================================================================================
    # 科技
    # =====================================================================================================
    # 军事
    # =====================================================================================================
    # 互联网

    # =====================================================================================================
    # 探索
    # =====================================================================================================
    # 健康
    # =====================================================================================================

    # 图片

    def province_news(self):
        # 查看省会的新闻
        pass

    @property
    def hot_news4(self):
        return self._hot_news4

    @property
    def hot_news1(self):
        return self._hot_news1


if __name__ == '__main__':
    pass
