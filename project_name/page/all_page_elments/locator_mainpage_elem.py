from selenium.webdriver.common.by import By



input_field =(By.ID, 'kw')

click_btn = (By.ID, 'su')

longin_btn = (By.ID, 's-top-loginbtn')

input_name = (By.ID, 'TANGRAM__PSP_11__userName')

input_password = (By.ID, 'TANGRAM__PSP_11__password')

longin_sub = (By.ID, 'TANGRAM__PSP_11__submit')

locate_python = (By.XPATH, '//*[@id="3001"]/div/div[1]/div/div/h3/div/a/font')
login_assert = (By.XPATH, '//*[@id="s-top-username"]/span[2]')
quit_login_btn = (By.XPATH, '//*[@id="s-user-name-menu"]/a[4]')
quit_btn = (By.XPATH, '//*[@id="dialog_con_wrap"]/div[3]/div[1]/span[1]')


class LocatorMainpageElem(object):
    search = (By.ID, 'kw')

    news = (By.LINK_TEXT, '新闻')  # 定位新闻

    hao123 = (By.LINK_TEXT, 'hao123') # 定位hao123

    tieba = (By.LINK_TEXT, '贴吧')

    video = (By.LINK_TEXT, '视频')

    picture = (By.LINK_TEXT,'图片')

    network_disk = (By.LINK_TEXT, '网盘')

    setting = (By.LINK_TEXT, '设置')

    login = (By.LINK_TEXT,'登录')

    maps = (By.LINK_TEXT, '地图')

    more = (By.LINK_TEXT, '更多')

    translate = (By.LINK_TEXT,'tj_fanyi')

    zhibo= (By.NAME, 'tJ_live')

    music = (By.NAME,'tj_mp3')

    xueshu = (By.NAME, 'tj_xueshu')

    wenku = (By.NAME, 'tj_wenku')

    baike = (By.NAME,'tj_baike')

    zhidao = (By.NAME,'tj_zhidao')

    jiankang = (By.NAME, 'tj_jiankang')

    yingxiaotuiguang = (By.NAME, 'yingxiaotuiguang')

    chakangengduochanpin= (By.LINK_TEXT,'查看全部百度产品 ')

    baiduyixia = (By.ID, 'su')









