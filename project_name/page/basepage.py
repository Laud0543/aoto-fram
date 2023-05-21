import os
import pickle
import sys
import time

import allure
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import logger
# from utils.logger import Logger
from config import POLL_FREQUENCY,TESTCASE_SUCCESS_DIR,LOCATOR_FAILED_DIR,ASSERT_FAILED_DIR,IMPLICITLY_WAIT_TIME,circulation
from utils.save_screen_shot import screen_shot


# 读取配置参数
# WEB_UI = reda_conf('WEB_UI')
# WEB_POLL_FREQUENCY = WEB_UI.get('WEB_WIMPLICITLY_WAIT_TIME')
# WEB_IMPLICITLY_WAIT_TIME = WEB_UI.get('WEB_POLL_FREQUENCY')

# 读取配置参数
# APP_UI = reda_conf('APP_UI')
# APP_POLL_FREQUENCY = APP_UI.get('APP_POLL_FREQUENCY')
# APP_IMPLICITLY_WAIT_TIME = 5
# PLATFORM = APP_UI.get('APP_PLATFORM')

# 读取 项目类型
# CASE_TYPE = reda_conf('CURRENCY').get('CASE_TYPE')
#
# if CASE_TYPE.lower() == 'web':
#     POLL_FREQUENCY = WEB_POLL_FREQUENCY
#     IMPLICITLY_WAIT_TIME = WEB_IMPLICITLY_WAIT_TIME
# else:
# POLL_FREQUENCY = 0.5
# IMPLICITLY_WAIT_TIME = 5
#circulation=3 循环次数


class BasePage(object):
    xpath = By.XPATH
    link = By.LINK_TEXT
    id = By.ID
    name = By.NAME
    tag = By.TAG_NAME
    cname = By.CLASS_NAME
    css = By.CSS_SELECTOR
    def __init__(self, driver: WebDriver):
        self.driver = driver



    def locator(self,locator):
        """
            :param locator: 元组形式(By.ID,"id")
            :return: 返回element
        """
        try:
            # element = WebDriverWait(self.driver,30).until(ec.presence_of_element_locatord(*locator))
            for i in range(circulation):
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))

                if element is not None:
                    return element
        except TimeoutException as e:
            #后期改为logger
            logger.error(f"寻找{locator}元素时间超时"+str(e), exc_info=True)
            screen_shot(self.driver,n=3)
            raise
#            logger.exception(e) 将异常存入日志




    def click(self,locator):
        self.locator(locator).click()

    #获取元素对象的属性(text,title,name,id,class)
    def get_elenm_attr(self):
        pass




    def input(self,locator,data):
        """
        :param locator: 定位元素
        :param data: 输入需要搜索的内容
        """
        ele = self.locator(locator)
        ele.clear()
        ele.send_keys(data)

    def clear(self, locator):
        self.locator(locator).clear()
    #
    # def find_element(self,locator):
    #     try:
    #       return self.driver.find_element(*(locator))
    #     except:
    #         raise
    #
    # def find_element_click(self,locator):
    #     self.find_element(locator).click()

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def driver_element(self, locator, el: str = None, ):
        """
        返回 element
        :param locator: 定位元素
        :param el: 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        :return: driver 对象
        """

        if el is not None:
            element = WebDriverWait(self.driver, timeout=IMPLICITLY_WAIT_TIME,
                                    poll_frequency=POLL_FREQUENCY).until(
                lambda driver:self.driver.find_elements(*locator))

            return element
        else:
            element = WebDriverWait(self.driver, timeout=IMPLICITLY_WAIT_TIME,
                                    poll_frequency=POLL_FREQUENCY).until(
                lambda driver:self.driver.find_element(*locator))
            return element

    def screen_shot(self, imgreport: bool = False, n: int = 1) -> str or None:
        """
        截取当前界面图片
        :param n: int 默认为1，用例成功截图为1，失败为2，元素定位不到为3
        :param imgreport:  str 图片追加到测试报告 默认添加到报告
        :return:

        """

        # if not os.path.exists("./image"):
        #     os.makedirs("./image")
        filename = str(round(time.time() * 1000)) + ".png"
        if len(filename) >= 200:
            filename = str(round(time.time() * 1000)) + ".png"
        if n == 1:
            filepath = os.path.join(TESTCASE_SUCCESS_DIR, filename)
        elif n == 2:
            filepath = os.path.join(ASSERT_FAILED_DIR, filename)
        elif n == 3:
            filepath = os.path.join(LOCATOR_FAILED_DIR, filename)
        else:
            logger.error('n不在1,2,3取值范围内，默认为1')
            filepath = os.path.join(TESTCASE_SUCCESS_DIR, filename)
        self.driver.save_screenshot(filepath)

        if imgreport:
            pass
            # allure.attach(self.driver.get_screenshot_as_png(),
        #                   name=filename,
        #                   attachment_type=allure.attachment_type.PNG)
        # logger.debug(f"截图成功已经存储在: {filepath}")
        #   return filepath
    #
    # def is_alert_present(self):
    #
    #     try:
    #
    #         self.driver.switch_to.alert()
    #
    #     except NoAlertPresentException as e:
    #
    #         return False
    #
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #
    #     try:
    #
    #         alert = self.driver.switch_to.alert()
    #
    #         alert_text = alert.text
    #
    #         if self.accept_next_alert:
    #
    #             alert.accept()
    #
    #         else:
    #
    #             alert.dismiss()
    #
    #         return alert_text
    #
    #     finally:
    #         self.accept_next_alert = True


        # def screen_shot(self, imgreport: bool = False) -> str or None:
        #     """
        #     截取当前界面图片
        #     :param imgreport:  str 图片追加到测试报告 默认添加到报告
        #     :return:
        #     """
        #
        #     filename = str(round(time.time() * 1000)) + ".png"
        #     if len(filename) >= 200:
        #         filename = str(round(time.time() * 1000)) + ".png"
        #     filepath = os.path.join(PRPORE_SCREEN_DIR, filename)
        #
        #     self.driver.save_screenshot(filepath)
        #     if imgreport:
        #         allure.attach(self.driver.get_screenshot_as_png(),
        #                       name=filename,
        #                       attachment_type=allure.attachment_type.PNG)
        #     logger.debug(f"截图成功已经存储在: {filepath}")
        #     return filepath

    def save_cookie(self, path):
        '''

        :param path: 保存cookie的路径
        :return:
        '''
        with open(path, 'wb') as filehandler:
            cookies = self.driver.get_cookies()
            print(cookies)
            pickle.dump(cookies, filehandler)

    def load_cookie(self,path):
        '''

        :param path:  保存cookie的路径
        :return:

        '''
        with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def delete_cookies(self):
        logger.info("清除cookies")
        self.driver.delete_all_cookies()

    def web_title(self, loadtime : int = 0):
        """
        获取当前web_页面  title
        # loadtime  等待页面加载出title所消耗的时间
        :return:
        """

        self.sleep(loadtime)  # 获取页面标题，等待loadtime秒
        title = self.driver.title
        logger.debug(f"获取当前页面title {title}")
        return title

    @property
    def web_html_content(self):
        """
        获取当前web页面 html内容
        :return:
        """
        content = self.driver.page_source
        logger.debug('获取当前HTML内容')
        return content

    def sleep(self, s: float) -> float or int:
        """
        休眠秒数
        :param s:
        :return:
        """
        if s:
            # logger.debug('强制等待 {} /s'.format(s))
            time.sleep(s)
        else:
            pass

    def web_refresh(self):
        """
        刷新当前页面
        :return:
        """
        logger.debug('刷新当前页面')

        return self.driver.refresh()

    def web_back(self):
        """
        返回上一个页面
        :return:
        """
        # logger.debug('返回上一个页面')
        return self.driver.back()

    def web_forward(self):
        """
        前进到下一个页面
        :return:
        """
        logger.debug('前进到下一个页面')

        return self.driver.forward()

    # 没有click方法
    # def web_baclick(self):
    #     """
    #     点击页面
    #     :return:
    #     """
    #
    #     base_click = self.driver.click()
    #     logger.debug('点击当前页面')
    #     return base_click

    def web_scroll(self, direction: str) -> None:
        """
        网页滚动 部分网页不可用时轻请使用  web_scroll_to_ele
        :param direction: str   up 顶部   Down 底部
        :return:
        """
        if direction == "up":
            logger.debug('滚动到顶部')
            self.driver.execute_script("window.scrollBy(0, -10000);")
        if direction == "down":
            logger.debug('滚动到底部')
            self.driver.execute_script("window.scrollBy(0, 10000)")

    def web_scroll_to_ele(self,locator: tuple, index: int = None) -> None:
        """
        滚动至元素ele可见位置
        :param types: 定位类型
        :param locator: 定位器
        :param index: 多个标签索引
        :return:
        """
        el = None
        if index is not None:
            el = 's'
        target = self.driver_element(locator, el=el)
        logger.debug('滚动页面')
        if index is not None:
            self.driver.execute_script("arguments[0].scrollIntoView();", target[index])
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", target)

    @property
    def web_current_window(self):

        """
        获取当前窗口句柄 不能单一使用 实际获取的不是当前句柄
        :return:
        """
        current_window = self.driver.current_window_handle
        logger.debug('获取当前页面句柄 ')
        return current_window

    @property
    def web_all_handle(self):
        """
        获取所有句柄
        :return:  list
        """
        handle = self.driver.window_handles
        logger.debug('获取所有句柄')
        return handle

    def web_switch_windows(self, index: int):
        """
        多窗口切换
        :param index: 列表索引 all_handle的列表索引位置
        :return:
        """
        handle = self.web_all_handle[index]

        try:
            logger.debug('窗口已经切换')
            return self.driver.switch_to.window(handle)
        except Exception as e:
            logger.debug("查找窗口句柄handle异常-> {0}".format(e))

    def web_switch_frame(self, locator: tuple, index: int = None) -> None:
        """
        #切换到 iframe
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个

        if index is not None:
            el = 'l'
        logger.debug('切换到 iframe')
        if el is not None and index is not None:
            # 多个定位定位 利用index 列表索引点击
            element = self.driver_element(locator=locator, el=el)[index]
            self.driver.switch_to.frame(element)
        else:
            # 单个定位点击
            element = self.driver_element(locator=locator)
            self.driver.switch_to.frame(element)

    def web_switch_default_content(self) -> None:
        """
        返回默认节点
        :return:
        """
        logger.debug('返回到默认节点')
        self.driver.switch_to.default_content()

    def web_switch_parent_frame(self) -> None:
        """
        返回父节点
        :return:
        """
        logger.debug('返回父节点')
        self.driver.switch_to.parent_frame()

    def web_switch_to_alert(self):
        """
        切换焦点到弹框
        """
        try:
            accept = self.driver.switch_to.alert
            logger.debug('切换焦点到弹框')
            return accept
        except Exception as e:
            logger.error("查找alert弹出框异常-> {0}".format(e))

    def web_accept(self) -> None:
        """
        警告框处理 确认
        :return:
        """
        try:
            accept = self.driver.switch_to.alert.accept()
            logger.debug('警告框已确认')
            return accept
        except Exception as e:
            logger.error("查找alert弹出框异常-> {0}".format(e))

    def web_dismiss(self) -> None:
        """
        警告框处理  取消
        :return:
        """
        try:
            accept = self.driver.switch_to.alert.dismiss()
            logger.debug('警告框已取消')
            return accept
        except Exception as e:
            logger.error("查找dismiss弹出框异常-> {0}".format(e))

    def web_alert_text(self) -> None or str:
        """
        警告框处理 提取警告框文本
        :return:
        """
        try:
            accept = self.driver.switch_to.alert.text
            logger.debug(f'警告框文本信息为 {accept}')
            return accept
        except Exception as e:
            logger.error("查找alert弹出框异常-> {0}".format(e))


    def web_get_dropdown_options_count(self, locator: tuple) -> str or None:
        """
        获取下拉选项的个数
        :param types: 定位类型
        :param locator: 定位器
        :return:
        """

        element = self.driver_element(locator)
        sel = Select(element)
        options = sel.options
        logger.debug(f'获取下拉选项的个数:{options}')
        return options

    def web_element_hover(self, locator: tuple):
        """
        获取元素后悬停到元素位置
        :param types: 定位类型
        :param locator: 定位器
        :return:
        """
        element = self.driver_element(locator)
        hover = ActionChains(self.driver).move_to_element(element).perform()
        logger.debug(f"鼠标悬停位置{locator}")
        return hover

    def web_element_hover_clicks(self, locator: tuple, index: int = None) -> None:
        """
        获取元素后悬停到元素位置 后点击该元素
        :param types: 定位类型
        :param locator: 定位器
        :param index: 多个时列表索引
        :return:
        """
        element = self.driver_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        self.sleep(0.5)
        self.often_click(locator=locator, index=index)
        logger.debug(f"鼠标悬停位置{locator} 点击")

    def web_save_as_img(self,locator: tuple, filename: str, sleep: int = 1) -> None or str:
        """
       图片另存为 下载文件也可以直接使用
        :param types: 定位类型
        :param locator: 定位器
        :param filename: 图片名称 路径必须要输入正确 以为函数没办法判断是否成功
        :param sleep: 等待windo 窗口时间 默认 1 秒
        :return: str path 文件路径
        """
        if sys.platform.lower() == 'win32':
            import pyautogui, pyperclip
            # 右键点击
            self.web_right_click(locator=locator)

            # 图片另存为
            pyautogui.typewrite(['V'])

            # 将地址以及文件名复制
            pic_dir = None
            pyperclip.copy(os.path.join(PRPORE_SCREEN_DIR, f'{filename}.jpg'))
            # 等待窗口打开，以免命令冲突，粘贴失败，试过很多次才有0.8，具体时间自己试
            self.sleep(sleep)
            # 粘贴
            pyautogui.hotkey('ctrlleft', 'V')
            # 保存
            pyautogui.press('enter')
            logger.debug(f'图片路径为{filename}！')
            return pic_dir

    def web_selcet_locat(self, locator: tuple, value: str) -> None:
        """
        下拉框操作  **此函数只支持 Select标签 其它标签不支持
        :param types:  定位类型
        :param locator: 定位参数
        :param value:   #选项文字内容
            # 通过index进行选择
            .select_by_index(1)
            # 通过value进行选择
            .select_by_value("2")
            select_by_visible_text("Male")
            # 通过选项文字进行选择
        :return:
        """
        selcet = self.driver_element(locator)
        Select(selcet).select_by_visible_text(value)
        logger.debug('web下拉框选择')

    def is_element_var(self, var) -> bool:
        """
        检查值是否存在
        :param var:查询的值
        :param locator: 定位器
        :return:
        """
        content = self.web_html_content
        if var in content:
            return True
        else:
            return False

    def web_is_element_displayed(self, locator: tuple):
        """
        检查元素是否存在
        :param types:定位类型
        :param locator: 定位器
        :return:
        """
        if locator is not None:

            element = self.driver_element(locator)
            displayed = element.is_displayed()
            if displayed:
                return True
            else:
                return False
        else:
            logger.error('类型定位元素不能为空')

    def web_title_contains(self, text: str) -> bool:
        """
        判断当前页面的title是否包含
        :param text:内容
        :return: bool
        """
        return EC.title_contains(text)(self.driver)

    def web_title_is(self, text: str) -> bool:
        """
        判断当前页面的title是否包含
        :param text:内容
        :return: bool
        """
        return EC.title_is(text)(self.driver)

    def web_send_enter_key(self, locator: tuple, index: int = None) -> None:
        """
        发送回车键
        :param types:
        :param locator:
        :param index:
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('回车键操作')
        if el is not None and index is not None:
            # 多个定位
            self.driver_element(locator=locator, el=el)[index].send_keys(Keys.ENTER)
        else:
            # 单个定位提取文本元素必须是唯一 如果多个时默认返回第一个
            self.driver_element(locator=locator).send_keys(Keys.ENTER)

    def web_send_down_or_up_key(self, locator: tuple, index: int = None, key: str = 'down') -> None:
        """
        按下 键盘 下或者上
        :param types:
        :param locator:
        :param index:
        :param key: down or up
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        logger.debug('键盘上键操作')
        if index is not None:
            el = 'l'

        if key == 'down':
            keys = Keys.DOWN
        else:
            keys = Keys.UP

        if el is not None and index is not None:
            self.driver_element(locator=locator, el=el)[index].send_keys(keys)
        else:
            self.driver_element(locator=locator).send_keys(keys)

    def web_submit(self, locator: tuple, index: int = None) -> None:
        """
        获取元素后  提交 * 前提是input元素的type为submit
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('提交操作')
        if el is not None and index is not None:
            # 多个定位定位 利用index 列表索引点击
            self.driver_element(locator=locator, el=el)[index].submit()
        else:
            # 单个定位点击
            self.driver_element(locator=locator).submit()

    def web_right_click(self, locator: tuple, index: int = None) -> None:
        """
        获取元素后 右键点击
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('web右键点击')
        if el is not None and index is not None:
            element = self.driver_element(locator=locator, el=el)[index].click()
            ActionChains(self.driver).context_click(element).perform()
        else:
            # 单个定位点击
            element = self.driver_element(locator=locator).click()
            ActionChains(self.driver).context_click(element).perform()

    def web_double_click(self,locator: tuple, index: int = None) -> None:
        """
        获取元素后 双击击
        :param types: 定位类型
        :param locator: 定位器
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('web双击点击')
        if el is not None and index is not None:
            element = self.driver_element(locator=locator, el=el)[index]
            ActionChains(self.driver).double_click(element).perform()
        else:
            # 单个定位点击
            element = self.driver_element(locator=locator)
            ActionChains(self.driver).double_click(element).perform()

    def web_js_clear(self,locator: tuple, index: int = None) -> None:
        """
        js方式清除 输入框
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('web js清除操作')
        if el is not None and index is not None:
            element = self.driver_element(locator=locator, el=el)[index]
        else:
            element = self.driver_element(locator=locator)

        self.driver.execute_script("arguments[0].value = '';", element)

    def web_execute_js(self, js: str) -> None:
        """
        执行js
        :param js: js 语法
        """
        logger.debug('web js执行操作')
        self.driver.execute_script(js)

    def web_jsclear_continue_input(self, locator: tuple, text: str, index: int = None) -> None:
        """
        js清除数据在输入
        :param types: 定位类型
        :param locator: 定位元素
        :param text: 输入文本
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        logger.debug('js清除数据在输入')
        self.web_js_clear(locator=locator, index=index)
        self.sleep(0.5)
        self.often_input(locator=locator, text=text, index=index)

    def often_text(self, locator: tuple, index: int = None):
        """
        获取元素  提取文本内容
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置  find_element传递时 此值必填
        :return: driver 对象
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('提取文本内容')
        if el is not None and index is not None:
            # 多个定位
            return self.driver_element(locator=locator, el=el)[index].text
        else:
            # 单个定位提取文本元素必须是唯一 如果多个时默认返回第一个
            return self.driver_element(locator=locator).text

    def often_click(self,locator: tuple, index: int = None) -> None:
        """
        获取元素后  点击
        :param types: 定位类型
        :param locator: 定位元素
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('点击操作')
        if el is not None and index is not None:
            # 多个定位定位 利用index 列表索引点击
            self.driver_element(locator=locator, el=el)[index].click()
        else:
            # 单个定位点击
            self.driver_element(locator=locator).click()

    def  often_input(self,locator: tuple, text: str, index: int = None) -> None:
        """
        获取元素后输入 并支持键盘操作
        :param types: 定位类型
        :param locator:  定位元素或者 表达式
        :param text:  输入内容
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('输入操作')
        if el is not None and index is not None:
            self.driver_element(locator=locator, el=el)[index].send_keys(text)
        else:
            self.driver_element(locator=locator).send_keys(text)

    def often_clear(self,locator: tuple, index: int = None) -> None:
        """
        清除输入框  * 此方法不适用时 请用js_clear
        :param types: 定位类型
        :param locator: 定位元素

        :param index: 列表索引位置  find_element传递时 此值必填
        """
        el = None  # 单个/多个  默认 find_element=None 单个  / 如果 find_element = 's' 多个
        if index is not None:
            el = 'l'
        logger.debug('清除操作')
        if el is not None and index is not None:
            self.driver_element(locator=locator, el=el)[index].clear()
        else:
            self.driver_element(locator=locator).clear()

    def often_clear_continue_input(self, locator: tuple, text: str, index: int = None) -> None:
        """
        清除数据在输入
        :param types: 定位类型
        :param locator: 定位元素
        :param text: 输入文本
        :param index: 列表索引位置  find_element传递时 此值必填
        :return:
        """
        logger.debug('清除数据在输入操作')
        self.often_clear(locator=locator, index=index)
        self.sleep(0.5)
        self.often_input(locator=locator, text=text, index=index)

# def get_code(driver, id):
#     # 获取验证码图片
#     t = time.time()
#     path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
#     picture_name1 = path + '\\' + str(t) + '.png'
#
#     driver.save_screenshot(picture_name1)
#
#     ce = driver.find_element_by_id(id)
#
#     left = ce.location['x']
#     top = ce.location['y']
#     right = ce.size['width'] + left
#     height = ce.size['height'] + top
#
#     dpr = driver.execute_script('return window.devicePixelRatio')
#
#     print(dpr)
#     im = Image.open(picture_name1)
#     img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))
#
#     t = time.time()
#
#     picture_name2 = path + '\\' + str(t) + '.png'
#     img.save(picture_name2)  # 这里就是截取到的验证码图片
#
#     # r = ShowapiRequest("http://route.showapi.com/184-4", "290728", "1bd001f23c874581aac4db788a92c71d")
#
#     r.addFilePara("image", picture_name2)
#     r.addBodyPara("typeId", "34")
#     r.addBodyPara("convert_to_jpg", "0")
#     r.addBodyPara("needMorePrecise", "0")
#     res = r.post()
#     text = res.json()['showapi_res_body']
#     code = text['Result']
#     return code
#
# from PIL import Image
# # from lib.ShowapiRequest import ShowapiRequest