import xlrd
from .opengovparser import OpenGovParser
import requests
import shutil
import os
import urllib
from django.conf import settings
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

class OldLoksabhaParser(OpenGovParser):
	def load_candidate_data(self):
		workbook = xlrd.open_workbook(self.url)
		for sheet in workbook.sheets():
			for row in range(1, sheet.nrows):
				candidate_name = sheet.cell_value(row, 0)
				party = sheet.cell_value(row, 1)
				constituency = sheet.cell_value(row, 2)
				state = sheet.cell_value(row, 3)
				term = int(sheet.cell_value(row, 4))
				image_src = sheet.cell_value(row, 5)
				education = sheet.cell_value(row, 6)
				permanent_address = sheet.cell_value(row, 8)
				email = sheet.cell_value(row, 9)
				criminal_cases = sheet.cell_value(row, 10)
				assests = sheet.cell_value(row, 11)
				liabilities = sheet.cell_value(row, 12)
				#print(candidate_name,party,constituency,state,term,image_url,education,permanent_address,email,criminal_cases,assests,liabilities)
				filename,img = self.download_image(image_src,row,term)
				#print(filename)
				if term == 16:
					source = "https://myneta.info/ls2014/index.php?action=show_winners&sort=default"
				if term == 15:
					source = "https://myneta.info/ls2009/index.php?action=show_winners&sort=default"
				#print(candidate_name,party,constituency,state,term,image_src,education,permanent_address,email,criminal_cases,assests,liabilities,source)
				data = [candidate_name,constituency,state,party,email,education,permanent_address,filename,img,term,criminal_cases,assests,liabilities,source]
				OpenGovParser.load_old_candidate_data(self,*data)
				print(candidate_name, "is added")
			print("All data added")




	def download_image( self,img_src,row,term):
		filename = str(term)+"_"+str(row)+'.jpg'
		img_temp = NamedTemporaryFile(delete=True)
		try:
			img_temp.write(urlopen(img_src).read())
			img_temp.flush()
		except:
			img_temp.write(urlopen("https://via.placeholder.com/150").read())
			img_temp.flush()
		return filename,img_temp			

