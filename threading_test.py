import threading
import time
import requests
from multiprocessing import Process, Lock


count = 1


# 请求百度
def res_bd():
    url = 'http://www.baidu.com'
    global count
    res = requests.get(url)
    res_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'第{count}次请求状态码：' + str(res.status_code) + f'    {res_time}')
    count += 1

# -------------------------------多线程并发---------------------------------#

def thread_res():
    for t in iter_num:
        num = int(t) + 1
        print('\n' + '\n' + '-------------------' + f'第{num}次迭代开始' + '-------------------' + '\n')
        for i in threads:
            t = threading.Thread(target=res_bd)
            t.start()
            t.join()
        time.sleep(2)
        print('\n' + '-------------------' + f'第{num}次迭代结束' + '-------------------')


# -------------------------------多进程并发---------------------------------#
def process_res():
    for t in iter_num:
        num = int(t) + 1
        print('\n' + '\n' + '-------------------' + f'第{num}次迭代开始' + '-------------------' + '\n')
        for i in process_num:
            P = Process(target=res_bd)
            P.start()
            P.join()
        time.sleep(2)
        print('\n' + '-------------------' + f'第{num}次迭代结束' + '-------------------')



if __name__ == '__main__':
    while True:
        print('请选择操作：1.多线程并发   2.多进程并发')
        work = int(input())
        if work == 1:
            iter_num = range(int(input('请输入迭代次数：')))
            threads = range(int(input('请输入线程数：')))
            thread_res()
            break
        elif work == 2:
            iter_num = range(int(input('请输入迭代次数：')))
            process_num = range(int(input('请输入进程数：')))
            process_res()
            break
        else:
            print('请输入正确的操作编号  "1"或"2"')
            continue

''' 执行结果如下:

请选择操作：1.多线程并发   2.多进程并发
1
请输入迭代次数：3
请输入线程数：4


-------------------第1次迭代开始-------------------

第1次请求状态码：200    2020-04-18 16:15:37
第2次请求状态码：200    2020-04-18 16:15:37
第3次请求状态码：200    2020-04-18 16:15:38
第4次请求状态码：200    2020-04-18 16:15:38

-------------------第1次迭代结束-------------------


-------------------第2次迭代开始-------------------

第5次请求状态码：200    2020-04-18 16:15:40
第6次请求状态码：200    2020-04-18 16:15:40
第7次请求状态码：200    2020-04-18 16:15:40
第8次请求状态码：200    2020-04-18 16:15:40

-------------------第2次迭代结束-------------------


-------------------第3次迭代开始-------------------

第9次请求状态码：200    2020-04-18 16:15:42
第10次请求状态码：200    2020-04-18 16:15:42
第11次请求状态码：200    2020-04-18 16:15:42
第12次请求状态码：200    2020-04-18 16:15:42

-------------------第3次迭代结束-------------------
'''