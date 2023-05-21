from page import News

# _hot_news1 = (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a')
# _hot_news2 = (By.XPATH, '//*[@id="pane-news"]/ul[1]/li[1]/a')
# _hot_news3 = (By.XPATH, '//*[@id="pane-news"]/ul[2]/li[1]/a')
# _hot_news6 = (By.XPATH, '//*[@id="pane-news"]/ul[5]/li[1]/a')

# hot_news = [{'data':News._hot_news1}, {'data':News._hot_news2}, {'data':News._hot_news3}, {'data':News._hot_news4}]

hot_news = [News._hot_news1, News._hot_news2,News._hot_news3, News._hot_news4,News._hot_news6,News._lunbo_news,News._hot_search,
            News._baijiahao1,News._baijiahao2,News._baijiahao3]
hot_pictures = [News._baijiahao_picture1,News._baijiahao_picture2,News._baijiahao_picture3,News._baijiahao_picture4]

if __name__ == '__main__':
    print(hot_pictures)