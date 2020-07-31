import datetime
import json
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def send_mail(flag, mail):
    now_time = datetime.datetime.now().strftime('%F %T')
    now_date = datetime.datetime.now().strftime('%F')

    if flag == 1:
        msg = MIMEText('登记成功，登记时间：' + now_time, 'plain', 'utf-8')
        msg['Subject'] = Header(now_date + ' 健康日报登记成功', 'utf-8')
    else:
        msg = MIMEText('登记失败，请重新登记', 'plain', 'utf-8')
        msg['Subject'] = Header(now_date + ' 健康日报登记失败', 'utf-8')

    msg['From'] = Header(mail['sender'])
    msg['To'] = Header(mail['receiver'])

    try:
        server = smtplib.SMTP_SSL(mail['smtp_host'])
        server.connect(mail['smtp_host'], 465)
        server.login(mail['sender'], mail['smtp_pwd'])
        server.sendmail(mail['sender'], mail['receiver'], msg.as_string())
        server.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('邮件发送失败')


def login(driver, username, password):
    try:
        url = 'http://iapp.zzuli.edu.cn/portal/portal-app/app-5/user.html'
        driver.get(url)
        locator = (By.ID, 'tx_username')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        driver.find_element_by_id('tx_username').send_keys(username)
        driver.find_element_by_id('tx_password').send_keys(password)
        sleep(1)
        driver.find_element_by_class_name('login_btn').click()

        locator = (By.CLASS_NAME, 'user_name')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        print('登录成功')
        return True
    except TimeoutException:
        print('登录超时，网络问题')
        return False


def register(driver, user):
    if login(driver, user['username'], user['password']) is False:
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
        if user['dormitory_loc'] == 'KX':
            driver.find_element_by_xpath(
                './/li[@role="button" and text()="科学校区"]'
            ).click()
            sleep(0.5)

            driver.find_element_by_xpath(
                './/li[@role="button" and text()="' + user['dormitory_bd'] + '号楼"]'
            ).click()
            sleep(0.5)

        elif user['dormitory_loc'] == 'ZD':
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
        ).send_keys(user['dormitory_num'])
        sleep(0.5)

        # 10 联系电话 11位手机号
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[12]/div[2]/div/div/div/input'
        ).send_keys(user['mobile_phone'])
        sleep(0.5)

        # 10-1 家庭、家长 联系电话
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[13]/div[2]/div/div/div/input'
        ).send_keys(user['home_phone'])
        sleep(0.5)

        # 13 假期是否到过湖北以下地区（默认：无
        driver.find_element_by_xpath(
            'html/body/div/div/div[3]/div[3]/div[20]/div/div[2]/div/div/div/div/div/div[1]'
        ).click()
        sleep(0.5)

        # 14 假期是否到过河南以下地区
        flag = 0
        if user['xinyang'] == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[2]'
            ).click()
            sleep(0.5)
            flag = 1

        if user['nanyang'] == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[3]'
            ).click()
            sleep(0.5)
            flag = 1

        if user['zhumadian'] == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[4]'
            ).click()
            sleep(0.5)
            flag = 1

        if user['shangqiu'] == 1:
            driver.find_element_by_xpath(
                'html/body/div/div/div[3]/div[3]/div[22]/div/div[2]/div/div/div/div/div/div[5]'
            ).click()
            sleep(0.5)
            flag = 1

        if user['zhoukou'] == 1:
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
        ).send_keys(user['other_info'])
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

        locator = (By.XPATH, './/div[@class="div-body"]/p[1]')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        return True

    except TimeoutException:
        print('登记超时，网络问题')
        return False
    except Exception:
        print('登记失败，请核对信息')
        return False


def main():
    with open('user_info.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)
    user = data[0]
    mail = data[1]

    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--headless")

    cnt = 0
    ok = 0
    try:
        while True:
            driver = webdriver.Chrome(chrome_options=options)
            driver.set_page_load_timeout(30)
            cnt += 1
            print('正在进行第', cnt, '次尝试')
            res = register(driver, user)
            driver.quit()

            if res is True:
                print('登记成功，愿疫情早日结束！')
                ok = 1
                break
            elif cnt == 5:
                print('超过尝试次数，请重新登记！')
                break

            sleep(3)

    except Exception:
        print('莫名其妙的错误，请重新登记')
    finally:
        if user['mail_flag'] == 1:
            if ok == 1:
                send_mail(1, mail)
            else:
                send_mail(0, mail)

    os.system('pause')


if __name__ == '__main__':
    main()
    
