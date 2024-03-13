import urllib.request
import sys
import MainCode

from urllib.request import urlopen  # 웹드라이버에서 유알엘 오픈
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QApplication, QGraphicsObject
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal, QThread, QUrl
import time
import random


form_class = MainCode.Ui_zx

class OptionWindow(QDialog):

    def __init__(self, parent):
            super(OptionWindow, self).__init__(parent)
            option_ui = 'Popup.ui'
            uic.loadUi(option_ui, self)
            self.show()

class MyWindow(QMainWindow, MainCode.Ui_zx):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lawyer_sample()

        self.btn1.clicked.connect(self.tip_exec) #판례에서 법률팁 가져오기
        self.btn1.clicked.connect(self.content_combo_search) #콤보박스 이용한 검색
        self.pushButton_16.clicked.connect(self.lawyer_search) #변호사 검색
        self.pushButton_4.clicked.connect(self.video_search) #유튜브 영상 가져오기
        self.pushButton_0.clicked.connect(self.content_search) #검색창으로 판례 검색
        self.pushButton_0.clicked.connect(self.tip_exec) #검색창 검색 시 법률팁 가져오기
        self.setWindowIcon(QtGui.QIcon('background.png')) #배경색 깔기

    def lawyer_sample(self): #변호사 검색
        #추천 변호사 리스트
        lawyer = [['https://www.lawtalk.co.kr//uploads/original/5f881865cb260001e2375768-original.jpg',
                   '노동/인사, 명예훼손/모욕, 성범죄', 'https://www.lawtalk.co.kr/directory/profile/7308-%EC%9D%B4%EC%B2%A0%ED%9D%AC?pg=main.lawyers&source=search-lawyers-all_p&position=19&sc=category&sca=%EB%AA%85%EC%98%88%ED%9B%BC%EC%86%90~2F%EB%AA%A8%EC%9A%95'],
                  ['https://www.lawtalk.co.kr//uploads/original/607058cc1615b100738d17fd-original.jpg',
                   '의료, 노동/인사, 손해배상, 보험', 'https://www.lawtalk.co.kr/directory/profile/5056-%EC%B1%84%EC%83%81%EA%B5%AD?pg=main.lawyers&source=search-lawyers-all_p&position=13&sc=category&sca=%EC%9D%98%EB%A3%8C'],
                  ['https://www.lawtalk.co.kr//uploads/original/5c66037ebb38fe09bee50c8f-original.jpg',
                   '명예훼손/모욕, 폭행/협박, 노동/인사', 'https://www.lawtalk.co.kr/directory/profile/2555-%EC%A7%84%EB%B3%B4%EB%9D%BC?pg=main.lawyers&source=search-lawyers-all_p&position=84&sc=keyword&sca=%ED%8F%AD%ED%96%89~2F%ED%98%91%EB%B0%95'],
                  ['https://www.lawtalk.co.kr//uploads/original/5f2e26d069e950024229076e-original.jpg', '성범죄, 재산범죄', 'https://www.lawtalk.co.kr/directory/profile/8047-%EC%9D%B4%EC%82%BC%EC%9C%A4?pg=main.lawyers&source=search-lawyers-all_p&position=29&sc=category&sca=%EC%84%B1%EB%B2%94%EC%A3%84'],
                  ['https://www.lawtalk.co.kr//uploads/original/5e67385e9f847c027128e519-original.jpg',
                   '재산범죄, 형사기타, 계약일반', 'https://www.lawtalk.co.kr/directory/profile/9410-%EC%9D%B4%EC%B2%AD%EC%95%84?pg=main.lawyers&source=search-lawyers-all_p&position=47&sc=keyword&sca=%EC%9E%AC%EC%82%B0%EB%B2%94%EC%A3%84']]

        sel_num = [] #랜덤값 뽑아서 넣을 리스트
        while len(sel_num) < 3: # 중복 숫자 없이 랜덤값 뽑기
            num = random.randint(0, 4)
            if num not in sel_num:  # 새로운 수가 중복이 아니면,
                sel_num.append(num)  # 리스트에 추가

        img_num = 10 #이미지 띄우는 레이블값
        link_num = 105 #링크 연결하는 레이블값
        for i in range(0, 3):
            def ImageLoad(self): #변호사 이미지 레이블에 넣는 함수
                Image_src = lawyer[sel_num[i]][0] #추천 변호사 리스트 중 뽑힌 랜덤값 자리 이미지
                imageWeb = urllib.request.urlopen(Image_src).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaled(91, 81) #사진 값 조정
                imload = "self.label_" + str(img_num) + ".setPixmap(self.qPixmapWebVar)" #사진 넣는 명령어
                exe_link = "self.url" + str(i + 1) + "= lawyer[sel_num[i]][2]" #url 넣는 명령어
                exec(exe_link) #명령어 실행
                exec(imload) #명령어 실행
            ImageLoad(self) #이미지 넣는 함수 실행
            img_num += 1 #레이블 이름 값 변경
            link_num += 1 #레이블 이름 값 변경

        part_num = 55 #분야 연결 레이블값
        for i in range(0, 3):
            tb_t = "self.textBrowser_" + str(part_num) + ".setText(lawyer[sel_num[" + str(i) + "]][1])" #분야 넣는 명령어
            exec(tb_t) # 명령어 실행
            part_num += 1 #레이블 이름 값 변경

    def lawyer_search(self): #변호사 검색 함수
        driver = webdriver.Chrome('chromedriver.exe')
        search = self.textEdit_22.toPlainText() #검색창 글씨 변수
        url = "https://www.lawtalk.co.kr/lawyers?keyword=" + search #url 생성
        law_image = [] #이미지 넣을 리스트
        driver.get(url)

        image_real = driver.find_elements_by_class_name("lawyer-profile")  # 변호사 이미지 요소 찾기
        for image in image_real:
            src = image.get_attribute('src')  # 이미지 src요소 분리
            law_image.append(src) #이미지 리스트에 넣기

        law_btn = driver.find_elements_by_class_name('lawyer-name')  # 버튼 요소 모으기
        lawyer_name = [] #변호사 이름 리스트
        lawyer_company = [] #회사명 리스트
        lawyer_phone = [] #전화번호 리스트
        lawyer_address = [] #주소 리스트
        lawyer_produce = [] #한줄소개 리스트
        count = 1
        for i in law_btn:
            i.click() #버튼 요소 클릭
            time.sleep(1) #페이지 대기
            driver.switch_to.window(driver.window_handles[-1])  # 클릭해서 열린페이지로 이동
            driver.implicitly_wait(5) #페이지 대기
            time.sleep(1)
            con = driver.find_element_by_xpath(
                '//*[@id="root-view"]/div/div/div/div[1]/div[3]/div[2]/div/section[1]').text #변호사 정보 가져오기
            back_law = con.split('\n') #정보 분리하기
            if back_law[2].endswith('개') != True: #특정 정보 들어있다면
                lawyer_produce.append(back_law[0]) #한줄소개 넣기
                lawyer_name.append(back_law[1]) #이름 넣기
                lawyer_company.append('- ' + back_law[2]) #회사명 넣기
                lawyer_address.append('- ' + back_law[3]) #주소 넣기
                lawyer_phone.append(back_law[4]) #전화번호 넣기

            else: #특정 정보가 들어있지 않다면
                lawyer_produce.append(back_law[0]) #한줄소개 넣기
                lawyer_name.append(back_law[1]) #이름 넣기
                lawyer_company.append('- ' + back_law[3]) #회사명 넣기
                lawyer_address.append('- ' + back_law[4]) #주소 넣기
                lawyer_phone.append(back_law[5]) #전화번호 넣기

            print(count)
            if count == 12: #변호사 정보 12개 가져오면
                break #멈추기
            count += 1 #가져온 정보 수 세기
            driver.close() #열린 창 닫고
            driver.switch_to.window(driver.window_handles[0]) #열리기 전 창으로 넘어가기
            time.sleep(0.5) #로딩 기다리기

        name_num = 25 #이름 레이블 값
        produce_num = 22 #한줄소개 텍스트브라우저 값
        company_num = 37 #회사명 레이블 값
        address_num = 34 #주소 텍스트브라우저 값
        phone_num = 49 #전화번호 레이블 값
        for i in range(0, 12):
            tb_n = "self.label_" + str(name_num) + ".setText(lawyer_name[" + str(i) + "])" #이름 넣는 명령어
            tb_p = "self.textBrowser_" + str(produce_num) + ".setText(lawyer_produce[" + str(i) + "])" #한줄소개 명령어
            tb_c = "self.label_" + str(company_num) + ".setText(lawyer_company[" + str(i) + "])" #회사명 명령어
            tb_a = "self.textBrowser_" + str(address_num) + ".setText(lawyer_address[" + str(i) + "])" #주소 명령어
            tb_t = "self.label_" + str(phone_num) + ".setText(lawyer_phone[" + str(i) + "])" #전화번호 명령어
            exec(tb_n) #명령어 실행
            exec(tb_p)
            exec(tb_c)
            exec(tb_a)
            exec(tb_t)
            name_num += 1 #레이블, 텍스트브라우저 값 변경
            produce_num += 1
            company_num += 1
            address_num += 1
            phone_num += 1

        img_num = 13 #사진 넣을 레이블 값
        for b in range(0, 12):
            def ImageLoad(self): #이미지 불러오는 함수
                Image_src = law_image[b] #리스트에 있는 이미지 불러오기
                imageWeb = urllib.request.urlopen(Image_src).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaled(151, 131) #사진 사이즈 조정
                imload = "self.label_" + str(img_num) + ".setPixmap(self.qPixmapWebVar)" #이미지 넣는 명령어
                exec(imload) #명령어 실행
            ImageLoad(self) #이미지 불러오는 함수 실행
            img_num += 1 #레이블 값 변경

    def video_search(self):
        driver = webdriver.Chrome('chromedriver.exe')
        video_search = self.textEdit_23.toPlainText() #검색창 값 변수
        url = 'https://www.youtube.com/results?search_query=' + video_search #url 생성
        driver.get(url)
        page = driver.page_source
        soup = bs(page, 'html.parser') #불러온 페이지 소스 연결

        ytb_title = [] #영상 제목 리스트
        ytb_channel = [] #영상 게시자 리스트
        ytb_link = [] #영상 링크 리스트

        title = driver.find_elements_by_xpath('//*[@id="video-title"]') #영상 제목 불러오기
        for a in title:
            ytb_title.append(a.text) #리스트에 넣기

        channel = soup.find_all('a', 'yt-simple-endpoint style-scope yt-formatted-string') #채널명 불러오기
        for b in channel:
            ytb_channel.append(b.text) #리스트에 넣기

        link_back = driver.find_elements_by_id('video-title') #링크 전체 불러오기
        for i in link_back:
            ylink = i.get_attribute('href') #href요소 분리
            temp = ylink.split('=') #링크 중 필요없는 값 분리
            real_link = "https://www.youtube.com/embed/" + temp[-1] #영상 바로 보이게 링크 생성
            ytb_link.append(real_link) #링크 리스트에 넣기
            time.sleep(0.5) #페이지 대기

        ytb_num = 1 #영상 넣을 레이블 값
        for i in range(0, 9):
            vi_tb = "self.webview_" + str(ytb_num) + ".setUrl(QUrl(\"" + str(ytb_link[i]) + "\"))" #영상 넣는 명령어
            exec(vi_tb) #명령어 실행
            ytb_num += 1 #레이블 값 변경

        v_num_t = 46 #영상 제목 레이블 값
        v_num_l = 61 #영상 게시자 레이블 값
        for i in range(0, 9):
            v_tb_t = "self.textBrowser_" + str(v_num_t) + ".setText(ytb_title[" + str(i) + "])" #제목 넣는 명령어
            v_tb_l = "self.label_" + str(v_num_l) + ".setText(ytb_channel[" + str(i) + "])" #채널 넣는 명령어
            exec(v_tb_t) #제목 명령어 실행
            exec(v_tb_l) #채널 명령어 실행
            v_num_t += 1 #텍스트 브라우저 값 변경
            v_num_l += 1 #레이블 값 변경

        print(ytb_link, '\n', ytb_title, '\n', ytb_channel) #리스트가 잘 정리됐는지 확인

        self.label_80.setText("출처: YouTube") #검색창 검색 시 출처 변경

    def content_search(self): #판례 검색창 검색
        Site = self.cb3.currentText() #검색창 값 변수
        search_result = "\"" + Site + "\" 에 \"" + self.textEdit.toPlainText() + "\" 을(를) 검색한 결과" #출처 표시
        self.label_2.setText(search_result) #출처 레이블에 넣기

        if (Site == "로시컴"): #사이트가 로시컴일 경우
            driver = webdriver.Chrome('chromedriver.exe')
            search = quote(self.textEdit.toPlainText()) #검색창 값 url형식으로 변경
            url = "http://www.lawsee.com/auction/list?search_grade=&search_field=&search_field2=&search_expert=&search_orderby=1&search_word=" + search
            #url 생성
            driver.get(url)
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            lis_title = [] # 판례 제목 리스트
            lis_content = [] #사례 내용 리스트
            lis_link = [] #링크 리스트
            lis_answer = [] #답변 리스트
            title = soup.find_all('h2', {'class': 'h1'})  # 제목 크롤링
            answer = soup.find_all('p', {'class': 't1 t-dot'})  # 답변 크롤링
            for n in title:
                if "										" in n.get_text(): #제목에 빈칸이 있으면
                    n = n.get_text().replace("										", "")  # 빈칸 없애는 작업
                    temp = n.split("\n")  # 내용을 엔터 기준으로 나눴을 때, 제목이 보통 temp[5]나 temp[6]에 들어가있음
                    if len(temp[5]) > 5:  # 제목을 제외하고 가장 긴 길이의 요소가 5글자여서 temp[5]가 5글자보다 길면 temp[5]를 리스트에 집어넣음
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

                elif "	" in n.get_text():  # 위와 마찬가지
                    n = n.get_text().replace("	", "")
                    temp = n.split("\n")
                    if len(temp[5]) > 5:
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

                else:
                    temp = n.split("\n")  # 위와 마찬가지
                    if len(temp[5]) > 5:
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

            for i in answer:  # 답변 가져오는 반복문
                if "										" in i.get_text():
                    i = i.get_text().replace("										", "")
                    lis_answer.append(i)

            for links in soup.find_all('h2', {'class': 'h1'}):  # 사례 내용 있는 링크 모아주기
                for a in links.select("a[href^='/auction/counsel/view']"):
                    lis_link.append("http://www.lawsee.com/" + a.get('href'))

            for b in lis_link:  # html 링크 내에 사례 가져오는 반복문
                link_url = b
                link_html = urllib.request.urlopen(link_url).read()
                soup_1 = BeautifulSoup(link_html, 'html.parser')
                real_con = soup_1.select_one("div.bbsN_cbox p").get_text()
                lis_content.append(real_con) #사례 내용 리스트에 넣기


            if len(lis_title) <= 3: #리스트 요소가 3개 미만이라면
                self.onButtonClicked() #알림창 띄우기

            else: #3개 이상이면
                content_num = 1 #텍브 값
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])" #제목 넣는 명령어
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])" #내용 넣는 명령어
                    print(tb_t)
                    exec(tb_t) #명령어 실행
                    print(tb_c)
                    exec(tb_c) #명령어 실행
                    content_num += 1 #텍브 값 변경

        elif (Site == "LAW TALK"): #사이트가 로톡이라면
            search = self.textEdit.toPlainText() #위와 동일
            driver = webdriver.Chrome('chromedriver.exe')
            search = quote(search)
            url = "https://www.lawtalk.co.kr/cases?pg=1&sort=recentAnswer&keyword=" + search
            driver.get(url)
            lis_title = [] #제목 넣을 리스트
            lis_content = [] #사례 내용 리스트
            wait = WebDriverWait(driver, 5)
            image = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'case-card__title'))) #클래스 이름이 나올 때까지 대기

            for a in range(1, 11):
                path = '//*[@id="root-view"]/div[2]/div[3]/section/div/div[4]/div/section/case-card[' + str(
                    a) + ']/a' #링크 xpath 만들기
                law_btn = driver.find_element_by_xpath(path) #path로 이동
                law_btn.click() #버튼 클릭
                time.sleep(1) #페이지 로딩 대기
                driver.switch_to.window(driver.window_handles[-1])  # 클릭해서 열린페이지로 이동
                driver.implicitly_wait(5)
                time.sleep(1)
                title = driver.find_element_by_xpath('//*[@id="root-view"]/div/div/div/question/div/h1').text #제목 크롤링
                con = driver.find_element_by_xpath(
                    '//*[@id="root-view"]/div/div/div/question/div/p').text #내용 크롤링

                lis_title.append(title) #제목 리스트에 넣기
                lis_content.append(con) #내용 리스트에 넣기
                driver.back() #전 페이지로 되돌아가기
                # 로딩 기다리기
                time.sleep(0.5)

            if len(lis_title) <= 3: #리스트 요소가 3개 미만이면
                self.onButtonClicked() #알림창 띄우기

            else: #로시컴과 동일
                content_num = 1
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])"
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])"
                    print(tb_t)
                    exec(tb_t)
                    print(tb_c)
                    exec(tb_c)
                    content_num += 1

        elif (Site == "대한민국 법원 종합법률정보"): #사이트가 법률정보일 경우
            lis_title = [] #제목 리스트
            lis_content = [] #내용 리스트
            search = self.textEdit.toPlainText()
            driver = webdriver.Chrome('chromedriver')
            link = 'https://glaw.scourt.go.kr/wsjo/panre/sjo050.do'
            driver.get('https://glaw.scourt.go.kr/wsjo/panre/sjo050.do')  # 판례검색 사이트 접속

            time.sleep(0.5)

            driver.find_element_by_xpath('//*[@id="search"]/div[2]/fieldset/input').send_keys(search)  # 키워드 입력 'search'
            driver.find_element_by_xpath('//*[@id="srch_img"]').click()  # 검색버튼 클릭

            time.sleep(0.5)

            for i in range(0, 20):  # 판례 내용 읽기
                v = str(i)
                subpage = driver.page_source
                soup = bs(subpage, 'html.parser')  # html 파싱
                driver.implicitly_wait(30)  # 기다려주기

            title = soup.select('td:nth-child(2) > dl > dt > a:nth-child(1)')  # 제목 - bs 셀렉터
            for tit in title:
                lis_title.append(tit.text) #리스트에 추가

            content = soup.select('td:nth-child(2) > dl > dd:nth-child(3)')  # 내용 - bs 셀렉터
            for con in content:
                lis_content.append(con.text) #리스트에 추가

            if len(lis_title) <= 3: #리스트 요소가 3개 미만이면
                self.onButtonClicked() #알림창

            else: #로시컴과 동일
                content_num = 1
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])"
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])"
                    print(tb_t)
                    exec(tb_t)
                    print(tb_c)
                    exec(tb_c)
                    content_num += 1

    def tip_exec(self):
        # 법률TIP
        driver = webdriver.Chrome('chromedriver.exe')
        url = "https://www.lawtalk.co.kr/videos" #법률TIP 사이트
        driver.get(url)
        wait = WebDriverWait(driver, 5) #페이지 대기
        image = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'video-title'))) #찾는 클래스 이름 나올 때까지 대기
        tip_url = [] #링크 리스트
        video_title = [] #제목 리스트
        video_lawyer = [] #변호사 이름 리스트

        vi_title = driver.find_elements_by_class_name('video-title') #제목 가져오기
        for c in vi_title:
            video_title.append(c.text) #텍스트만 리스트에 추가

        vi_lawyer = driver.find_elements_by_class_name('author-lawyer') #변호사 가져오기
        for d in vi_lawyer:
            video_lawyer.append(d.text) #텍스트만 리스트에 추가

        for a in range(1, 11):
            path = '//*[@id="root-view"]/div[2]/div[3]/section/div/div[2]/div/section/div[' + str(
                a) + ']/video-card/article/div[2]/p[1]' #들어갈 xpath 만들기
            law_btn = driver.find_element_by_xpath(path) #xpath요소 찾기
            law_btn.click() #클릭
            time.sleep(1) #대기하기

            back = driver.find_element_by_tag_name('iframe') #iframe 찾기
            video_link = back.get_attribute('src') #src 분리
            tip_url.append(video_link) #링크 리스트 추가
            driver.back() #그 전 창으로 이동
            time.sleep(1) #페이지 로딩 대기

        num = 1 #영상 넣을 자리 값
        for i in range(0, 9):
            tb = "self.webview_" + str(num) + ".setUrl(QUrl(\"" + str(tip_url[i]) + "\"))" #영상 넣는 명령어
            print(tb)
            exec(tb) #명령어 실행
            num += 1 #값 변경

        v_num_t = 46 #영상 제목 텍브 값
        v_num_l = 61 #변호사 레이블 값
        for i in range(0, 9):
            v_tb_t = "self.textBrowser_" + str(v_num_t) + ".setText(video_title[" + str(i) + "])" #제목 넣는 명령어
            v_tb_l = "self.label_" + str(v_num_l) + ".setText(video_lawyer[" + str(i) + "])" #변호사 넣는 명령어
            print(v_tb_t)
            exec(v_tb_t) #명령어 실행
            print(v_tb_l)
            exec(v_tb_l) #명령어 실행
            v_num_t += 1 #값 변경
            v_num_l += 1 #값 변경

    def content_combo_search(self): #판례 콤보박스 검색
        Site = self.cb3.currentText() #콤보박스 선택값을 사이트로 지정
        search_result = "\"" + Site + "\" 에 \"" + self.cb1.currentText() + " " + self.cb2.currentText() + "\" 을(를) 검색한 결과"
        self.label_2.setText(search_result)
        if (Site == "로시컴"): #검색창 검색 시 크롤링 방식과 동일

            url_query = quote(self.cb1.currentText() + " " + self.cb2.currentText())
            driver = webdriver.Chrome('chromedriver.exe')
            url = "http://www.lawsee.com/auction/list?search_grade=&search_field=&search_field2=&search_expert=&search_orderby=1&search_word=" + url_query
            html = urllib.request.urlopen(url).read()
            driver.get(url)
            soup = BeautifulSoup(html, 'html.parser')
            lis_title = []
            lis_content = []
            lis_link = []
            lis_answer = []
            title = soup.find_all('h2', {'class': 'h1'})  # 제목 크롤링
            answer = soup.find_all('p', {'class': 't1 t-dot'})  # 답변 크롤링
            for n in title:
                if "										" in n.get_text():
                    n = n.get_text().replace("										", "")  # 빈칸 없애는 작업
                    temp = n.split("\n")  # 내용을 엔터 기준으로 나눴을 때, 제목이 보통 temp[5]나 temp[6]에 들어가있음
                    if len(temp[5]) > 5:  # 제목을 제외하고 가장 긴 길이의 요소가 5글자여서 temp[5]가 5글자보다 길면 temp[5]를 리스트에 집어넣음
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

                elif "	" in n.get_text():  # 위와 마찬가지
                    n = n.get_text().replace("	", "")
                    temp = n.split("\n")
                    if len(temp[5]) > 5:
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

                else:
                    temp = n.split("\n")  # 위와 마찬가지
                    if len(temp[5]) > 5:
                        lis_title.append(temp[5])
                    else:
                        lis_title.append(temp[6])

            for i in answer:  # 답변 가져오는 반복문
                if "										" in i.get_text():
                    i = i.get_text().replace("										", "")
                    lis_answer.append(i)

            for links in soup.find_all('h2', {'class': 'h1'}):  # 세부 링크 가져오는 반복문
                for a in links.select("a[href^='/auction/counsel/view']"):
                    lis_link.append("http://www.lawsee.com/" + a.get('href'))

            for b in lis_link:  # html 링크 내에 사례 가져오는 반복문
                link_url = b
                link_html = urllib.request.urlopen(link_url).read()
                soup_1 = BeautifulSoup(link_html, 'html.parser')
                real_con = soup_1.select_one("div.bbsN_cbox p").get_text()
                lis_content.append(real_con)

            if len(lis_title) <= 3:
                self.onButtonClicked()

            else:
                print(len(lis_title))
                content_num = 1
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])"
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])"
                    print(tb_t)
                    exec(tb_t)
                    print(tb_c)
                    exec(tb_c)
                    content_num += 1

        elif (Site == "LAW TALK"):
            search = self.cb1.currentText() + ' ' + self.cb2.currentText()
            driver = webdriver.Chrome('chromedriver.exe')
            url_query_law = quote(string=search)
            url = "https://www.lawtalk.co.kr/cases?pg=1&sort=recentAnswer&keyword=" + url_query_law
            driver.get(url)

            lis_title = []
            lis_content = []
            wait = WebDriverWait(driver, 5)
            image = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'case-card__title')))

            for a in range(1, 11):
                path = '//*[@id="root-view"]/div[2]/div[3]/section/div/div[4]/div/section/case-card[' + str(
                    a) + ']/a'
                law_btn = driver.find_element_by_xpath(path)
                law_btn.click()
                time.sleep(1)
                driver.switch_to.window(driver.window_handles[-1])  # 클릭해서 열린페이지로 이동
                driver.implicitly_wait(5)
                time.sleep(1)
                title = driver.find_element_by_xpath('//*[@id="root-view"]/div/div/div/question/div/h1').text
                con = driver.find_element_by_xpath(
                    '//*[@id="root-view"]/div/div/div/question/div/p').text

                lis_title.append(title)
                lis_content.append(con)
                driver.back()
                # 로딩 기다리기
                time.sleep(0.5)

            for i in lis_title:
                print(i)

            for j in lis_content:
                print("**********\n", j)

            if len(lis_title) <= 3:
                self.onButtonClicked()

            else:
                print(len(lis_title))
                content_num = 1
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])"
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])"
                    print(tb_t)
                    exec(tb_t)
                    print(tb_c)
                    exec(tb_c)
                    content_num += 1

        elif (Site == "대한민국 법원 종합법률정보"):
            lis_title = []
            lis_content = []

            search = self.cb1.currentText() + " " + self.cb2.currentText()

            driver = webdriver.Chrome('chromedriver')
            link = 'https://glaw.scourt.go.kr/wsjo/panre/sjo050.do'
            driver.get('https://glaw.scourt.go.kr/wsjo/panre/sjo050.do')  # 판례검색 사이트 접속

            time.sleep(0.5)

            driver.find_element_by_xpath('//*[@id="search"]/div[2]/fieldset/input').send_keys(search)  # 키워드 입력 'search'
            driver.find_element_by_xpath('//*[@id="srch_img"]').click()  # 검색버튼 클릭

            time.sleep(0.5)

            for i in range(0, 20):  # 판례 내용 읽기
                v = str(i)
                subpage = driver.page_source
                soup = bs(subpage, 'html.parser')  # html 파싱
                driver.implicitly_wait(30)  # 기다려주기

            title = soup.select('td:nth-child(2) > dl > dt > a:nth-child(1)')  # 제목 - bs 셀렉터
            for tit in title:
                lis_title.append(tit.text)
                print(tit.text)

            print('\n' "#################################" '\n')

            content = soup.select('td:nth-child(2) > dl > dd:nth-child(3)')  # 내용 - bs 셀렉터
            for con in content:
                lis_content.append(con.text)
                print(con.text)

            if len(lis_title) <= 3:
                self.onButtonClicked()

            else:
                print(len(lis_title))
                content_num = 1
                for i in range(0, len(lis_title)):
                    tb_t = "self.textBrowser_" + str(content_num) + ".setText(lis_title[" + str(i) + "])"
                    tb_c = "self.textEdit_" + str(content_num) + ".setText(lis_content[" + str(i) + "])"
                    print(tb_t)
                    exec(tb_t)
                    print(tb_c)
                    exec(tb_c)
                    content_num += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()