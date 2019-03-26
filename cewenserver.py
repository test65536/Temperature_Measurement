from socket import *
import threading as td
import pymysql
import serial
def database(d): #数据库连接
    global t
    db = pymysql.connect("10.0.0.111", "root", "zong123", "test")  # 打开数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    for s in d:
        a = s[0]
        b = s[1]
        c = s[2]
        e = s[3]
    sqlinsert = "insert into sob values('%d','%d','%d','%d')" % (a,b,c,e) #插入数据
    sqlslect = "select * from sob" #查询数据
    try:
        cursor.execute(sqlinsert)
        db.commit()
        # data = cursor.fetchall()
        # for row in data:
        #     print(row)
    except:
        db.rollback()
    try:
        cursor.execute(sqlslect)
        db.commit()
        t = cursor.fetchall() #返回测试时间间断
    except:
        db.rollback()
    cursor.close()
    db.close()
    return t
def zigbee(): #定时接收来自zigbee的信息，同时写入数据库
    global d
    c = []
    ser = serial.Serial('com5', baudrate=115200, bytesize=8, timeout=2)#连接串口
    # while( True ):
    d = ser.read(10)
    for c in d:
        print(hex(c))
    r = database(c)
    ser.write(r)
thread1 = td.Thread(target=zigbee,args=())
thread1.start()
thread1.join()
print('加入主线程成功')
