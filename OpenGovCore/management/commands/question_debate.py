from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from time import sleep, time
from random import choice
import os
import requests
from urllib.request import urlopen as uReq
from .opengovparser import OpenGovParser


options = webdriver.ChromeOptions()
options.headless = True


class ScrapeLokSabha(OpenGovParser):
    page_count = 1
    def load_questions(self):
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        browser.implicitly_wait(5)
        browser.get(self.url)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_questions(browser)
    
    def nextPageQuestions(self,browser):
        browser.find_element_by_id("ContentPlaceHolder1_txtpage").clear()
        inputElement = browser.find_element_by_id("ContentPlaceHolder1_txtpage")
        inputElement.send_keys(ScrapeLokSabha.page_count)
        element = browser.find_element_by_id("ContentPlaceHolder1_btngo")
        element.click()
        sleep(4)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_questions(browser)
    
    def fetch_questions(self,browser):
        table = self.soup.find('table', { "id" : "ContentPlaceHolder1_tblMember" }).find("tbody")
        rows = table.find("table",{"class":"member_list_table"}).find("tbody").find_all("tr")
        total_pages = self.soup.find("table",{"class":"pagings"}).find("tbody").find_all("td")[2]
        page_no = int(total_pages.find("span",{"id":"ContentPlaceHolder1_lblfrom"}).text.strip().split(" ")[1])
        for row in rows:
            question_number = row.find_all('td')[0].text.strip()
            type = row.find_all('td')[1].text.strip().split()[0]
            date = row.find_all('td')[2].text.strip()
            ministry = row.find_all('td')[3].text.strip()
            #member = row.find_all('td')[4].text.strip()
            member = row.find_all('td')[4].text.strip().split(",")
            members_list = []
            for i in range(0,len(member),2):
                members_list.append(member[i+1]+" "+ member[i])
            subject = row.find_all('td')[5].text.strip()
            question_link = row.find_all('td')[5].find_all('a')[-1]['href']
            formed_url = "http://loksabhaph.nic.in/Questions/" + question_link
            print("Question Number ", question_number)
            print("Question Type",type)
            print("Date ",date)
            print("Ministry ",ministry)
            print("Member ",members_list)
            print("Subject ",subject)
            self.url = formed_url
            super().load_parser()
            question,answer = self.getQuestionText()
            print("Question",question)
            #print("Answer",answer)
            data = [date,ministry,members_list,subject,question,answer,formed_url,type]
            OpenGovParser.load_questions(self,*data)
            print()
            #break
        ScrapeLokSabha.page_count += 1
        print("/////////////////////////////////////////////////",ScrapeLokSabha.page_count)
        if ScrapeLokSabha.page_count > page_no:
            ScrapeLokSabha.page_count = 1
            return
        else:
            self.nextPageQuestions(browser)
    def getQuestionText(self):
        main_table = self.soup.find_all('table')[1]
        othertables = main_table.find_all('table')
        question_num = othertables[4].find_all('span')[1].text
        answered_on = othertables[5].find('span').text
        try:
            question = othertables[9].find_all("td",attrs={'class':'stylefontsize'})[1].text.strip()
            answer = othertables[9].find_all("td",attrs={'class':'stylefontsize'})[2].text.strip()
        except:
            try:
                question = main_table.find("table",{"id":"ContentPlaceHolder1_GridView2"}).find_all("td",{"class":"stylefontsize"})[0].text.strip()
                answer = main_table.find("table",{"id":"ContentPlaceHolder1_GridView2"}).find_all("td",{"class":"stylefontsize"})[1].text.strip()
            except:
                question = ""
                answer = ""
        #print("Question Number : ",question_num)
        #print("Answered On : ",answered_on)
        #print("Question : ",question)
        print("============================================================================================")
        return [question,answer]
    def load_debates(self):
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        browser.implicitly_wait(5)
        browser.get(self.url)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_debates(browser)
    def fetch_debates(self,browser):
        div_sec = self.soup.find("div",{"id":"content"}).find("div",{"id":"ContentPlaceHolder1_Panel2"})
        tables = div_sec.find_all("table")
        for i in range(1,len(tables) - 2):
            rows = tables[i].find("tbody").find_all("tr")
            debate_type = rows[0].find_all("td")[1].text.strip()
            debate_title = rows[1].find_all("td")[1].text.strip()
            debate_date = rows[2].find_all("td")[1].text.strip()
            #participants = rows[3].find_all("td")[1].text.strip()
            participants = rows[3].find_all("td")[1].text.strip().split(",")
            participants_list = []
            if len(participants) > 1:
                for i in range(0,len(participants),2):
                    participants_list.append(participants[i+1]+" "+ participants[i])
            else:
                participants_list = participants
            debate_link = "http://loksabhaph.nic.in/Debates/" + rows[1].find_all("td")[1].find('a')["href"]
            print("Debate Type: ",debate_type)
            print("Debate Title : ",debate_title)
            print("Debate Date : ",debate_date)
            print("Debate Perticipants : ",participants_list)
            print("Debate Link : ",debate_link)
            data = [debate_title,debate_type,debate_date,participants_list,debate_link]
            OpenGovParser.load_debates(self,*data)
            print("Debate data added")

        total_pages = self.soup.find("table",{"class":"pagings"}).find("tbody").find_all("td")[2]
        page_no = int(total_pages.find("span",{"id":"ContentPlaceHolder1_lblfrom"}).text.strip().split(" ")[1])
        ScrapeLokSabha.page_count += 1
        print("/////////////////////////////////////////////////",ScrapeLokSabha.page_count)
        if ScrapeLokSabha.page_count > page_no:
            return
        else:
            self.nextPageDebates(browser)
    
    def nextPageDebates(self,browser):
        browser.find_element_by_id("ContentPlaceHolder1_txtpage").clear()
        inputElement = browser.find_element_by_id("ContentPlaceHolder1_txtpage")
        inputElement.send_keys(ScrapeLokSabha.page_count)
        element = browser.find_element_by_id("ContentPlaceHolder1_btngo")
        element.click()
        sleep(4)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_debates(browser)




