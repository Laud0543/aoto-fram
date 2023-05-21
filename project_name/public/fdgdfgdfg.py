import pymysql

db = pymysql.connect(host='localhost',user='root',db='test',

           password='123456',port=3306,charset='utf8')

cursor = db.cursor()

cursor.execute('select * from test1')

aa = cursor.fetchone()

print(aa)

# 注意这一句一定是在循环之外，不能放到循环里面。想想这是为什么？

# cursor.execute('select * from student')
#
# for i in range(aa[0]):
#
#   a,b = cursor.fetchone()
#
#   if b == "女":
#
#     a = "我叫{}，我是一个学生！".format(a)
#
#     print(a)

db.close()