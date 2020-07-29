import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep


# 用户名（学号）
username = '541713460000'

# 密码（信息门户密码）
password = 'xxxxxxxx'

# 校区，科学：'KX'  走读：'ZD'
dormitory_loc = 'KX'

# 宿舍楼号，如 3 号楼填写 '3'
dormitory_buildin = '3'

# 宿舍号
dormitory_number = '615'

# 联系电话 11位手机
mobile_phone = '15600000000'

# 家庭电话
home_phone = '13200000000'

# 是否到过河南以下地区，到过则修改为 1
xinyang = 0
nanyang = 0
zhumadian = 0
shangqiu = 0
zhoukou = 0

# 其他需要说明的情况
other_info = '无'


def login(driver):
    url = 'http://iapp.zzuli.edu.cn/portal/portal-app/app-5/user.html'
    driver.get(url)

    try:
        locator = (By.ID, 'tx_username')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))

        driver.find_element_by_id('tx_username').send_keys(username)
        driver.find_element_by_id('tx_password').send_keys(password)
        sleep(1)
        driver.find_element_by_class_name('login_btn').click()
        sleep(1)
        print('登录成功，开始登记')

    except TimeoutException:
        print('登录超时，网络问题')
        return False

    return True


def register(driver):
    auth = login(driver)
    if auth is False:
        return False

    try:
        main_url = 'http://microapp.zzuli.edu.cn/microapplication/yqfk_qy/home.html'
        driver.get(main_url)

        locator = (By.XPATH, './/div[@class="content"]/div[1]/a')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))

        driver.find_element_by_xpath('.//div[@class="content"]/div[1]/a').send_keys(Keys.ENTER)

        locator = (By.XPATH, 'html/body/div/div/div[3]/div[3]/div[10]/div[2]/div/div/div/input')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))

        # 修改地址获取方式为 h5
        driver.execute_script('now_from="h5"')
        sleep(0.5)

        # 9 在校居住宿舍楼
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[10]/div[2]/div/div/div/input'
        ).click()
        sleep(0.5)

        # 选择宿舍楼
        if dormitory_loc == 'KX':
            driver.find_element_by_xpath(
                './/li[@role="button" and text()="科学校区"]'
            ).click()
            sleep(0.5)

            driver.find_element_by_xpath(
                './/li[@role="button" and text()="' + dormitory_buildin + '号楼"]'
            ).click()
            sleep(0.5)

        elif dormitory_loc == 'ZD':
            driver.find_element_by_xpath(
                './/li[@role="button" and text()="校外走读"]'
            ).click()
            sleep(0.5)

        # 确定宿舍楼信息
        driver.find_element_by_xpath(
            './/div[@class="van-picker"]/div/button[2]'
        ).click()
        sleep(0.5)

        # 9-1 在校居住宿舍号
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[11]/div/div[2]/div/div/div/input'
        ).send_keys(dormitory_number)
        sleep(0.5)

        # 10 联系电话 11位手机号
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[12]/div[2]/div/div/div/input'
        ).send_keys(mobile_phone)
        sleep(0.5)

        # 10-1 家庭、家长 联系电话
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[13]/div[2]/div/div/div/input'
        ).send_keys(home_phone)
        sleep(0.5)

        # 13 假期是否到过湖北以下地区（默认：无
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[20]/div/div[2]/div/div/div/div/div/div[1]'
        ).click()
        sleep(0.5)

        # 14 假期是否到过河南以下地区
        flag = 0
        if xinyang == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[2]'
            ).click()
            sleep(0.5)
            flag = 1

        if nanyang == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[3]'
            ).click()
            sleep(0.5)
            flag = 1

        if zhumadian == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[4]'
            ).click()
            sleep(0.5)
            flag = 1

        if shangqiu == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[5]'
            ).click()
            sleep(0.5)
            flag = 1

        if zhoukou == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[6]'
            ).click()
            sleep(0.5)
            flag = 1

        if flag == 0:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[1]'
            ).click()
            sleep(0.5)

        # 15 目前您的位置和居住地点（由浏览器自动获取
        try:
            locator = (By.XPATH, 'html/body/div/div/div[3]/div[5]/div/div[2]/div/div/div/textarea')
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[5]/div/div[2]//div/div/div/textarea'
            ).click()
            WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element_value(locator, ''))

        except TimeoutException:
            print('地址获取超时')
            return False

        sleep(0.5)

        # 15-1 你获取的位置与本人目前所在地是否相符合（默认：是
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[5]/div[2]/div[2]/div/div[2]'
        ).click()
        sleep(0.5)

        # 15-3 您所在的小区是否有确诊病例（默认：无
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[6]/div/div[2]/div/div[1]'
        ).click()
        sleep(0.5)

        # 17 您今日有无以下症状（默认：无
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[10]/div[2]/div/div/div/div/div/div[1]'
        ).click()
        sleep(0.5)

        # 18 今日同住人员身体状况（默认：无症状
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[12]/div[2]/div/div/div[1]'
        ).click()
        sleep(0.5)

        # 18-2 您是否与疫区人员有过接触（默认：否
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[14]/div/div[2]/div/div[1]'
        ).click()
        sleep(0.5)

        # 20-5 您是否曾经被诊断为确诊病例（默认：否
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[21]/div/div[2]/div/div[1]'
        ).click()
        sleep(0.5)

        # 21 其他需要说明的情况
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[26]/div[2]/div/div/div/textarea'
        ).send_keys(other_info)
        sleep(0.5)

        # 点击提交
        driver.find_element_by_xpath(
            './/div[@class="submit-div"]/button'
        ).click()
        sleep(0.5)

        # 确认提交
        driver.find_element_by_xpath(
            './/div[@class="van-dialog"]/div[3]/button[2]'
        ).click()
        sleep(0.5)

    except TimeoutException:
        print('登记超时，网络问题')
        return False

    except Exception as e:
        print(e)
        print('登记失败，请检查信息')
        return False

    return True


def main():
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    cnt = 0
    while True:
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_page_load_timeout(30)
        cnt += 1
        print('正在进行第', cnt, '次尝试')
        res = register(driver)

        if res is True:
            print('登记成功，愿疫情早日结束！')
            break
        elif cnt == 5:
            print('超过尝试次数，请重新登记！')
            break

        driver.quit()
        sleep(5)

    os.system('pause')


if __name__ == "__main__":
    main()