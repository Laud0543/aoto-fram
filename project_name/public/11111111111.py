# import os
# import time
#
# from config import REPORT_PATH
# from utils.logger import logger
#
# logger.info('zahuishia')
#
# logger.error('buduijinga')
#
#
# now = time.strftime('%Y-%m-%d')
# print(now)
#
# now = time.strftime('%Y-%m-%d')
# report = os.path.join(REPORT_PATH,now+'-'+'report.html')
# print(report)



class QaLogger:

    def __init__(self):
        self._step_index = 0
        self._last_log = None

    def info(self, text):
        print(text)
        self._last_log = text

    def step(self, text):
        self._step_index += 1
        print('\nStep {}: {}'.format(self._step_index, text))
        self._last_log = text

    def step_done(self):
        print('Step {}  done!'.format(self._step_index))


logger = QaLogger()

def test_put_new_order():
    logger.step('login...')
    # app.home.login()
    logger.step_done()

    logger.step('close wizard...')
    # app.wizard.close()
    logger.step_done()

    logger.step('put new order')
    # app.order.create_new_order()
    logger.step_done()

def test_hhhh():
    logger.step('login1...')
    # app.home.login()
    logger.step_done()

    logger.step('close1 wizard...')
    # app.wizard.close()
    logger.step_done()

    logger.step('put1 new order')
    # app.order.create_new_order()
    logger.step_done()

if __name__ == '__main__':
   def a():
       print('a')
   print(2,a())