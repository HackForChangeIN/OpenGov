from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from time import sleep, time
from random import choice
import os
import requests
from urllib.request import urlopen as uReq
from .opengovparser import OpenGovParser
from selenium.webdriver.support.ui import Select
from OpenGovCore.models import Questions,Term,Debates,Bills
import datetime


options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)



class ScrapeLokSabha(OpenGovParser):
    page_count = 1
    att_page_no = 0
    bill_count = 0
    bills_page_no = 0

    def load_questions(self):
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
        term = self.term
        
        for row in rows:
            try:
                question_number = row.find_all('td')[0].text.strip()
            except:
                question_number = ""
            try:
                question_type = row.find_all('td')[1].text.strip().split()[0]
            except: 
                question_type = ""
            try:
                date = row.find_all('td')[2].text.strip()  #23.09.2020
                date=date.split(".") #23.09.2020
                date = date[2] + "-" + date[1] + "-" + date[0]
                format_str = '%Y-%m-%d'
                date=datetime.datetime.strptime(date, format_str).date()

            except: 
                date = ""
            try:
                ministry = row.find_all('td')[3].text.strip()
            except: 
                ministry = ""
            try:
                member = row.find_all('td')[4].text.strip().split(",")
                members_list = []
                if len(member) % 2 == 0:
                    for i in range(0,len(member),2):
                        member_name_info = member[i+1].strip()+" "+ member[i].strip()
                        members_list.append(member_name_info.strip())
                elif len(member) == 1:
                    try:
                        single_member = member[0].split(" ",1)[1].strip() + " " + member[0].split(" ",1)[0].strip()
                        members_list.append(single_member)
                    except:
                        single_member = member[0].split("-")[1].strip() + " " + member[0].split(" ",1)[0].strip()
                        members_list.append(single_member)
                else:
                    members_list = []
                    continue
            except:
                continue
            try:
                subject = row.find_all('td')[5].text.strip()
            except:
                subject = ""
            try:
                question_link = row.find_all('td')[5].find_all('a')[-1]['href']
            except:
                question_link = ""
            formed_url = "http://loksabhaph.nic.in/Questions/" + question_link
            print("Question Number ", question_number)
            print("Question Type",question_type)
            print("Date ",date)
            print("Ministry ",ministry)
            print("Member ",members_list)
            print("Subject ",subject)
            print("term",term)
            self.url = formed_url
            try:
                super().load_parser()
            except:
                continue
            question,answer = self.getQuestionText()
            print("Question",question)
            """ Date checking"""
            term_id=Term.objects.get(term_name = term)
            latest_date = Questions.objects.filter(term_id=term_id).latest('date')
            if date >= latest_date.date:
                print(" New Question inserted")
            else:
                print("Question already present")
                return
            data = [date,ministry,members_list,subject,question,answer,formed_url,question_type,term]
            OpenGovParser.load_questions(self,*data)
            print("Question added to Database")
            
        ScrapeLokSabha.page_count += 1
        print("/////////////////////////////////////////////////",ScrapeLokSabha.page_count)
        if ScrapeLokSabha.page_count > 10: #replace with page_no
            ScrapeLokSabha.page_count = 1
            return
        else:
            self.nextPageQuestions(browser)


    def getQuestionText(self):
        try:
            main_table = self.soup.find_all('table')[1]
        except:
            return
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
        return [question,answer]

    #########################   Debates  ######################
    def load_debates(self):
        browser.implicitly_wait(5)
        browser.get(self.url)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_debates(browser)


    def fetch_debates(self,browser):
        div_sec = self.soup.find("div",{"id":"content"}).find("div",{"id":"ContentPlaceHolder1_Panel2"})
        tables = div_sec.find_all("table")
        term = self.term

        for i in range(1,len(tables) - 2):
            try:
                rows = tables[i].find("tbody").find_all("tr")
            except:
                continue

            try:
                debate_type = rows[0].find_all("td")[1].text.strip()
            except:
                debate_type = ""
            try:
                debate_title = rows[1].find_all("td")[1].text.strip()
            except:
                debate_title = ""
            try:
                debate_date = rows[2].find_all("td")[1].text.strip()
                debate_date=debate_date.split("-") #23-09-2020
                debate_date = debate_date[2] + "-" + debate_date[1] + "-" + debate_date[0]
                format_str = '%Y-%m-%d'
                debate_date=datetime.datetime.strptime(debate_date, format_str).date()

            except:
                debate_date = ""
            try:
                participants = rows[3].find_all("td")[1].text.strip().split(",")
                participants_list = []
            except:
                continue
            
            try:
                if len(participants) > 1:
                    for i in range(0,len(participants),2):
                        participants_info = participants[i+1].strip()+" "+ participants[i].strip()
                        participants_list.append(participants_info)
                elif len(participants) == 1:
                    try:
                        participant = participants[0].split(" ",1)[1].strip() + " " + participants[0].split(" ",1)[0].strip()
                        participants_list.append(participant)
                    except:
                        participant = participants[0].split("-")[1].strip() + " " + participants[0].split(" ",1)[0].strip()
                        participants_list.append(participant)
                else:
                    participants_list = participants
            except:
                continue

            debate_link = "http://loksabhaph.nic.in/Debates/" + rows[1].find_all("td")[1].find('a')["href"]
            print("Debate Type: ",debate_type)
            print("Debate Title : ",debate_title)
            print("Debate Date : ",debate_date)
            print("Debate Perticipants : ",participants_list)
            print("Debate Link : ",debate_link)
            print ("Term",term)
            term_id = Term.objects.get(term_name = term)
            latest_date = Debates.objects.filter(term_id=term_id).latest('date')
            if debate_date >= latest_date.date:
                print("New debate inserted")
            else:
                print("Debate already exist")
                return
            data = [debate_title,debate_type,debate_date,participants_list,debate_link,term]
            OpenGovParser.load_debates(self,*data)
            print("Debate data added")

        total_pages = self.soup.find("table",{"class":"pagings"}).find("tbody").find_all("td")[2]
        page_no = int(total_pages.find("span",{"id":"ContentPlaceHolder1_lblfrom"}).text.strip().split(" ")[1])
        ScrapeLokSabha.page_count += 1
        print("/////////////////////////////////////////////////",ScrapeLokSabha.page_count)
        if ScrapeLokSabha.page_count > 10: # replace with page_no
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

    ################### Bills############################

    def load_bills(self):
        #browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        browser.implicitly_wait(5)
        browser.get(self.url)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        element = browser.find_element_by_id("ContentPlaceHolder1_RadioButtonList1_0").click()
        bill_type = browser.find_element_by_id("ContentPlaceHolder1_RadioBttnbilltyp_0").click()
        submit_element = browser.find_element_by_id("ContentPlaceHolder1_btnsbmt").click()
        sleep(4)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_bills(browser)
    def fetch_bills(self,browser):
        table = self.soup.find("table",{"class":"member_list_table_td"}).find("tbody").find("table")
        all_rows = table.find("tbody").find_all("tr")
        total_bills = self.soup.find('table',{'id':'Table5'}).find("tbody").find("tr").find("td").find_all('span')[1].text.strip()
        for i in range(3,len(all_rows)):
            try:
                year = all_rows[i].find_all("td")[0].text.strip()
            except:
                year = ""
            try:
                bill_no = all_rows[i].find_all("td")[1].text.strip()
            except:
                bill_no = ""
            try:
                bill_title = all_rows[i].find_all("td")[2].find('a').text.strip()
            except:
                bill_title = ""
            try:
                bill_link = all_rows[i].find_all("td")[2].find_all('a')[1]['href']
            except:
                bill_link = ""
            try:
                bill_type = all_rows[i].find_all("td")[3].text.strip()
            except:
                bill_type = ""
            try:
                date_of_intoduction = all_rows[i].find_all("td")[5].find_all('span')[0].text.strip()
                date_of_intoduction=date_of_intoduction.split("/") #22/09/2020
                date_of_intoduction = date_of_intoduction[2] + "-" + date_of_intoduction[1] + "-" + date_of_intoduction[0]
                format_str = '%Y-%m-%d'
                date_of_intoduction=datetime.datetime.strptime(date_of_intoduction, format_str).date()

            except:
                date_of_intoduction = ""
            try:
                house_introduced = all_rows[i].find_all("td")[5].find_all('span')[1].text.strip()
            except:
                house_introduced = ""
            try:
                debate_passed_date_loksabha = all_rows[i].find_all("td")[6].find('a').text.strip()
            except:
                debate_passed_date_loksabha = ""
            try:
                debate_passed_date_rajyasabha = all_rows[i].find_all("td")[7].text.strip()
            except:
                debate_passed_date_rajyasabha = ""
            try:
                status = all_rows[i].find_all("td")[11].text.strip()
            except:
                status = ""
            print("Year : ",year)
            print("Bill no : ",bill_no)
            print("Bill title : ", bill_title)
            print("Bill Link  : ",bill_link)
            print("Bil type : ",bill_type)
            print("Date of Introduction : ",date_of_intoduction)
            print("House Introduced : ",house_introduced)
            print("Debate Passed date loksabha : ",debate_passed_date_loksabha)
            print("Debate Passed date Rajyasabha : ",debate_passed_date_rajyasabha)
            print("Status : ",status)
            latest_date = Bills.objects.latest('date_of_introduction')
            if date_of_intoduction >= latest_date.date_of_introduction:
                print("New Bill inserted")
            else:
                print("Bill already exist")
                return
            data = []
            data = [bill_title,bill_type,status,date_of_intoduction,debate_passed_date_loksabha,debate_passed_date_rajyasabha,bill_link]
            OpenGovParser.load_bills(self,*data)
            ScrapeLokSabha.bill_count += 1
        if(ScrapeLokSabha.bill_count > 100):  # replace 10 with total_bills
            return
        ScrapeLokSabha.bills_page_no += 1
        if(ScrapeLokSabha.bills_page_no % 10 == 0):
            return
        self.nextPageBills(browser)
    def nextPageBills(self,browser):
        if ScrapeLokSabha.bills_page_no <= 10:
            td_pages = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_GR1']/tbody/tr/td/table/tbody/tr/td")
            td_page = td_pages[:len(td_pages)-1]
        else:
            td_pages = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_GR1']/tbody/tr/td/table/tbody/tr/td")
            td_page = td_pages[2:len(td_pages)-1]
        element = td_page[ScrapeLokSabha.bills_page_no%10]
        element.click()
        browser.implicitly_wait(5)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_bills(browser)
        if ScrapeLokSabha.bills_page_no % 10 == 0:
            element = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_GR1']/tbody/tr/td/table/tbody/tr/td")[-2]
            element.click()
            browser.implicitly_wait(5)
            html_source = browser.page_source.encode('utf-8')
            self.soup = bs(html_source,"html.parser")
            self.fetch_bills(browser)
    
    ###########    Attendance    ########################
    def load_attendance(self):
        #browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        browser.implicitly_wait(5)
        browser.get(self.url)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.changeSessions(browser)
    def date_conversion(self,date):
        date=date.split(".") #23.09.2020
        date = date[2] + "-" + date[1] + "-" + date[0]
        format_str = '%Y-%m-%d'
        date=datetime.datetime.strptime(date,format_str).date()
        return date
    def fetch_attendance(self,browser,session_name,session_start_date,session_end_date):
        table = self.soup.find("table",{"id":"ContentPlaceHolder1_DataGrid1"}).find("tbody")
        rows = table.find_all("tr")
        #no_pages = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_DataGrid1']/tbody/tr/td/a")
        no_pages = self.soup.find("table",{"id":"ContentPlaceHolder1_DataGrid1"}).find("tbody").find("tr").find("td").find_all("a")
        if type(session_start_date)=="str":
            session_start_date = self.date_conversion(session_start_date)
            session_end_date = self.date_conversion(session_end_date)
        for i in range(2,len(rows)-1):
            member_name = rows[i].find_all("td")[0].text.strip()
            constituency = rows[i].find_all("td")[1].text.strip()
            days_members_signed = rows[i].find_all("td")[2].text.strip()
            if '(' in session_name:
                session_name = session_name.split('(')[0].strip()
            else:
                session_name = session_name
            
            print("Session Name : ",session_name)
            print("Member Name : ",member_name)
            print("Constituency : ",constituency)
            print("Number of Days Members signed Register",days_members_signed)
            data =[]
            data = [session_name,member_name,constituency,days_members_signed,self.term,session_start_date,session_end_date]
            OpenGovParser.load_attendance(self,*data)
            print(member_name," attendance data added")

        print("All attendance data added")
        ScrapeLokSabha.att_page_no += 1
        print("Page No : ",ScrapeLokSabha.att_page_no)
        print("no pages : ",len(no_pages))
        if(ScrapeLokSabha.att_page_no >= len(no_pages)):
            ScrapeLokSabha.att_page_no = 0
            td_pages = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_DataGrid1']/tbody/tr/td/a")
            elements = td_pages[ScrapeLokSabha.att_page_no]
            elements.click()
            return
        else:
            self.nextPageAttendance(browser,session_name,session_start_date,session_end_date)
    def nextPageAttendance(self,browser,session_name,session_start_date,session_end_date):
        td_pages = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_DataGrid1']/tbody/tr/td/a")
        elements = td_pages[ScrapeLokSabha.att_page_no]
        elements.click()
        sleep(4)
        html_source = browser.page_source.encode('utf-8')
        self.soup = bs(html_source,"html.parser")
        self.fetch_attendance(browser,session_name,session_start_date ,session_end_date)
    def changeSessions(self,browser):
        session_length = self.soup.find("select",{"id":"ContentPlaceHolder1_DropDownListSession"}).find_all("option")
        latest_term = self.soup.find("select",{"id":"ContentPlaceHolder1_DropDownListLoksabha"}).find_all("option")[0].text.strip() + 'th'
        self.term = latest_term
        for i in range(1,len(session_length)+1):
            select = Select(browser.find_element_by_id("ContentPlaceHolder1_DropDownListSession"))
            select.select_by_value(str(i))
            element = session_length[-i]
            session_name = element.text
            session_start_date = self.soup.find("select",{"id":"ContentPlaceHolder1_DropDownListSession"}).find_all("option")[-i].text.strip().split("(")[1].split(" to ")[0].strip()
            session_end_date = self.soup.find("select",{"id":"ContentPlaceHolder1_DropDownListSession"}).find_all("option")[-i].text.strip().split(" to ")[-1].replace(")","").strip()
            html_source = browser.page_source.encode('utf-8')
            self.soup = bs(html_source,"html.parser")
            self.fetch_attendance(browser,session_name,session_start_date,session_end_date)




