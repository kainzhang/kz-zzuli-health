from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# 用户名
username = ''
# 密码
password = ''
# 宿舍号
dormitory_number = ''
# 联系电话 11位手机
mobile_phone = ''
# 家庭电话
home_phone = ''
# 需要说明的情况
other_info = '无'

url = 'http://iapp.zzuli.edu.cn/portal/portal-app/app-5/user.html'
mobile_emulation = {'deviceName':'iPhone 6'}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

try:
    driver.find_element_by_id('tx_username').send_keys(username)
    driver.find_element_by_id('tx_password').send_keys(password)
    sleep(1)
    driver.find_element_by_class_name('login_btn').click()
    sleep(2)
    driver.refresh()
    print('登录成功')
    try:
        driver.get('http://microapp.zzuli.edu.cn/microapplication/yqfk_qy/home.html')
        sleep(1)
        driver.find_element_by_xpath(".//div[@class='content']/div[1]/a").send_keys(Keys.ENTER)
        sleep(1)
        driver.execute_script("now_from='h5'")
        sleep(1)

        # 9 在校居住宿舍楼
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[10]/div[2]/div/div/div/input'
        ).click()
        sleep(1)

        # 选择校区
        driver.find_element_by_xpath(
            './/li[@role="button" and text()="科学校区"]'
        ).click()
        sleep(1)

        # 选择宿舍楼
        driver.find_element_by_xpath(
            './/li[@role="button" and text()="3号楼"]'
        ).click()
        sleep(1)

        # 确定宿舍
        driver.find_element_by_xpath(
            './/div[@class="van-picker"]/div/button[2]'
        ).click()
        sleep(1)

        # 9-1 在校居住宿舍号
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[11]/div/div[2]/div/div/div/input'
        ).send_keys(dormitory_number)
        sleep(1)

        # 10 联系电话 11位手机号
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[12]/div[2]/div/div/div/input'
        ).send_keys(mobile_phone)
        sleep(1)

        # 10-1 家庭、家长 联系电话
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[13]/div[2]/div/div/div/input'
        ).send_keys(home_phone)
        sleep(1)

        # 13 假期是否到过湖北以下地区
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[20]/div/div[2]/div/div/div/div/div/div'
        ).click()
        sleep(1)

        # 14 假期是否到过河南以下地区
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div'
        ).click()
        sleep(1)

        # 15 目前您的位置和居住地点
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[5]/div/div[2]/div/div/div/textarea'
        ).click()
        sleep(2)

        # 15-1 你获取的位置与本人目前所在地是否相符合
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[5]/div[2]/div[2]/div/div[2]'
        ).click()
        sleep(1)

        # 15-3 您所在的小区是否有确诊病例
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[6]/div/div[2]/div/div[1]'
        ).click()
        sleep(1)

        # 17 您今日有无以下症状
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[10]/div[2]/div/div/div/div/div/div[1]'
        ).click()
        sleep(1)

        # 18 今日同住人员身体状况
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[12]/div[2]/div/div/div[1]'
        ).click()
        sleep(1)

        # 18-2 您是否与疫区人员有过接触
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[14]/div/div[2]/div/div[1]'
        ).click()
        sleep(1)

        # 20-5 您是否曾经被诊断为确诊病例
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[21]/div/div[2]/div/div[1]'
        ).click()
        sleep(1)

        # 21 其他需要说明的情况
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[26]/div[2]/div/div/div/textarea'
        ).send_keys(other_info)
        sleep(1)

        # 点击提交
        driver.find_element_by_xpath(
            './/div[@class="submit-div"]/button'
        ).click()
        sleep(1)

        # 确认提交
        driver.find_element_by_xpath(
            './/div[@class="van-dialog"]/div[3]/button[2]'
        ).click()
        sleep(1)

        print('操作成功')
        driver.quit()
    except:
        print('操作失败')

except:
    print('登录失败')

