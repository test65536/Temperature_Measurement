import time
import pymysql
from functools import reduce
# lowest common multiple-LCM 最小公倍数
# 函数lcm_seq功能：求多个数的最小公倍数


def lcm_seq(seq):  # 求多个数的最小公倍
    def gcd(a, b):  # 求两个数的最大公约数
        r = a % b
        if r:
            return gcd(b, r)
        else:
            return b

    def lcm(a, b):  # 求两个数的最小公倍数
        return a * b / gcd(a, b)
    return reduce(lcm, seq)


conn = pymysql.connect(host="10.0.0.111", user="root", passwd="zong123", db="test")
cursor = conn.cursor()

cursor.execute("select * from addrtable")   # 查询数据
time_addr_table = cursor.fetchall()

cursor.execute("select time from addrtable")   # 查询睡眠时间数据
conn.commit()
data_time_col = cursor.fetchall()   # 获取查询的睡眠时间数据
sleep_time_list = []  # 初始化睡眠时间列表
for data_time_col_1 in data_time_col:  # 提取出双重元组的睡眠时间
    sleep_time_list.append(data_time_col_1[0])   # 追加元素到睡眠时间列表
print("最小公倍数：", int(lcm_seq(sleep_time_list)))

time_start = int(time.time())  # 开始时间，向下取整
# 每秒查询是否有设备睡眠时间到了
while True:
    time_up_addr = []  # 初始化时间到了的地址列表
    time_end = int(time.time())+1  # 防止出现delta_time=0导致第一次就发数据
    delta_time = time_end - time_start  # 间隔时间
    print("---------------", delta_time)
    for k in range(0, len(time_addr_table)):  # 遍历所有睡眠时间
        if delta_time % time_addr_table[k][0] == 0:  # 时间间隔% 睡眠时间 ==0 取出地址加入地址列表
            print('设备[%02d] time is up, 请给设备[%02d]发消息' % (time_addr_table[k][1], time_addr_table[k][1]))
            print('------------------------------------------')
            time_up_addr.append(time_addr_table[k][1])  # 取出睡眠时间到了的设备地址加入地址列表
            print(time_up_addr)  # 打印取出的地址列表
    if delta_time == int(lcm_seq(sleep_time_list)):  # 计时超出最小公倍数，重新开始计算时间
        print("超出最大时间了，请重新计算时间!")
        time_start = time_end  # 重新计算时间
    time.sleep(1)
    for tua in time_up_addr:  # 遍历睡眠时间到了的设备地址
        print(tua)
        cursor.execute("select * from addrtable where addr = %d" % tua)  # 查询改地址行记录
        conn.commit()
        select_addr_data = cursor.fetchall()
        print(select_addr_data)

