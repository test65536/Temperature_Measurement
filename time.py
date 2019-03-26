import time
import pymysql  # 导入pymysql
while True:
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(type(b))
    db = pymysql.connect("10.0.0.111", "root", "zong123", "test")  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    sqlinsert = "insert into sob values('%s','%d','%d','%d')" % (b, 1, 2, 3)  # 第一列时间字符串温度数据插入数据库方法
    cursor.execute(sqlinsert) # 执行插入数据操作
    db.commit()
    time.sleep(10)