# 변호사탭 누르고 새 페이지에서 상세 내용 불러오기


from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

law_image = []

driver = webdriver.Chrome('chromedriver.exe')
url = "https://www.lawtalk.co.kr/lawyers?keyword=%EC%9D%98%EB%A3%8C"
driver.get(url)

image_real = driver.find_elements_by_class_name("lawyer-profile")  # 변호사 이미지
for image in image_real:
    src = image.get_attribute('src')  # 이미지 src요소 분리
    law_image.append(src)

law_btn = driver.find_elements_by_class_name('lawyer-name')  #버튼 요소 모으기
lawyer_name = []
lawyer_company = []
lawyer_phone = []
lawyer_address =[]
lawyer_part = []
lawyer_produce = []
count = 1
for i in law_btn:
    i.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])  # 클릭해서 열린페이지로 이동
    driver.implicitly_wait(5)
    time.sleep(1)
    con = driver.find_element_by_xpath('//*[@id="root-view"]/div/div/div/div[1]/div[3]/div[2]/div/section[1]').text
    back_law = con.split('\n')
    if back_law[2].endswith('개') != True:
        lawyer_produce.append(back_law[0])
        lawyer_name.append(back_law[1])
        lawyer_company.append(back_law[2])
        lawyer_address.append(back_law[3])
        lawyer_phone.append(back_law[4])
        lawyer_part.append(back_law[6])

    else:
        lawyer_produce.append(back_law[0])
        lawyer_name.append(back_law[1])
        lawyer_company.append(back_law[3])
        lawyer_address.append(back_law[4])
        lawyer_phone.append(back_law[5])
        lawyer_part.append(back_law[7])


    print(count)
    count += 1
    # print(back_law)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # 로딩 기다리기
    time.sleep(0.5)


for i in range(0, len(law_btn)-1):
    print(law_image[i])
    print(lawyer_produce[i], '*', lawyer_name[i], "*", lawyer_company[i], "*", lawyer_address[i], "*", lawyer_phone[i], "*", lawyer_part[i], "\n")
