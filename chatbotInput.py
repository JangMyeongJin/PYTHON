#!/usr/bin/env python
# coding: utf-8



# 챗봇 QnA Input

# In[7]:


from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv
import time
from urllib.request import urlopen
from urllib.request import HTTPError
import re
from pprint import pprint as pp

c_options = ChromeOptions()
#c_options.add_argument('--headless')
c_options.add_argument('--no-sandbox')
c_options.add_argument('--disable-dev-shm-usage')
c_options.add_argument('--window-size=1920x1080')
    
sample_csv_r = open('C:\\chatbotData/장명진_지식_대화_3.csv','rt',encoding='UTF8')
sample_csv_read = csv.reader(sample_csv_r)
    
try : 
    #QnAList 만들기
    QnAList =[]
    QnANameList = []
    nameCount = 0
    for line in sample_csv_read:
        QnAHashMap = {}
    
        QnAName = line[2]
        nameCount += 1
        if QnAName not in QnANameList:
            nameCount = 1
            QnANameFull = QnAName + str(nameCount)
        else:
            QnANameFull = QnAName + str(nameCount)
        QnANameList.append(QnAName)
    
        tagNameFull = line[3]
        tagList = []
        nameList = tagNameFull.split('\n')
        for n in nameList:
            tagName = re.sub('[(,)]','',n)
            tagList.append(tagName)

        questionList = []
        fullQuestion = line[8]
        count = fullQuestion.find(']')
        question = fullQuestion[count+1:]
        questionList.append(fullQuestion)
        questionList.append(question)

        answer = line[9].replace('\n','')

        QnAHashMap['QnAName'] = QnANameFull
        QnAHashMap['categoryName'] = QnAName
        QnAHashMap['QnATag'] = tagList
        QnAHashMap['QnAQuestionList'] = questionList
        QnAHashMap['QnAAnswer'] = answer
        

        QnAList.append(QnAHashMap)

    #중간부터 데이터 넣기
    listCount = 0
    for line in QnAList:
        name = 'myPC22'

        if name == line['QnAName']:
            break
        else:
            listCount += 1
    
    QnAList = QnAList[listCount+1:]

    prochat_driver = Chrome('C:\\chromedriver.exe', options=c_options)
    prochat_driver.get('http://192.168.0.5:6551/manager/login.ps')

    userIdInput = WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.ID, 'userId'))
    userPWInput = WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.ID, 'password'))
    #로그인
    userId = 'jean9710'
    userPW = 'jean13568!'
    userIdInput.send_keys(userId)
    userPWInput.send_keys(userPW + Keys.ENTER)

    time.sleep(5)

    WebDriverWait(prochat_driver, 15).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/aside/div/nav/ul/li[1]/a')).click()

    WebDriverWait(prochat_driver, 15).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/aside/div/nav/ul/li[1]/ul/li[2]/a')).click()

    time.sleep(1)

    #신규등록
    for line in QnAList:
        categoryName = line['categoryName']
        QnAName = line['QnAName']
        questionListInput = line['QnAQuestionList']
        tagList = line['QnATag']
        answer = line['QnAAnswer']
        

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/form/div/div[2]/div/div/div/div[2]/div/a[3]')).click()

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.ID, 'categoryName')).click()

        time.sleep(1)

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[2]/input')).send_keys(categoryName + Keys.ENTER)

        time.sleep(1)

        categoryUl = WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.CLASS_NAME, 'list-group'))
        categoryLis = WebDriverWait(categoryUl, 10).until(lambda x: x.find_elements(By.TAG_NAME, 'li'))

        count = 0
        for category in categoryLis:
            count += 1
            if category.text == categoryName:

                WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[3]/ul/li['+str(count)+']')).click()

                WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')).click()
                break
            
        time.sleep(1)

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.ID, 'dialogNm')).send_keys(QnAName + Keys.ENTER)

        time.sleep(1)

        for tagName in tagList:
                WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/input')).send_keys(tagName + Keys.ENTER)

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/button')).click()

        time.sleep(1)

        print(questionListInput)
        for questionInput in questionListInput:
            WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.ID, 'ipt_question')).send_keys(questionInput + Keys.ENTER)
            time.sleep(1)

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.NAME, 'answer_desc')).send_keys(answer)

        WebDriverWait(prochat_driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[2]/form/div/div[6]/button')).send_keys(Keys.ENTER)

        time.sleep(1)

        prochat_driver.back()

        alert = prochat_driver.switch_to.alert

        alert.accept()
        print(QnAName + ' 입력')

        time.sleep(1)

    prochat_driver.quit()

except Exception as e:
    print('Error',e)

sample_csv_r.close()
print('csv close')

