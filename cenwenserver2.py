import pymysql  # 导入pymysql
import serial   # 导入serial
ser = serial.Serial('com7', baudrate=115200, bytesize=8, timeout=2)  # 连接串口
while True:  # 死循环
    db = pymysql.connect("10.0.0.111", "root", "zong123", "test")  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    sqlinsert = "insert into sob values('%d','%d','%d','%d')" % (a, b, f, e)  # 温度数据插入数据库方法
    sqlslect = "select * from sob where id = %d" % (row)  # 查询时间数据方法
    # cursor.execute(sqlinsert) # 执行插入数据操作
    # db.commit()
    cursor.execute(sqlslect)  # 执行查询数据操作
    db.commit()
    t = cursor.fetchall()  # 返回查询数据，十进制
    t = t[0]  # t为（（*），）型数据，访问第一个元组
    aa = t[0]
    bb = t[1]
    cc = t[2]
    dd = t[3]
    print('data read from database:',(aa,bb,cc,dd))  # 打印从数据库获取的数据，十进制
    y = [0xFC,0x08,0x03,0x01,0xFF,0xFF,aa,bb,cc,dd]  # 发给协调器的数据，十进制
    ser.write(y)  # 执行发给协调器数据的操作
    cursor.close()  # 数据库游标关闭
    db.close()  # 数据库关闭
#    d = tuple(ser.read(10))  # 接收测温模块数据，read为字节长度
#     if  not d:  # 未接收到数据，继续
#         continue
#     for c in d:  # 遍历接收的数据，温度数据
#         print('received data from router',int(c))
#     a = int(d[0])
#     b = int(d[1])
#     f = int(d[2])
#     e = int(d[3])