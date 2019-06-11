

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import configparser
import time
import sys
import os 
def download(url,song):

    try:
        driver = webdriver.Chrome()
        driver.get(url)
        # 输入歌曲名称
        input = driver.find_element_by_name("query")
        input.send_keys(song)
        # 搜索
        driver.find_element_by_id("button").click()
        float_window = driver.find_element_by_id("suggestions")
        driver.execute_script("document.getElementById('suggestions').setAttribute('style','none')")
        time.sleep(5)
        driver.find_elements_by_class_name("download")[0].click()
        time.sleep(10)
        # driver.find_elements_by_class_name("url")[0].click()
        driver.execute_script("$('.url')[0].click()")
        
        # list_a[0].click()
        time.sleep(10)
        os.system("open ~/Downloads/1.mp3")
        # driver.quit()

    except Exception as e:
        driver.quit()
        print(e)

if __name__ == "__main__":
    
    if len(sys.argv) >1:
        download("https://www.mp3juices.cc/", sys.argv[1])

    else:
        print("please input the song's name")
   