from .opengovparser import OpenGovParser
import requests
import shutil
import os
import urllib
from django.conf import settings
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile



class LoksabhaParser(OpenGovParser):

	def load_questions(self):
		pass

	def find_all_urls(self):
		all_class = self.soup.find("div", attrs={'id': 'divPrint'}).find_all('a')
		urls = []
		for a_tag in all_class:
			url = a_tag['href']
			if not url.startswith('http'):
				url = "http://loksabhaph.nic.in/Members/" + url
				urls.append(url)
		unique_urls = list(dict.fromkeys(urls))
		return unique_urls

	def download_image( self,img_src):
		filename = img_src.rsplit("/")[-1]
		img_temp = NamedTemporaryFile(delete=True)
		try:
			img_temp.write(urlopen(img_src).read())
			img_temp.flush()
		except:
			img_temp.write(urlopen("http://loksabhadocs.nic.in/mpimagemk/photo/5144.jpg").read())
			img_temp.flush()
		return filename,img_temp

	def load_candidate_data(self):
		super().load_parser()
		urls = self.find_all_urls()
		row = 0
		for url in urls:
			self.url = url
			super().load_parser()
			img = self.soup.find("img", attrs={"id": "ContentPlaceHolder1_Image1"})
			img_src = img['src']
			image_name,img_temp = self.download_image(img_src)
			all_detail = self.soup.find(
				"table", attrs={'id': 'ContentPlaceHolder1_Datagrid1'})
			table_data = all_detail.find('td')
			member = table_data.tr.find(
				'td', attrs={'class': 'gridheader1'}).text.strip().split(",")
			members_list = []
			if len(member) > 1:
				for i in range(0,len(member),2):
					members_list.append(member[i+1]+" "+ member[i])
					mp_name = members_list[0]
			else:
				m = ''
				mp_name = m.join(member)
			items = all_detail.find_all('td', attrs={'class': 'griditem2'})

			constituency = items[0].text.strip().split("(")[0]
			state = items[0].text.strip().rsplit("(")[-1].replace(")", "")

			party = items[1].text.strip()
			if '(' in party:
				party = party.split('(')[0].strip()
			else:
				party = party
			email = items[2].text.strip()
			email = ",".join(email.replace('AT','@').replace('DOT','.').replace('[','').replace(']','').split(" ")).replace(",,",",")
			More_detail = self.soup.find(
				"table", attrs={'id': 'ContentPlaceHolder1_DataGrid2'})
			more_items = More_detail.find_all('td', attrs={'class': 'griditem2'})
			dob = more_items[2].text.strip()
			education = more_items[9].text.strip()
			profession = more_items[10].text.strip()
			profession = profession.replace('\r', '').replace('\n', '')
			profession = " ".join(profession.split())

			try:
				permanent_address = more_items[12].text.strip(
				) + more_items[13].text.strip()

			except:
				permanent_address = 'Not Available '

			try:
				present_address = more_items[19].text.strip() + more_items[20].text.strip()
			except:
				present_address = 'Not Available'

			try:
				mobile = more_items[21].text.strip()
			except:
				mobile = 'Not Available'
			
			#print("Name : ", mp_name)
			#print("Source:",url)
			#print("Constituency : ", constituency)
			#print("State : ", state)
			#print("Party : ", party)
			#print("Email : ", email)
			#print("DOB : ", dob)
			#print("Education : ", education)
			#print("Profession : ", profession)
			#print("Permanent_address : ", permanent_address)
			#print("Present_address : ", present_address)
			#print("Mobile : ", mobile)
			data = []
			data.append(mp_name)
			data.append(constituency)
			data.append(state)
			data.append(party)
			data.append(email)
			data.append(dob)
			data.append(education)
			data.append(profession)
			data.append(permanent_address)
			data.append(present_address)
			data.append(mobile)
			data.append(image_name)
			data.append(url)
			data.append(img_temp)
			OpenGovParser.load_candidate_data(self,*data)
			OpenGovParser.load_candidature_data(self,*data)
			print(mp_name,"Added to the database")
		print("All the MP data are added")
			#row+=1
			#if(row == 50):
				#print("All the MP data are added")
				#break
				


#loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
#loksabha_parser.load_candidate_data()
