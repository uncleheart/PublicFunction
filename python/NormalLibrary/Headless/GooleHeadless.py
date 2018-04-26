# coding:utf-8
import platform
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import logging


class GoogleHeadless():
    mutex = threading.Lock()

    def __init__(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        mobileEmulation = {'deviceName': 'Pixel 2'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)

        options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 4.4.4; GT-N7100 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI"')

        sysstr = platform.system()
        if (sysstr == "Windows"):
            options.binary_location = r"D:\software\prerequisite\Google\Chrome\Application\chrome.exe"
            chromeDriverPath = r"G:\code\git\PublicFunction\python\files\chromedriver.exe"
            logging.info("widows platform")

        else:
            options.binary_location = "/usr/bin/chromium-browser"
            chromeDriverPath = "/usr/lib/chromium-browser/chromedriver"
            logging.info('other platform')

        self.driver = webdriver.Chrome(chromeDriverPath, chrome_options=options)
        self.driver.set_page_load_timeout(10)

    def getDriver(self):
        return self.driver


"""
[{
    'args':'',
    'jarpath':jarpath,
    },
]
"""
googleHeadless = None


def init(argsSum=None):
    global googleHeadless
    if googleHeadless is None:
        googleHeadless = GoogleHeadless()


def getDriver():
    global googleHeadless
    if googleHeadless is None:
        init()
    googleHeadless.mutex.acquire(10)
    logging.info("get driver")
    return googleHeadless.getDriver()


def releaseDriver():
    if googleHeadless is not None:
        logging.info("releaseDriver")
        googleHeadless.mutex.release()


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui


# 一直等待某元素可见，默认超时10秒
def is_visible(driver, locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


# 一直等待某个元素消失，默认超时10秒
def is_not_visible(driver, locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        EC.te
        return True
    except TimeoutException:
        return False


if __name__ == "__main__":
    init()
    driver = getDriver()
    driver.get(
        "https://login.10086.cn/login.html?channelID=12034&backUrl=http%3A%2F%2Fwww.10086.cn%2Findex%2Fbj%2Findex_100_100.html")
    driver.find_element_by_xpath('//*[@id="sms_nav"]').click()
    driver.find_element_by_xpath('//*[@id="p_phone"]').send_keys('17862701205')
    driver.find_element_by_xpath('//*[@id="getSMSpwd"]').click()

    # 等待验证码弹窗
    ui.WebDriverWait(driver, 5).until(EC.alert_is_present())

    alert = Alert(driver)
    if alert.text == '已将短信随机码发送至手机，请查收!':
        print('ok')
    else:
        print(alert.text)
    print(alert.text)

    is_not_visible('//*[@id="msmsendtips"]')

    errorMsg = driver.find_element_by_xpath('//*[@id="msmsendtips"]').text
    if errorMsg != '':
        print(errorMsg)
    else:
        print('ok')
    driver.find_element_by_xpath('//*[@id="smspwd_err"]').text
    driver.find_element_by_xpath('//*[@id="sms_pwd_l"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="submit_bt"]').click()
    print(driver.find_element_by_xpath('//*[@id="smspwd_err"]').text == '短信随机码不正确或已过期')
