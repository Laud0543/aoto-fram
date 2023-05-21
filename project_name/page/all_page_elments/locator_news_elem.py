from selenium.webdriver.common.by import By


class LocatorNewsElems(object):
    news_input = (By.ID, 'ww')
    news_btn = (By.ID, 's_btn_wr')
    hot_news1 = (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a')
    hot_news2 = (By.XPATH, '//*[@id="pane-news"]/ul[1]/li[1]/a')
    hot_news3 = (By.XPATH, '//*[@id="pane-news"]/ul[2]/li[1]/a')
    hot_news4 = (By.XPATH, '//*[@id="pane-news"]/ul[3]/li[1]/a')
    hot_news5 = (By.XPATH, '//*[@id="pane-news"]/ul[4]/li[1]/a')
    hot_news6 = (By.XPATH, '//*[@id="pane-news"]/ul[5]/li[1]/a')

    var = {
        'hot_news1': (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a'),
        'hot_news2': (By.XPATH, '//*[@id="pane-news"]/ul[1]/li[1]/a'),
        'hot_news3': (By.XPATH, '//*[@id="pane-news"]/ul[2]/li[1]/a'),
        'hot_news4': (By.XPATH, '//*[@id="pane-news"]/ul[3]/li[1]/a'),  # 关闭弹窗
        'hot_news5': (By.XPATH, '//*[@id="pane-news"]/ul[4]/li[1]/a'),
        'hot_news6': (By.XPATH, '//*[@id="pane-news"]/ul[5]/li[1]/a'),
        'picture_link': (By.XPATH, '//*[@id="imgTitle"]/a/strong'),
        'hot_search': (By.XPATH, '//*[@id="news-hotwords"]/div[2]/ul/li[1]/a'),
        'baijiahao1': (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[1]/li[1]/a'),
        'baijiahao2': (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[2]/li[1]/a'),
        'baijiahao3': (By.XPATH, '//*[@id="baijia"]/div[3]/div/ul[3]/li[1]/a'),
        'baijiahao_picture1': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[1]/div/a[1]'),  # 断言需获取元素title
        'baijiahao_picture2': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div/a[1]'),  # 断言需获取元素title
        'baijiahao_picture3': (By.XPATH, '//*[@id="baijia"]/div[2]/div/div[2]/div[2]/a[1]'),  # 断言需获取元素title
        'baijiahao_picture4': (By.XPATH, '//*[@id="baijia-aside-recommend"]/div/div/div/div/a[1]'),  # 断言需获取元素title
        'red_networld': (By.XPATH, '//*[@id="focus-top"]/div[2]/div[1]/ul/a'),  # 回退浏览器
    }



