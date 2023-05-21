import unittest

from project_name.testcase import all_testcase
def Case_Suite():
    suite = unittest.TestSuite()

    for classname in all_testcase:
        suite.addTest(unittest.makeSuite(classname))
    return suite





    # unittest.main()

    # suite = unittest.TestSuite()
    # --------------------------------------------------------------------------------------

    # suite.addTest(test_News("test_hot_news5")) #添加 单条用例
    # suite.addTest(test_News('test_input_search')) # 添加单条用例
    # --------------------------------------------------------------------------------------

    # caselist=[test_News('test_rednews') , test_News('test_lunbonews7')] # 添加多条用例
    # suite.addTests(caselist)

    # --------------------------------------------------------------------------------------
    # suite.addTest(unittest.makeSuite(test_News))  # 添加单个模块用例
    # --------------------------------------------------------------------------------------
    # 添加多个模块
    # suite1=unittest.TestLoader().loadTestsFromTestCase(test_News)
    # suite2=unittest.TestLoader().loadTestsFromTestCase(test_main_page)
    # suite=unittest.TestSuite([suite1, suite2])
    # --------------------------------------------------------------------------------------

    # suite = unittest.defaultTestLoader.discover("testcase", "test*.py")
    # #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
