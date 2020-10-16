from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from opengovparser import OpenGovParser
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)




class OldLoksabhaParser(OpenGovParser):


	def load_candidate_details(self):
		table = self.soup.find("table",{"id":"ContentPlaceHolder1_tblMember"}).find("tbody").find_all("tr")[0].find("td")
		all_rows = table.find("table",{"class":"member_list_table"}).find("tbody").find_all("tr")
		for row in all_rows:
			member = row.find_all("td")[1].text.strip().split(",")
			member_name_info = member[1].strip()+" "+ member[0].strip()

			party = row.find_all("td")[2].text.strip()
			constituency = row.find_all("td")[3].text.strip().split("(")[0].strip()
			#state = row.find_all("td")[3].text.strip().split("(")[1].replace(')',"").strip()
			
			print("Member Name: ",member_name_info)
			print("Party: ",party)
			print("constituency: ",constituency)
			#print("State: ",state)


	def load_data(self):
		browser.get(self.url)
		browser.implicitly_wait(5)
		html_source = browser.page_source
		self.soup = bs(html_source, "html.parser")
		self.load_candidate_details()







# 16th term
url = "http://loksabhaph.nic.in/Members/lokaralpha.aspx?lsno=16&tab=0"
lok = OldLoksabhaParser(url=url)
lok.load_data()


# 15th term
url = "http://loksabhaph.nic.in/Members/lokaralpha.aspx?lsno=15&tab=1"
lok = OldLoksabhaParser(url=url)
lok.load_data()


# 14th term
url = "http://loksabhaph.nic.in/Members/lokaralpha.aspx?lsno=14&tab=2"
lok = OldLoksabha(url=url)
lok.load_data()