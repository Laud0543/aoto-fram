from page import MainPage
# from selenium import webdriver
from config import url
from utils.logger import logger
from driver.driver_factory import DriverFactory
# from selenium.webdriver.common.by import By
# from time import sleep


class Startpage:

    def __init__(self):
        """
          初始化driver
          :param browser:浏览器名称
          """
        self.driver = DriverFactory.get_driver()
        self.url = url
        self.driver.maximize_window()

    def start_main_page(self):
        self.driver.get(self.url)
        logger.info('进入百度首页')
        return MainPage(self.driver)
        # if '判断页面标题是否是 login page':
        #     是就调用login
        #     然后再return主页面
        # elif 返回主页面


# 开启无头浏览器
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://www.baidu.com/')
# sleep(2)
# driver.quit()

# 添加代理服务器
# PROXY = "proxy_host:proxy:port"
# options = webdriver.ChromeOptions()
# desired_capabilities = options.to_capabilities()
# desired_capabilities['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "noProxy": None,
#     "proxyType": "MANUAL",
#     "class": "org.openqa.selenium.Proxy",
#     "autodetect": False
# }
# driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

# WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value))

# 页面加载策略

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  # complete
# # caps["pageLoadStrategy"] = "eager"  #  interactive
# # caps["pageLoadStrategy"] = "none"
# driver = webdriver.Chrome(desired_capabilities=caps)
# driver.get('https://www.ptpress.com.cn/')
# driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/input').send_keys('Storm')
# sleep(2)
# driver.quit()

# 处理弹窗
# options = webdriver.ChromeOptions()
# prefs = {
#     'profile.default_content_setting_values':
#         {
#             'notifications': 1
#         }
# }
# options.add_experimental_option('prefs', prefs)
#
# cls.driver = webdriver.Chrome(chrome_options=options)




#  那直接进入首页点击其它功能按钮才调出登录页的怎么搞呢

# def quit(self):
#     self.driver.quit()

# def assertion(self):
#     pass


if __name__ == '__main__':
    Startpage().start_main_page()

    # var = {
    # 'hot_news1': (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a'),
    # 'hot_news2': (By.XPATH, '//*[@id="pane-news"]/ul[1]/li[1]/a'),
    # 'hot_news3': (By.XPATH, '//*[@id="pane-news"]/ul[2]/li[1]/a'),
    # 'hot_news4': (By.XPATH, '//*[@id="pane-news"]/ul[3]/li[1]/a'), # 关闭弹窗
    # 'hot_news5': (By.XPATH, '//*[@id="pane-news"]/ul[4]/li[1]/a'),
    # 'hot_news6': (By.XPATH, '//*[@id="pane-news"]/ul[5]/li[1]/a'),
    # 'picture_link' : (By.XPATH, '//*[@id="imgTitle"]/a/strong'),
    # 'hot_search' : (By.XPATH, '//*[@id="news-hotwords"]/div[2]/ul/li[1]/a'),
    # 'baijiahao1' : (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[1]/li[1]/a'),
    # 'baijiahao2' : (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[2]/li[1]/a'),
    # 'baijiahao3' : (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[3]/li[1]/a'),
    # 'baijiahao_picture1': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[1]/div/a[1]'), # 断言需获取元素title
    # 'baijiahao_picture2': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div/a[1]'), # 断言需获取元素title
    # 'baijiahao_picture3': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div[2]/a[1]'), # 断言需获取元素title
    # 'baijiahao_picture4': (By.XPATH, '//*[@id="baijia-aside-recommend"]/div/div/div/div/a[1]'), # 断言需获取元素title
    # 'red_networld' : (By.XPATH, '//*[@id="focus-top"]/div[2]/div[1]/ul/a'), # 回退浏览器
    # }
    # a = Startpage()
    # b = a.start_main_page()
    # c = b.goto_news()
    #
    # for key1 in var:
    #     # c.read_hot_news()
    #     sleep(1)
    #     # if key1 != 'red_networld':
    #     #     b.web_switch_windows(2)
    #     if key1 == 'hot_news4' :
    #         b.web_switch_windows(1)
    #         text1 = b.locator(var.get(key1)).text[:3]
    #         b.click(var.get(key1))
    #         # b.web_switch_frame((By.XPATH,'/html/body/iframe'))
    #         # print('已切换iframe')
    #         sleep(2)
    #         b.web_switch_windows(2)
    #
    #         b.click((By.ID,'TANGRAM__PSP_4__closeBtn'))
    #         sleep(1)
    #         assert text1 in b.web_title
    #         print('已关闭弹窗')
    #
    #         # b.web_switch_default_content()
    #     if key1 == 'red_networld':
    #         b.web_switch_windows(1)
    #         sleep(1)
    #         b.click(var.get(key1))
    #         assert '理论新境界' in b.web_title
    #         print('断言成功')
    #
    #         # b.web_back()
    #         # print('已回退')
    #
    #
    #     if 'baijiahao' in key1:
    #         b.web_switch_windows(1)
    #         sleep(1)
    #         title = b.locator(var.get(key1)).get_attribute('title')
    #         sleep(1)
    #         b.click(var.get(key1))
    #         sleep(2)
    #         b.web_switch_windows(2)
    #         sleep(1)
    #         assert title in b.web_title
    #         b.close()
    #         print('已关闭新窗口')
    #
    #     else:
    #         b.web_switch_windows(1)
    #         sleep(1)
    #         text1 = b.locator(var.get(key1)).text[:3]
    #         b.click(var.get(key1))
    #         sleep(2)
    #         b.web_switch_windows(2)
    #         assert text1 in b.web_title
    #         sleep(1)
    #         b.close()
    #         print('已关闭新窗口')

    # assert text1 in b.web_title
    # print(b.web_title)
    # if key1 != 'red_networld':
    #     b.close()
    # print('已关闭新窗口')

    # print(b.locator((By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[1]/h1')).text)
    # b.sleep(2)

    # assert b.locator((By.XPATH,'//*[@id="__next"]/div/div[2]/div[3]/div[1]/h1')).text == '独家视频丨习近平在沧州市考察调研'
    # b.sleep(3)
    # b.screen_shot(n=3)
    # b.quit()
