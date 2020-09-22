from opengovparser import OpenGovParser
import requests
import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


class PRSIndiaParser(OpenGovParser):
    def parse(self):
        client = urlopen(self.url)
        mplist = client.read()
        soup = bs(mplist, "html.parser")
        return soup

    def attendeance_details(self, soup):
        l = []
        att = soup.find_all("div", attrs={'class': 'view-content'})[0]
        overall_attendance = att.find('h2').text.split("(")[1].split(" ")[0]
        att_table_rows = att.find('table').find('tbody').find_all('tr')

		if len(att_table_rows) == 0:
            return l

		for row in att_table_rows:
			session = row.find_all('td')[0].text.strip()
			attendance = row.find_all('td')[1].text.strip()
			l.append([session, attendance])
		return l

    def debates_details(self, soup):
        l1 = []
        debates = soup.find_all("div", attrs={'class': 'view-content'})[1]
        deb_rows = debates.find('table').find('tbody').find_all('tr')
        if len(deb_rows) == 0:
			return l1

		for debate in deb_rows:
			debate_date = debate.find_all('td')[0].text.strip()
			debate_title = debate.find_all('td')[1].text.strip()
			debate_type = debate.find_all('td')[2].text.strip()
			l1.append([debate_date, debate_title, debate_type])
		return l1

    def questions_details(self, soup):
        l2 = []
        questions = soup.find_all("div", attrs={'class': 'view-content'})[2]
        question_rows = questions.find('tbody').find_all('tr')
        if len(question_rows) == 0:
			return l2

		for question in question_rows:
			ques_date = question.find_all('td')[0].text.strip()
			ques_title = question.find_all('td')[1].text.strip()
			ques_type = question.find_all('td')[2].text.strip()
			ques_category = question.find_all('td')[3].text.strip()
			l2.append([ques_date, ques_title, ques_type, ques_category])
		return l2

    def main_struct(self):
        soup = self.parse()
        all_class = soup.find_all("div", attrs={'class': 'view-content'})
        all_profiles = all_class[1].find_all(
            'div', attrs={'class': 'views-field views-field-title-field'})
        n = 0
		for link in all_profiles:
			profile_link = "https://www.prsindia.org"+link.find('a')['href']
			self.url = profile_link

			soup = self.parse()
			info = soup.find("div", attrs={'class': 'row mp_profile_header_info'})
			mp_name = info.find(
			    "div", attrs={'class': 'mp-name'}).find('h1').find('a').text
			mp_state = info.find_all("div", attrs={'class': 'mp_state'})[
                            0].find('a').text
			if '(' in mp_state:
				mp_state = mp_state.split('(')[0].strip()
			else:
				mp_state = mp_state

			mp_constituency = info.find(
			    "div", attrs={'class': 'mp_constituency'}).text.split(":")[1].strip()
			party = info.find_all("div", attrs={'class': 'mp_state'})[1].find('a').text
			if '(' in party:
				mp_party = party.split('(')[0].strip()
			else:
				mp_party = party

			nature_of_membership = info.find_all("div", attrs={'class': 'age'})[
                            0].text.split(":")[1].strip()
			start_term = info.find("span", attrs={'class': 'date-display-single'}).text
			term_end = info.find("div", attrs={'class': 'term_end'}).text.split(":")[
                            1].strip()
			num_of_term = info.find_all("div", attrs={'class': 'age'})[
                            1].text.split(":")[1].strip()

			standing_commitee = info.find("div", attrs={'class': 'standing'})
			if standing_commitee != None:
				standing_commitee_mem = standing_commitee.text
			else:
				standing_commitee_mem = ""

			gender = info.find("div", attrs={'class': 'gender'}).find('a').text
			education = info.find("div", attrs={'class': 'education'}).find('a').text

			l_att = self.attendeance_details(soup)
			l_deb = self.debates_details(soup)
			l_ques = self.questions_details(soup)

			print("MP Name : ", mp_name)
			print("Mp State : ", mp_state)
			print("MP Constituency : ", mp_constituency)
			print("MP Party : ", mp_party)
			print("Nature of Membership : ", nature_of_membership)
			print("Start term : ", start_term)
			print("Term end : ", term_end)
			print("No of term : ", num_of_term)
			print("Standing commitee : ", standing_commitee_mem)
			print("Gender : ", gender)
			print("Education : ", education)
			print("Session Att", l_att)
			print("Debates", l_deb)
			print("Questions", l_ques)

			print("===========================================================")

			n += 1


p1 = PRSIndia(url)
p1.main_struct()
#17thurl = "https://www.prsindia.org/mptrack"+"?field_paliament_term_tid=2302"
#url = "https://www.prsindia.org/mptrack"+"?field_paliament_term_tid=62"
