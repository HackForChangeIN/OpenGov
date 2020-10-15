from urllib.request import urlopen as uReq
from .opengovparser import OpenGovParser
from bs4 import BeautifulSoup as bs
from time import sleep, time


class MyNetaParser(OpenGovParser):
    def load_asset_criminal_cases(self):
        html_page = super().load_parser()
        rows = html_page.find_all("table")[2].find_all("tr")[2:]
        for row in rows:
            member_name = row.find_all("td")[1].text.strip()
            constituency = row.find_all("td")[2].text.strip().title()
            party = row.find_all("td")[3].text.strip()
            criminal_cases = row.find_all("td")[4].text.strip()
            total_assets = row.find_all("td")[6].text.strip()
            liabilities = row.find_all("td")[7].text.strip()
            print("Member Name : ",member_name)
            print("Constituency : ",constituency)
            print("Party : ",party)
            print("Criminal Cases : ",criminal_cases)
            print("Total Assets : ",total_assets)
            print("Liabilities : ",liabilities)
            data = [member_name,constituency,criminal_cases,total_assets,liabilities]
            OpenGovParser.load_asset_criminal_cases(self,*data)
            print(member_name,"asset and case added")
        print("All members data added")



			



