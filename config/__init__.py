import os
import time
import sys
from utils.file_reader import YamlReader

__all__ = ['BASE_DIR', 'TESTCASE_SUCCESS_DIR', 'LOCATOR_FAILED_DIR', 'ASSERT_FAILED_DIR', 'POLL_FREQUENCY',
           'IMPLICITLY_WAIT_TIME', 'circulation', 'url', 'p', 'REPORTPATH' ]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 测试截图目录
TESTCASE_SUCCESS_DIR = os.path.join(BASE_DIR, "output", 'screen_shoots', "testcase_success_screen")
LOCATOR_FAILED_DIR = os.path.join(BASE_DIR, "output", 'screen_shoots', "locator_failed_screen")
ASSERT_FAILED_DIR = os.path.join(BASE_DIR, "output", 'screen_shoots', "testcase_failed_screen")

REPORTPATH = 'D:\\python_file\\auto_fram_5.9\output\\report\\'
# 间隔多长时间再次寻找元素
POLL_FREQUENCY = 0.5

# 显示等待时长
IMPLICITLY_WAIT_TIME = 10

# 定位元素循环次数
circulation = 1

# 首页url
url = 'https://www.baidu.com/'


p = 1  # 运行用例的级别



# 所有相关文件的路径

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'output', 'report')


class Config:
    def __init__(self, config=CONFIG_FILE):
        # print('配置文件地址：',config)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

#邮件配置
message='这是今天的测试报告，请查收！', #标题
receiver='',  #邮件接收人,接受list
server='smtp.163.com', #邮件服务器
sender='',  # 发送者
password=''  #开启邮件服务器密码


# database configuration
__DATABASE_HOST = "127.0.0.1"
__DATABASE_PORT = "3306"
__DATABASE_USER = "root"
__DATABASE_PASSWORD = "password"
__DATABASE_NAME = "demo"


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_PATH)