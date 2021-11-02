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
import shutil
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
import re
import datetime
from OpenGovCore.models import Questions,Parliamentary_Sessions

options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

""""options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)"""


class RajyaSabhaParser(OpenGovParser):

	current_page_no = 1
	current_record = 0
	
	def find_all_urls(self,browser):
		count = False
		elements = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView2']/tbody/tr")

		for i in range(1,len(elements)):
			if count == True:
				browser.get(self.url)
				elements = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView2']/tbody/tr")
			element = elements[i].find_elements_by_tag_name("td")[1].find_element_by_tag_name("a")
			element.click()
			browser.implicitly_wait(5)
			html_source = browser.page_source
			self.load_data(html_source,browser)
			count = True
			
			
	def load_data(self,html_source,browser):
		self.soup = bs(html_source, "html.parser")
		table = self.soup.find("table",{"id":"ctl00_ContentPlaceHolder1_GridView1"}).find("tbody")
		img = table.find("tr").find_all("td")[0].find("img")["src"]
		img_link = "https://rajyasabha.nic.in/rsnew/member_site/" + img
		mp_name = table.find("tr").find_all("td")[1].find("span").text.strip()
		mp_name = re.sub(' +', ' ', mp_name)

		body = self.soup.find("div",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_body"})
		all_rows = body.find("table").find("tbody").find_all("tr")
		#state = all_rows[0].find_all("td")[1].text.strip()
		state = table.find("span",{"id":"ctl00_ContentPlaceHolder1_GridView1_ctl02_Label26"}).text.replace("  ","").split(':')[1].strip()
		#party = all_rows[1].find_all("td")[1].text.strip()
		party = table.find("span",{"id":"ctl00_ContentPlaceHolder1_GridView1_ctl02_Label27"}).text.replace("  ","").split(':')[1].strip()
		#present_add = all_rows[2].find_all("td")[1].text.strip()
		#present_add = re.sub(' +', ' ', present_add)
		office_phone_no = all_rows[3].find_all("td")[1].text.strip()

		#permanent_add = all_rows[4].find_all("td")[1].text.strip()
		#permanent_add =  re.sub(' +', ' ', permanent_add)
		#home_phone_no = all_rows[5].find_all("td")[1].text.strip()
		#email_id = all_rows[6].find_all("td")[1].find("img")["src"].split("id=")[-1].strip()
		email_id = ""

		print("Mp_name: ",mp_name)
		#print("Image URL: ", img_link)
		print("State: ",state)
		print("Party: ",party)
		#print("Present Address: ",present_add)
		#print("office Phone no: ",office_phone_no)
		#print("Permanent Address: ",permanent_add)
		#print("Home Phone no: ",home_phone_no)
		#print("Email ID: ",email_id)
		source = "https://rajyasabha.nic.in/rsnew/member_site/memberlist.aspx"
		dob,education,profession,permanent_address,present_address = self.get_biodata(browser)
		image_name,img_temp = self.download_image(img_link)
		constituency = " "
		term = ''
		office_phone_no = ''
		data = [mp_name,constituency,state,party,email_id,dob,education,profession,permanent_address,present_address,office_phone_no,image_name,source,img_temp,term]
		OpenGovParser.load_candidate_data(self,*data)
		OpenGovParser.load_rajyasabha_candidature_data(self,*data)
		print(mp_name,"is added")
	





	def get_biodata(self,browser):
		element = browser.find_element_by_xpath("//a[@id='__tab_ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata']")
		element.click()
		browser.implicitly_wait(4)
		sleep(3)
		self.parser(browser)
		
		table_rows = self.soup.find("table",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata_DetailsView_Biodata"}).find("tbody").find_all("tr")

		mp_name = table_rows[0].find_all("td")[1].find_all("span")[0].text.strip()
		mp_fathers_name = table_rows[0].find_all("td")[1].find_all("span")[1].text.strip()
		mp_mothers_name = table_rows[1].find_all("td")[1].find("span").text.strip()
		dob = table_rows[2].find_all("td")[1].find("span").text.strip()
		place_of_birth = table_rows[3].find_all("td")[1].find("span").text.strip()
		marital_status = table_rows[4].find_all("td")[1].find("span").text.strip()
		spouse_name = table_rows[5].find_all("td")[1].find("span").text.strip()
		children = table_rows[6].find_all("td")[1].find("span").text.strip()
		education = table_rows[7].find_all("td")[1].find("span",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata_DetailsView_Biodata_Label16"}).text.replace("  ","").strip()
		profession = table_rows[8].find_all("td")[1].find("span",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata_DetailsView_Biodata_Label17"}).text.replace("  ","").strip()
		permanent_address = table_rows[9].find_all("td")[1].find("span",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata_DetailsView_Biodata_Label18"}).text.replace("  ","").strip()
		present_address = table_rows[10].find_all("td")[1].find("span",{"id":"ctl00_ContentPlaceHolder1_TabContainer1_Tab_Biodata_DetailsView_Biodata_Label19"}).text.replace("  ","").strip()
		#print("MP name :",mp_name)
		#print("Mp Fathers name :", mp_fathers_name)
		#print("Mp Mothers name :", mp_mothers_name)
		#print("dob :", dob)
		#print("Place of birth: ", place_of_birth)
		#print("marital Status :",marital_status)
		#print("Spouse name :", spouse_name)
		#print("Children",children)
		#print("Education :",education)
		#print("Profession :", profession)
		#print("permanent address:",permanent_address)
		#print("present address:",present_address)
		return dob,education,profession,permanent_address,present_address

	def download_image( self,img_src):
		filename = img_src.rsplit("/")[-1]
		img_temp = NamedTemporaryFile(delete=True)
		try:
			img_temp.write(urlopen(img_src).read())
			img_temp.flush()
		except:
			img_temp.write(urlopen("https://prsindia.org/files/mptrack/16-lok-sabha/profile_image/160053.jpg").read())
			img_temp.flush()
		return filename,img_temp
	def load_candidate_data(self):
		browser.get(self.url)
		self.parser(browser)
		self.find_all_urls(browser)
		
		

	def parser(self,browser):
		html_source = browser.page_source.encode('utf-8')
		self.soup = bs(html_source, "html.parser")
	#######################Question#####################


	def load_questions(self):
		browser.get(self.url)
		element = browser.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_Button2']")
		element.click()
		browser.implicitly_wait(4)
		sleep(3)
		self.question_detail(browser)


	def question_detail(self,browser):
		self.parser(browser)
		table  = self.soup.find("table",{"id":"ctl00_ContentPlaceHolder1_DG1"}).find("tbody").find_all("tr")
		pages = len(table[0].find("td").find_all('a'))
		rows = table[2:len(table)-1]
		session = self.soup.find("select",{"id":"ctl00_ContentPlaceHolder1_DRSession"}).find_all("option")[0].text.strip()

		total_records = self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_Label4"}).text.strip().split("=")[1].strip().split(" ")[0].strip()
		max_pages = int(self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_Label4"}).text.strip().split("of ")[1].strip())
		current_page = self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_Label4"}).text.strip().split("Page ")[1].strip().split(" ")[0].strip()
		RajyaSabhaParser.current_page_no = int(current_page)
		

		for row in rows:
			sno = row.find_all("td")[0].text.strip()
			quesno = row.find_all("td")[1].text.strip()
			q_type = row.find_all("td")[2].text.strip()
			date = row.find_all("td")[3].text.strip()
			ministry = row.find_all("td")[4].text.strip()
			member = row.find_all("td")[5].text.strip()
			subject = row.find_all("td")[6].text.strip()
			english_file_link = row.find_all("td")[7].find("a")["href"]
			hindi_file_link = row.find_all("td")[8].find("a")["href"]
			date=date.split(".") #23.09.2020
			date = date[2] + "-" + date[1] + "-" + date[0]
			format_str = '%Y-%m-%d'
			date=datetime.datetime.strptime(date, format_str).date()
			#session = "252"
			session_id = Parliamentary_Sessions.objects.get(type = session)
			
			#latest_date = Questions.objects.filter(parliamentary_session_id = session_id).latest('date')
			#if date >= latest_date.date:
			#	print(" New Question inserted")
			#else:
			#	print("Question already present")
			#	return
			



			print("Sno :",sno)
			print("Ques No :",quesno)
			print("Ques Type :",q_type)
			print("Date :", date)
			print("Ministry :",ministry)
			print("Member :",member)
			print("Subject :",subject)
			print("English File Link :",english_file_link)
			#print("hindi File Link :",hindi_file_link)
			
			data = [date,ministry,member,subject,english_file_link,q_type,session]
			OpenGovParser.load_rajyasabha_question(self,*data)
			print(sno,"is added")

			RajyaSabhaParser.current_record += 1

		if RajyaSabhaParser.current_record == int(total_records):
			print("All questions added")
			return
		self.nextpage(max_pages,browser)


	def nextpage(self,max_pages,browser):
		elements = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_DG1']/tbody/tr")
		element = elements[0].find_elements_by_xpath("//td/a")
		if RajyaSabhaParser.current_page_no <= 10:
			try:
				element[RajyaSabhaParser.current_page_no - 1].click()
			except:
				print("next section")
	
		elif RajyaSabhaParser.current_page_no % 10 == 0:
			try:
				element[(RajyaSabhaParser.current_page_no % 10)+10].click()
			except:
				print("Next Section")
		else:
			try:
				element[RajyaSabhaParser.current_page_no % 10].click()
			except:
				print("Next Section")
	
		sleep(4)
		browser.implicitly_wait(4)
		self.question_detail(browser)
	############### Attendance#####################################
	def load_attendance(self):
		self.load_parser()
		table = self.soup.find("table",{"id":"ctl00_ContentPlaceHolder1_DataGrid1"}).find_all("tr")[1].find_all("td")
		session_no = table[0].text.strip()
		session_link = "https://rajyasabha.nic.in/rsnew/member_site/" + table[0].find('a')['href']
		self.url = session_link
		self.attendance_data(session_no)
	
	def date_conversion(self,date):
		date=date.split("-") #23-09-2020
		date = date[2] + "-" + date[1] + "-" + date[0]
		format_str = '%Y-%m-%d'
		date=datetime.datetime.strptime(date,format_str).date()
		return date

	def attendance_data(self,session_no):
		self.load_parser()
		session = self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_lb_sessionname"}).text.strip()
		session_start_date = self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_lb_period"}).text.strip().split("To")[0].replace("(","").strip()
		session_end_date = self.soup.find("span",{"id":"ctl00_ContentPlaceHolder1_lb_period"}).text.strip().split("To")[1].replace(")","").strip()
		session_start_date = self.date_conversion(session_start_date)
		session_end_date = self.date_conversion(session_end_date)
		all_rows = self.soup.find("table",{"id":"ctl00_ContentPlaceHolder1_GridView1"}).find_all("tr")

		for i in range(1,len(all_rows)):
			division = all_rows[i].find_all("td")[1].text.strip()
			member_name = all_rows[i].find_all("td")[2].text.strip()
			state = all_rows[i].find_all("td")[3].text.strip()
			days_signed_register = all_rows[i].find_all("td")[4].text.strip()
			source = self.url
			



			print("Division :",division)
			print("Member Name :",member_name)
			print("State :",state)
			print("Days signed Register :",days_signed_register)
			print("Session Name :",session)
			print("Session Start date",session_start_date)
			print("Session end date :",session_end_date)
			print("session_no:",session_no)
			
		
			
			data = [member_name,days_signed_register,session_no,source,session_start_date,session_end_date]
			OpenGovParser.load_rajyasabha_attendance_data(self,*data)
			print(member_name,"is added to Attendance")
		print("All candidate added to attendance for session",session_no )











