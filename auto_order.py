# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import configparser
import time



#平常是使用configparser.ConfigParser()来读取配置文件，但是当配置文件有特殊字符时就需要另外一个类了configparser.RawConfigParser()

config = configparser.ConfigParser()
config.read('config.ini')
info_list = list(config.items('INFO_LIST'))

config_for_url = configparser.RawConfigParser()
config_for_url.read('config.ini')
url = config_for_url.get('URL','url')
print url
driver = webdriver.Chrome()
driver.get(url)

name_list = ["reserve[number]", "reserve[value_31]", "reserve[value_28][last_name]","reserve[value_28][first_name]","reserve[value_29][number_1]","reserve[value_29][number_2]","reserve[value_29][number_3]"]
policy_id = 'reserve_policy'
confirm_xpatch= '//*[@id="form"]/div[6]/input[2]'
login_xpatch = '/html/body/div/section/div/div[2]/div[2]/form/div[3]/input[2]'

def auto_order():

    try:
        
        for i in xrange(0,7):
            dom_name = name_list[i]
            content_name = info_list[i][1]

            content_name = content_name.replace('\'','')
            if i == 0:
                select_item = Select(driver.find_element_by_name(dom_name))
                select_item.select_by_index(content_name)
            
            seletem_item = driver.find_element_by_name(dom_name)
            seletem_item.send_keys(content_name) 
        # 勾选
        driver.find_element_by_id(policy_id).click()
        time.sleep(4)
        # 确认
        driver.find_element_by_xpath(confirm_xpatch).click()

        # login 
        # driver.find_element_by_xpath(login_xpatch).click()
    except Exception as e:
        print e

if __name__ == "__main__":
    auto_order()
    time.sleep(35)
    driver.quit()