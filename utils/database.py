import sys
import logging
import pymysql
# import cx_Oracle
# from pyhive import sqlalchemy_hive, hive

# from clickhouse_driver import Client


# from pyspark.sql import HiveContext
# from pyspark import SparkConf, SparkContext

# 加入日志
# 获取logger实例
logger = logging.getLogger("dbSql")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("dbSql.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)


class DbConnect(object):
    """
	封装Mysql/Oracle/Hive/Clickhouse数据库基本操作函数
	"""
    __slots__ = ('_host', '_user', '_password', '_port', '_database', 'conn', 'cursor')

    def __init__(self, host, user, password, port, database):
        """
		魔术方法, 初始化, 构造函数
		:param host: IP
		:param user: 用户名
		:param password: 密码
		:param port: 端口号
		:param database: 数据库名
		"""
        self._host = host
        self._user = user
        self._password = password
        self._port = port
        self._database = database
        self.conn = None
        self.cursor = None

    def connectDb(self, connectType=None):
        """
		建立数据库连接
		:param connectType: 数据库类型->Mysql/Oracle/Hive/Clickhouse
		:return: 是否连接成功
		"""
        try:
            if connectType == 'Mysql':
                self.conn = pymysql.connect(host=self._host, user=self._user, password=self._password, port=self._port,
                                            database=self._database, charset='utf8', connect_timeout=10)
                self.cursor = self.conn.cursor()  # 使用cursor()方法获取操作游标
            # elif connectType == 'Oracle':
            #     self.conn = cx_Oracle.connect(
            #         self._user + "/" + self._password + "@" + self._host + ":" + self._port + "/" + self._database)
            #     self.cursor = self.conn.cursor()
            # elif connectType == 'Hive':
            #     self.conn = hive.Connection(host=self._host, port=self._port, database=self._database)
            #     self.cursor = self.conn.cursor()
            # elif connectType == 'Clickhouse':
            #     self.conn = Client(host=self._host, port=self._port, user=self._user, password=self._password,
            #                        database=self._database, send_receive_timeout=10)
        except Exception as e:
            logger.error("connectDatabase failed")
            print(e)
            return False
        return True

    def close(self):
        """
		关闭游标和数据库连接
		:return:
		"""
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        else:
            pass
        return True

    def execute_sql(self, sql, connectType=None, commit=False):
        """
		执行数据库的sql语句
		:param sql:
		:param params:
		:param connectType: 连接的数据库类型
		:param commit:
		:return:
		"""
        res = self.connectDb(connectType)  # 连接数据库
        if not res:
            return False
        try:
            if self.conn and self.cursor:
                rowcount = self.cursor.execute(sql)  # execute循环单条插入
                # rowcount = self.cursor.executemany(sql, params) # executemany批量插入
                # print(rowcount)

                if commit:
                    self.conn.commit()
                else:
                    pass
                return rowcount
        except Exception as e:
            logger.error("execute failed: " + sql)
            # logger.error("params: " + str(params))
            print(e)
            # self.conn.rollback()  # 发生错误时会滚
            self.close()
            return False


    def fetchall(self, sql, connectType=None, params=None):
        """
		fetchall() 方法获取所有数据
		:param sql:
		:param params:
		:param connectType: 连接的数据库类型
		:return:
		"""
        res = self.execute_sql(sql, connectType)
        if not res:
            logger.info("查询失败")
            return False
        self.close()
        results = self.cursor.fetchall()
        logger.info("查询成功" + str(results))
        return results

    def fetchone(self, sql, connectType=None, params=None):
        """
		fetchone() 方法获取一条数据
		:param sql:
		:param params:
		:param connectType: 连接的数据库类型
		:return:
		"""
        res = self.execute_sql(sql, connectType)
        if not res:
            logger.info("查询失败")
            return False
        self.close()
        result = self.cursor.fetchone()
        logger.info("查询成功" + str(result))
        return result

    def edit(self, sql, connectType=None, params=None):
        """
		增删改数据库操作
		:param sql:
		:param connectType: 连接的数据库类型
		:return:
		"""
        res = self.execute_sql(sql, connectType, True)
        if not res:
            logger.info("操作失败")
            return False
        self.conn.commit()
        self.close()
        logger.info("操作成功" + str(res))
        return res

    def ClickhouseExecute(self, sql, connectType=None):
        """
		执行数据库的sql语句
		:param sql:
		:param connectType: 连接的数据库类型
		:return:
		"""
        res = self.connectDb(connectType)  # 连接数据库
        if not res:
            return False
        try:
            if self.conn:
                rowcount = self.conn.execute(sql)
                return rowcount
        except Exception as e:
            logger.error("execute failed: " + sql)
            print(e)
            # self.conn.rollback()  # 发生错误时会滚
            self.close()
            return False



if __name__ == '__main__':

    # mysql连接
    mconn = DbConnect("127.0.0.1", "root", "123456", 3306, "test")
    sql = "select * from test1;"
    values = 1
    result1 = mconn.fetchall(sql, 'Mysql')
    result2 = mconn.fetchone(sql, 'Mysql')

# hive连接
# hconn = DbConnect("10.0.0.0", None, None, 10000, "database")
# sql = "select * from database.table limit1;"
# result = hconn.fetchall(sql, 'Hive')

# clickhouse连接
# cconn = DbConnect("10.0.0.0", "bigdata", "bigdata", 66666, "database")
# sql = "select * from database.table limit 1;"
# result = cconn.ClickhouseExecute(sql, 'Clickhouse')
# print(result)


# ==========================================================================================


# # encoding: utf-8
# """
# @desc: MySQL client. Manage the access evidence, wrap the common action, improve the performance, keep the security.
# """
# import MySQLdb
# import glog
# from DBUtils.PooledDB import PooledDB
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # database configuration
# __DATABASE_HOST = "127.0.0.1"
# __DATABASE_PORT = "3306"
# __DATABASE_USER = "root"
# __DATABASE_PASSWORD = "password"
# __DATABASE_NAME = "demo"
#
# # database connection pool configuration
# __NUM_DEFAULT_CONNECTION = 10
#
#
# def get_mysql_connection_pool():
#     """
#     Database connection to the server using the connection pool.
#     :return: database connection
#     """
#     db_host = __DATABASE_HOST
#     db_port = __DATABASE_PORT
#     db_user = __DATABASE_USER
#     db_password = __DATABASE_PASSWORD
#     db_name = __DATABASE_NAME
#
#     num_connection = __NUM_DEFAULT_CONNECTION
#
#     connection_pool = PooledDB(MySQLdb, num_connection,
#                                host=db_host, port=db_port, user=db_user, passwd=db_password, db=db_name)
#
#     return connection_pool
#
#
# def get_session():
#     """
#     Used by ORM framework.
#     """
#     db_host = __DATABASE_HOST
#     db_port = __DATABASE_PORT
#     db_user = __DATABASE_USER
#     db_password = __DATABASE_PASSWORD
#     db_name = __DATABASE_NAME
#
#     engine = create_engine('mysql+mysqlconnector://'
#                            + db_user + ':' + db_password + '@' + db_host + ':' + db_port + '/' + db_name)
#     da_session = sessionmaker(bind=engine)
#     session = da_session()
#     return session
#
#
# def watch_prepared_statement(sql, params):
#     """
#     When we use prepared sql statement, the program doesn't the real sql neither in the python program or
#     database process. This function will parse the expected sql statement for debugging.
#     """
#     expected_sql = sql % tuple(params)
#     return expected_sql
#
#
# class MysqlClient(object):
#     """
#     Package actions about the database.
#     """
#     def __init__(self):
#         self.connection_pool = get_mysql_connection_pool()
#
#     def query(self, sql, params=None):
#         """
#         Query action.
#         :param sql: being executed sql statement
#         :param params: sql param, to avoid the sql injection
#         :return: Query Result
#         :rtype: list
#         """
#         connection = self.connection_pool.connection()
#         cursor = connection.cursor()
#
#         if params is None:
#             params = []
#         try:
#             cursor.execute(str(sql), params)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             expected_sql = watch_prepared_statement(sql, params)
#             glog.error("[" + str(e) + "]" + expected_sql)
#             result = None
#         finally:
#             # release the connection to the pooled
#             cursor.close()
#             connection.close()
#
#         return result
#
#     def update(self, sql, params=None):
#         """
#         Update action.
#         :param sql: being executed sql statement
#         :param params: sql param, to avoid the sql injection
#         :return: affected rows count and the last row id
#         :rtype: tuple
#         """
#         connection = self.connection_pool.connection()
#         cursor = connection.cursor()
#
#         if params is None:
#             params = []
#         try:
#             cursor.execute(str(sql), params)
#             row_count = cursor.rowcount
#             row_id = cursor.lastrowid
#             connection.commit()
#             result = row_count, row_id
#         except Exception as e:
#             expected_sql = watch_prepared_statement(sql, params)
#             glog.error("[" + str(e) + "]" + expected_sql)
#             result = None
#         finally:
#             # release the connection to the pooled
#             cursor.close()
#             connection.close()
#
#         return result
#
#     def get_connection(self):
#         """
#         Other actions. Return the connection to finish other operations, such as executemany and so on.
#         """
#         return self.connection_pool.connection()
#
#
# __mysql_client = MysqlClient()
#
#
# def get_mysql_client():
#     """
#     Initialize the singleton object.
#     """
#     return __mysql_client
