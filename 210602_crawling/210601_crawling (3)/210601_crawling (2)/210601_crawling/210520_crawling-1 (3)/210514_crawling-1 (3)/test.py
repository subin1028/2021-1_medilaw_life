from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

lis_section = []

driver = webdriver.Chrome('chromedriver.exe')
url = "https://www.lawtalk.co.kr/videos"
driver.get(url)
wait = WebDriverWait(driver, 5)
image = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'video-title')))
tip_url = []
video_title = []
video_lawyer = []


vi_title = driver.find_elements_by_class_name('video-title')
for c in vi_title:
    video_title.append(c.text)

vi_lawyer = driver.find_elements_by_class_name('author-lawyer')
for d in vi_lawyer:
    video_lawyer.append(d.text)

for a in range(1, 11):
    path = '//*[@id="root-view"]/div[2]/div[3]/section/div/div[2]/div/section/div[' + str(
            a) + ']/video-card/article/div[2]/p[1]'
    law_btn = driver.find_element_by_xpath(path)
    law_btn.click()
    time.sleep(1)

    back = driver.find_element_by_tag_name('iframe')
    video_link = back.get_attribute('src')
    tip_url.append(video_link)
    driver.back()
    time.sleep(1)


for i in range(0, len(tip_url)-1):
    print(tip_url[i], "\n", video_title[i], "*", video_lawyer[i])