import threading
import time


mutex = threading.Lock()


def xc():
    global mutex
    time.sleep(1)
    mutex.acquire(2)  # 取得锁
    print("ok")
    time.sleep(5)
    mutex.release()  # 释放锁



mutex = threading.Lock()  # 创建锁
for i in range(2):
    t = threading.Thread(target=xc)
    t.start()