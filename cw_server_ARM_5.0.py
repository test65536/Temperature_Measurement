
import pymysql  # 导入pymysql
import serial   # 导入serial
import time
class crc16:
    auchCRCHi = [0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40]

    auchCRCLo = [0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06, \
                 0x07, 0xC7, 0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D, 0xCD, \
                 0x0F, 0xCF, 0xCE, 0x0E, 0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, \
                 0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9, 0x1B, 0xDB, 0xDA, 0x1A, \
                 0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC, 0x14, 0xD4, \
                 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13, 0xD3, \
                 0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, \
                 0xF2, 0x32, 0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4, \
                 0x3C, 0xFC, 0xFD, 0x3D, 0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A, \
                 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38, 0x28, 0xE8, 0xE9, 0x29, \
                 0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF, 0x2D, 0xED, \
                 0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26, \
                 0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60, \
                 0x61, 0xA1, 0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7, 0x67, \
                 0xA5, 0x65, 0x64, 0xA4, 0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, \
                 0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB, 0x69, 0xA9, 0xA8, 0x68, \
                 0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA, 0xBE, 0x7E, \
                 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75, 0xB5, \
                 0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, \
                 0x70, 0xB0, 0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92, \
                 0x96, 0x56, 0x57, 0x97, 0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C, \
                 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E, 0x5A, 0x9A, 0x9B, 0x5B, \
                 0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89, 0x4B, 0x8B, \
                 0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C, \
                 0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42, \
                 0x43, 0x83, 0x41, 0x81, 0x80, 0x40]

    def __init__(self):
        pass

    def createcrc(self, array):
        crchi = 0xff
        crclo = 0xff
        for i in range(0, len(array)):
            crcIndex = crchi ^ array[i]
            crchi = crclo ^ self.auchCRCHi[crcIndex]
            crclo = self.auchCRCLo[crcIndex]
        return (crchi << 8 | crclo)

    def createarray(self, array):
        crcvalue = self.createcrc(array)
        array.append(crcvalue >> 8)
        array.append(crcvalue & 0xff)
        return array

    def calcrc(self, array):
        crchi = 0xff
        crclo = 0xff
        lenarray = len(array)
        for i in range(0, lenarray - 2):
            crcIndex = crchi ^ array[i]
            crchi = crclo ^ self.auchCRCHi[crcIndex]
            crclo = self.auchCRCLo[crcIndex]
        if crchi == array[lenarray - 2] and crclo == array[lenarray - 1]:
            return 0
        else:
            return 1

# 连接串口 linux- /dev/ttyUSB0 win-com7
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, timeout=2)  # 连接串口 arm /dev/ttyUSB0
db = pymysql.connect("10.0.0.111", "root", "zong123", "test")  # 连接数据库
cursor = db.cursor()  # 使用cursor()方法获取操作游标
# sqlinsert = "insert into sob values('%d','%d','%d','%d')" % (a, b, f, e)  # 温度数据插入数据库方法
# sqlslect = "select * from sob where id = %d" % (row)  # 查询时间数据方法
while True:
    sqlslect1 = "select * from addrtable"  # 查询信息表行数
    cursor.execute(sqlslect1)
    db.commit()
    time_addr_table = cursor.fetchall()  # 加一个for循环遍历所有设备地址以及是否为新设备（未加！）
    # print(time_addr_table)
    print("设备总数:", len((time_addr_table)))
    for tat in time_addr_table:
        # print(type(tat))
        sleep_time = tat[0]  # 设备休眠时间
        sleep_time_h = sleep_time//256
        sleep_time_l = sleep_time % 256
        addr = tat[1]  # 设备地址
        # print(tat)
        new_old = tat[2]  # 判断新旧设备的条件

        # 写入新设备地址
        if new_old == 'N':
            # 写入数据校验码
            flag_write = 0
            flag_write_sleep = 0
            while True:
                flag_write += 1
                write_crc = crc16()
                array = [0xFF, 0x10, 0x00, 0x01, 0x00, 0x01, 0x02, 0x00, addr]  # 校验数据
                print(hex(write_crc.createcrc(array)).upper())  # 输出校验码
                write_crc_raw = hex(write_crc.createcrc(array)).upper()  # 赋值校验码
                if len(write_crc_raw) == 5:
                    write_crc_h = write_crc_raw[2]  # 写入crc校验高位，原始crc的低位
                    write_crc_l = write_crc_raw[3:]  # 写入crc校验低位，原始crc的高位
                elif len(write_crc_raw) == 6:
                    write_crc_h = write_crc_raw[2:4]  # 写入crc校验高位，原始crc的低位
                    write_crc_l = write_crc_raw[4:]  # 写入crc校验低位，原始crc的高位
                print(write_crc_h, write_crc_l)
                write_zigbee = [0xFC, 0x0F, 0x03, 0x01, 0xFF, 0xFF, 0xFF, 0x10, 0x00, 0x01,
                                0x00, 0x01, 0x02, 0x00, addr, int(write_crc_h, 16), int(write_crc_l, 16)]
                print(write_zigbee)
                ser.write(write_zigbee)  # 执行发给协调器数据的操作
                print("已执行写入地址。。。。。")
                # 读取从站是否修改地址成功
                time.sleep(1)
                read_crc = crc16()

                array = [addr, 0x03, 0x00, 0x01, 0x00, 0x01]
                print(hex(read_crc.createcrc(array)).upper())
                read_crc_raw = hex(read_crc.createcrc(array)).upper()
                if len(read_crc_raw) == 5:
                    read_crc_h = read_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                    read_crc_l = read_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
                elif len(read_crc_raw) == 6:
                    read_crc_h = read_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                    read_crc_l = read_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
                # 读取zigbee地址发给协调器的数据，含十进制
                print(addr, "//////////")
                print('......', read_crc_h, read_crc_l)
                read_zigbee_addr = [0xFC, 0x0C, 0x03, 0x01, 0xFF, 0xFF, addr, 0x03, 0x00,
                                    0x01, 0x00, 0x01, int(read_crc_h, 16), int(read_crc_l, 16)]
                i = 0
                while True:
                    global flag_read
                    flag_read = 0
                    ser.write(read_zigbee_addr)  # 执行发给协调器数据的操作
                    read_addr = tuple(ser.read(20))  # 接收模块地址数据，read为字节长度
                    print(read_addr)
                    if len(read_addr) == 0 or (read_addr[0] == 247 and read_addr[1] == 255):
                        print("地址%d读取失败" % addr)
                        i = i + 1
                    elif addr == read_addr[4]:
                        print("地址%d写入成功" % addr)
                        flag_read = 1
                        break
                    if i > 2:
                        break
                if flag_read == 1:
                    cursor.execute("update addrtable set New_Old='O' where addr = '%d'" % addr)  # 执行插入数据操作
                    db.commit()
                    break
                if flag_write == 2:
                    print("设备%02d异常，无法写入数据参数\n!!!!!!!!!!" % addr)
                    error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sqlinsert_error = "insert into errortable values('%s','%d')" % (error_time, addr)
                    cursor.execute(sqlinsert_error)  # 执行插入数据操作
                    db.commit()
                    print("异常设备%02d写入数据完成\n-----------------------------" % addr)
                    print("请检查新加的设备是否有问题！！！")
                    break

            # 写入睡眠时间crc16校验
            write_sleep_crc = crc16()
            array = [addr, 0x10, 0x00, 0x04, 0x00, 0x01, 0x02, sleep_time_h, sleep_time_l]
            write_sleep_crc_raw = hex(write_sleep_crc.createcrc(array)).upper()
            if len(write_sleep_crc_raw) == 5:
                write_sleep_crc_h = write_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                write_sleep_crc_l = write_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            elif len(write_sleep_crc_raw) == 6:
                write_sleep_crc_h = write_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                write_sleep_crc_l = write_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            # 计算查询睡眠时间crc16校验
            read_sleep_crc = crc16()
            array = [addr, 0x03, 0x00, 0x04, 0x00, 0x01]
            read_sleep_crc_raw = hex(read_sleep_crc.createcrc(array)).upper()
            if len(read_sleep_crc_raw) == 5:
                read_sleep_crc_h = read_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                read_sleep_crc_l = read_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            elif len(read_sleep_crc_raw) == 6:
                read_sleep_crc_h = read_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                read_sleep_crc_l = read_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            write_sleep_zigbee = [0xFC, 0x0F, 0x03, 0x01, 0xFF, 0xFF, addr, 0x10, 0x00,
                                  0x04, 0x00, 0x01, 0x02, sleep_time_h, sleep_time_l,
                                  int(write_sleep_crc_h, 16), int(write_sleep_crc_l, 16)]

            read_sleep_time = [0xFC, 0x0C, 0x03, 0x01, 0xFF, 0xFF, addr, 0x03, 0x00, 0x04,
                               0x00, 0x01, int(read_sleep_crc_h, 16), int(read_sleep_crc_l, 16)]

            refer_sleep_flag_N = 0
            while True:
                ser.write(write_sleep_zigbee)  # 执行写入睡眠时间操作
                time.sleep(1)
                ser.write(read_sleep_time)  # 执行查询睡眠时间操作
                read_sleep_time_data = tuple(ser.read(20))  # 读取查询睡眠时间
                if not read_sleep_time_data:  # 未接收到数据，继续
                    print("睡眠时间%02d没有收到数据" % addr)
                    refer_sleep_flag_N += 1
                elif read_sleep_time_data[0] == 247 and read_sleep_time_data[1] == 255:
                    print("睡眠时间%02d接收到错误数据" % addr)
                    refer_sleep_flag_N += 1
                else:
                    break
                if refer_sleep_flag_N > 7:
                    # print("设备%d异常，无法接收数据！！！" % addr)
                    print("睡眠时间%02d异常，无法接收数据\n!!!!!!!!!!" % addr)
                    error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sqlinsert_error = "insert into errortable values('%s','%d')" % (error_time, addr)
                    cursor.execute(sqlinsert_error)  # 执行插入数据操作
                    db.commit()
                    print("睡眠时间异常设备%02d写入数据完成\n-----------------------------" % addr)
                    break

        # 读取温度电压数据
        elif new_old == 'O':  # 执行查询数据功能。。。。。。。。。。。。。。。。。。。。
            # 查询电压温度数据crc16校验
            send_crc = crc16()
            array = [addr, 0x03, 0x00, 0x02, 0x00, 0x02]
            # print(hex(send_crc.createcrc(array)).upper())
            send_crc_raw = hex(send_crc.createcrc(array)).upper()
            if len(send_crc_raw) == 5:
                send_crc_h = send_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                send_crc_l = send_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            elif len(send_crc_raw) == 6:
                send_crc_h = send_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                send_crc_l = send_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            # #写入睡眠时间crc16校验
            # write_sleep_crc = crc16()
            # array = [addr, 0x10, 0x00, 0x04, 0x00, 0x01,0x02,sleep_time_h,sleep_time_l]
            # write_sleep_crc_raw = hex(write_sleep_crc.createcrc(array)).upper()
            # if len(write_sleep_crc_raw) == 5:
            #     write_sleep_crc_h = write_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
            #     write_sleep_crc_l = write_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            # elif len(write_sleep_crc_raw) == 6:
            #     write_sleep_crc_h = write_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
            #     write_sleep_crc_l = write_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            # # 计算查询睡眠时间crc16校验
            # read_sleep_crc = crc16()
            # array = [addr, 0x03, 0x00, 0x04, 0x00, 0x01]
            # read_sleep_crc_raw = hex(read_sleep_crc.createcrc(array)).upper()
            # if len(read_sleep_crc_raw) == 5:
            #     read_sleep_crc_h = read_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
            #     read_sleep_crc_l = read_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            # elif len(read_sleep_crc_raw) == 6:
            #     read_sleep_crc_h = read_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
            #     read_sleep_crc_l = read_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位

            # 读取zigbee温度发给协调器的数据，含十进制
            refer_zigbee = [0xFC, 0x0C, 0x03, 0x01, 0xFF, 0xFF, addr, 0x03, 0x00,
                            0x02, 0x00, 0x02, int(send_crc_h, 16),int(send_crc_l, 16)]

            # write_sleep_zigbee =[0xFC, 0x0F, 0x03, 0x01, 0xFF, 0xFF, addr, 0x10, 0x00,
            #                      0x04, 0x00, 0x01,0x02,sleep_time_h,sleep_time_l,
            #                      int(write_sleep_crc_h, 16),int(write_sleep_crc_l, 16)]

            # read_sleep_time = [0xFC, 0x0C, 0x03, 0x01, 0xFF, 0xFF,addr, 0x03, 0x00, 0x04,
            #                    0x00, 0x01,int(read_sleep_crc_h,16),int(read_sleep_crc_l, 16)]

            # refer_sleep_flag = 0
            # while True:
            #     ser.write(write_sleep_zigbee)  # 执行写入睡眠时间操作
            #     time.sleep(1)
            #     ser.write(read_sleep_time)   # 执行查询睡眠时间操作
            #     read_sleep_time_data = tuple(ser.read(20))  # 读取查询睡眠时间
            #     if not read_sleep_time_data:  # 未接收到数据，继续
            #         print("睡眠时间%02d没有收到数据" % addr)
            #         refer_sleep_flag += 1
            #     elif read_sleep_time_data[0] == 247 and read_sleep_time_data[1] == 255:
            #         print("睡眠时间%02d接收到错误数据" % addr)
            #         refer_sleep_flag += 1
            #     else:
            #         break
            #     if refer_sleep_flag > 7:
            #         # print("设备%d异常，无法接收数据！！！" % addr)
            #         print("睡眠时间%02d异常，无法接收数据\n!!!!!!!!!!" % addr)
            #         error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #         sqlinsert_error = "insert into errortable values('%s','%d')" % (error_time, addr)
            #         cursor.execute(sqlinsert_error)  # 执行插入数据操作
            #         db.commit()
            #         print("睡眠时间异常设备%02d写入数据完成\n-----------------------------" % addr)
            #         break

            # 如果接收数据失败，重复执行5次
            refer_flag = 0
            while True:
                while True:
                    ser.write(refer_zigbee)  # 执行发给协调器数据的操作
                    d = tuple(ser.read(20))  # 接收测温模块数据，read为字节长度
                    if not d:  # 未接收到数据，继续
                        print("设备%02d没有收到数据"% addr)
                        refer_flag += 1
                        # continue

                    if d:
                        if d[0] == 247 and d[1] == 255:
                            print("设备%02d接收到错误数据" % addr)
                            refer_flag += 1
                        else:
                            break
                    if refer_flag > 7:
                        # print("设备%d异常，无法接收数据！！！" % addr)
                        break

                if refer_flag > 7:
                    print("设备%02d异常，无法接收数据\n!!!!!!!!!!" % addr)
                    error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sqlinsert_error = "insert into errortable values('%s','%d')" % (error_time, addr)
                    cursor.execute(sqlinsert_error)  # 执行插入数据操作
                    db.commit()
                    print("异常设备%02d写入数据完成\n-----------------------------" % addr)
                    break
                print("原始数据:", d)
                tem_h = hex(d[3])[2:]  # 温度数据高位，字符串
                tem_l = hex(d[4])[2:]  # 温度数据低位，字符串
                v_h = hex(d[5])[2:]  # 电池电压数据高位，字符串
                v_l = hex(d[6])[2:]  # 电池电压数据低位，字符串
                received_crc_raw_h = hex(d[7])[2:].upper()  # 提取接收数据校验码高位，字符串
                received_crc_raw_l = hex(d[8])[2:].upper()  # 提取接收数据校验码低位，字符串
                # print(received_crc_raw_h, received_crc_raw_l)
                # 计算接收数据crc校验
                received_crc = crc16()
                array = [addr, 0x03, 0x04, int(tem_h, 16), int(tem_l, 16), int(v_h, 16), int(v_l, 16)]
                # print(hex(received_crc.createcrc(array)).upper(), "\n")

                cal_received_crc_raw = hex(received_crc.createcrc(array)).upper()
                if len(cal_received_crc_raw) == 5:
                    cal_received_crc_h = cal_received_crc_raw[2]  # 计算接收数据crc校验高位，原始crc的低位,字符串
                    cal_received_crc_l = cal_received_crc_raw[3:]  # 计算接收数据crc校验低位，原始crc的高位,字符串
                elif len(send_crc_raw) == 6:
                    cal_received_crc_h = cal_received_crc_raw[2:4]  # 计算接收数据crc校验高位，原始crc的低位,字符串
                    cal_received_crc_l = cal_received_crc_raw[4:]  # 计算接收数据crc校验低位，原始crc的
                # print(cal_received_crc_h, cal_received_crc_l)
                # 判断接收数据是否正确
                if (cal_received_crc_h == received_crc_raw_h
                        and cal_received_crc_l == received_crc_raw_l):  # 判断是否自己计算的校验码==收到的校验码，是继续，否不写入
                    print('设备%02d接收的数据校验成功！即将写入数据库！' % addr)
                    tem = tem_h + tem_l  # 温度数据字符串高低位拼接，
                    vol = v_h + v_l  # 电池电压数据字符串高低位拼接，
                    # print(tem)
                    # print("接收数据:",int(tem,16))
                    print("%02d-当前时间:" % addr,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    print("%02d-tem is %0.1f ℃" % (addr, int(tem, 16) * 0.1))
                    print('%02d-voltage is %0.0f mV' % (addr, int(vol, 16)))
                    # temtable 赋值
                    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    ad = refer_zigbee[6]
                    tem_dec = int(tem, 16) * 0.1
                    v = int(vol, 16) * 0.001
                    # 温度数据插入数据库方法
                    sqlinsert = "insert into temtable values('%s','%d','%.1f','%.3f')" % (t, ad, tem_dec, v)
                    cursor.execute(sqlinsert)  # 执行插入数据操作
                    db.commit()
                    print("设备%02d写入数据完成\n-----------------------------" % addr)
                    break
                else:
                    print('设备%02d接收的数据校验失败！！！！！！！！！' % addr)
                    continue
        elif new_old == 'T':

            # 写入睡眠时间crc16校验
            write_sleep_crc = crc16()
            array = [addr, 0x10, 0x00, 0x04, 0x00, 0x01, 0x02, sleep_time_h, sleep_time_l]
            write_sleep_crc_raw = hex(write_sleep_crc.createcrc(array)).upper()
            if len(write_sleep_crc_raw) == 5:
                write_sleep_crc_h = write_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                write_sleep_crc_l = write_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            elif len(write_sleep_crc_raw) == 6:
                write_sleep_crc_h = write_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                write_sleep_crc_l = write_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            # 计算查询睡眠时间crc16校验
            read_sleep_crc = crc16()
            array = [addr, 0x03, 0x00, 0x04, 0x00, 0x01]
            read_sleep_crc_raw = hex(read_sleep_crc.createcrc(array)).upper()
            if len(read_sleep_crc_raw) == 5:
                read_sleep_crc_h = read_sleep_crc_raw[2]  # 发送crc校验高位，原始crc的低位
                read_sleep_crc_l = read_sleep_crc_raw[3:]  # 发送crc校验低位，原始crc的高位
            elif len(read_sleep_crc_raw) == 6:
                read_sleep_crc_h = read_sleep_crc_raw[2:4]  # 发送crc校验高位，原始crc的低位
                read_sleep_crc_l = read_sleep_crc_raw[4:]  # 发送crc校验低位，原始crc的高位
            write_sleep_zigbee = [0xFC, 0x0F, 0x03, 0x01, 0xFF, 0xFF, addr, 0x10, 0x00,
                                  0x04, 0x00, 0x01, 0x02, sleep_time_h, sleep_time_l,
                                  int(write_sleep_crc_h, 16), int(write_sleep_crc_l, 16)]

            read_sleep_time = [0xFC, 0x0C, 0x03, 0x01, 0xFF, 0xFF, addr, 0x03, 0x00, 0x04,
                               0x00, 0x01, int(read_sleep_crc_h, 16), int(read_sleep_crc_l, 16)]

            refer_sleep_flag_N = 0
            while True:
                ser.write(write_sleep_zigbee)  # 执行写入睡眠时间操作
                time.sleep(1)
                ser.write(read_sleep_time)  # 执行查询睡眠时间操作
                read_sleep_time_data = tuple(ser.read(20))  # 读取查询睡眠时间
                if not read_sleep_time_data:  # 未接收到数据，继续
                    print("睡眠时间%02d没有收到数据" % addr)
                    refer_sleep_flag_N += 1
                elif read_sleep_time_data[0] == 247 and read_sleep_time_data[1] == 255:
                    print("睡眠时间%02d接收到错误数据" % addr)
                    refer_sleep_flag_N += 1
                else:  # 睡眠时间写入成功
                    cursor.execute("update addrtable set New_Old='O' where addr = '%d'" % addr)  # 睡眠时间写入成功
                    db.commit()
                    print("%02d修改睡眠时间成功。。。。\n-------------"% addr)
                    break  # 退出写入睡眠时间循环
                if refer_sleep_flag_N > 7:
                    # print("设备%d异常，无法接收数据！！！" % addr)
                    print("睡眠时间%02d异常，无法接收数据\n!!!!!!!!!!" % addr)
                    error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sqlinsert_error = "insert into errortable values('%s','%d')" % (error_time, addr)
                    cursor.execute(sqlinsert_error)  # 执行插入数据操作
                    db.commit()
                    print("睡眠时间异常设备%02d写入数据完成\n-----------------------------" % addr)
                    break
    time.sleep(4)  # 每次循环等待时间-s
