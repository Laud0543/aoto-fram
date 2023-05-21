# from page.all_page_elments import locator_mainpage_elem
from page.all_page_elments.locator_mainpage_elem import *
from page.basepage import BasePage
from page.news import News

elems = LocatorMainpageElem()

class MainPage(BasePage):
    username='15923371401'
    password='ly870246051'
    searchwords='python'


    def find_login_btn(self):
        return self.locator(longin_btn)

    def find_inputbox(self):
        return self.locator(input_field)

    def input_words(self,words=searchwords):
        # self.find_inputbox().send_keys(words)
        self.input(input_field, words)

    def click_search(self):
        self.click(click_btn)

    def click_login_btn(self):
        self.click(longin_btn)

    def input_username(self, username=username):
        self.input(input_name, username)

    def input_user_password(self, password=password):
        self.input(input_password, password)

    def click_login_sub(self):
        self.locator(longin_sub).submit()

    def python_assert_text(self):
        return self.locator(locate_python).text

    def get_login_assert_text(self):
        return self.locator(login_assert).text

    def move_to_user(self):
        self.web_element_hover(login_assert)

    def click_quit_login(self):
        self.click(quit_login_btn)

    def click_quit_btn(self):
        self.click(quit_btn)









    def input_search(self):
        self.input(elems.search, 'cainiao')

    def click_baidu(self):
        self.click(elems.baiduyixia)

    def goto_hao123(self):
        self.click(elems.hao123)

    def goto_video(self):
        self.click(elems.video)

    def goto_pictures(self):
        self.click(elems.picture)

    def goto_network_disk(self):
        self.click(elems.network_disk)

    def goto_setting(self):
        self.click(elems.setting)

    def goto_login(self):
        self.click(elems.login)

    def goto_maps(self):
        self.click(elems.maps)

    def goto_tieba(self):
        self.click(elems.tieba)

    def goto_news(self):
        self.click(elems.news)
        return News(self.driver)

    def goto_more(self):
        self.click(elems.more)

    def goto_translate(self):
        self.click(elems.translate)

    def goto_zhibo(self):
        self.click(elems.zhibo)

    def goto_music(self):
        self.click(elems.music)

    def goto_xueshu(self):
        self.click(elems.xueshu)

    def goto_wenku(self):
        self.click(elems.wenku)

    def goto_baike(self):
        self.click(elems.baike)

    def goto_zhidao(self):
        self.click(elems.zhidao)

    def goto_jiankang(self):
        self.click(elems.jiankang)

    def goto_yingxiaotuiguang(self):
        self.click(elems.yingxiaotuiguang)

    def goto_chakangengduochanpin(self):
        self.click(elems.chakangengduochanpin)

    def goto_baiduyixia(self):
        self.click(elems.baiduyixia)