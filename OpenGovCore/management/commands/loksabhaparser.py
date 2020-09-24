from .opengovparser import OpenGovParser
import requests
import shutil

class LoksabhaParser(OpenGovParser):

	def load_questions(self):
		pass

	def find_all_urls(self):
		all_class=self.soup.find("div",attrs = {'id':'divPrint'}).find_all('a')
		urls = []
		for a_tag in all_class:
			url = a_tag['href']
			if not url.startswith('http'):
				url = "http://loksabhaph.nic.in/Members/" + url
				urls.append(url)
		unique_urls = list(dict.fromkeys(urls))
		return unique_urls

	def download_image(self,img_src):
		response = requests.get(img_src, stream=True)
		filename = img_src.rsplit("/")[-1]
		file = open("media/{}".format(filename), 'wb')
		response.raw.decode_content = True
		shutil.copyfileobj(response.raw, file)
		del response
		return filename

	def load_candidate_data(self):
		super().load_parser()
		urls = self.find_all_urls()
		row = 0
		for url in urls:
			self.url = url
			super().load_parser()
			img = self.soup.find("img", attrs={"id":"ContentPlaceHolder1_Image1"})
			img_src=img['src']
			image_name = self.download_image(img_src)

			all_detail = self.soup.find("table",attrs = {'id':'ContentPlaceHolder1_Datagrid1'})
			table_data = all_detail.find('td')
			mp_name = table_data.tr.find('td',attrs = {'class':'gridheader1'}).text.strip()
			items = all_detail.find_all('td',attrs = {'class':'griditem2'})

			constituency = items[0].text.strip().split(" ")[0]
			state = items[0].text.strip().rsplit("(")[-1].replace(")","")

			party = items[1].text.strip()
			if '(' in party:
				party = party.split('(')[0].strip()
			else:
				party = party
			email = items[2].text.strip()
			email = email.replace('AT','@').replace('DOT','.').replace('[','').replace(']','')
			
			More_detail = self.soup.find("table",attrs = {'id':'ContentPlaceHolder1_DataGrid2'})
			more_items = More_detail.find_all('td',attrs = {'class':'griditem2'})
			
			dob = more_items[2].text.strip()
			education = more_items[9].text.strip()

			profession = more_items[10].text.strip()
			profession = profession.replace('\r','').replace('\n','')
			profession = " ".join(profession.split())

			try:
				permanent_address = more_items[12].text.strip() + more_items[13].text.strip()
			
			except:
				permanent_address='Not Available '

			try:
				present_address=more_items[19].text.strip() + more_items[20].text.strip()
			except:
				present_address='Not Available'

			try:
				mobile=more_items[21].text.strip()
			except:
				mobile='Not Available'

			row+=1
			if(row == 6):
				break

			print("Name : ", mp_name)
			print("Constituency : ",constituency)
			print("State : ",state)
			print("Party : ", party)
			print("Email : ", email)
			print("DOB : ", dob)
			print("Education : ", education)
			print("Profession : ", profession)
			print("Permanent_address : ", permanent_address)
			print("Present_address : ", present_address)
			print("Mobile : ", mobile)
			data = []
			data.append(mp_name)
			data.append(constituency)
			data.append(state)
			data.append(party)
			data.append(email)
			data.append(dob)
			data.append(education)
			data.append( profession)
			data.append(permanent_address)
			data.append(present_address)
			data.append(mobile)
			data.append(image_name)
			OpenGovParser.load_candidate_data(self,*data)
    	

#loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
#loksabha_parser.load_candidate_data()
