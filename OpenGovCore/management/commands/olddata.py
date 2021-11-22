from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .question_debate import ScrapeLokSabha
from .myneta import MyNetaParser
from .oldloksabhaparser import OldLoksabhaParser
from .bills_details import bills_details_scraper
from .opengovparser import OpenGovParser

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #16 th term Loksabha
        #url = "http://loksabhaph.nic.in/Members/lokaralpha.aspx?lsno=16&tab=0"
        #lok = OldLoksabhaParser(url="./OpenGovCore/data/raw_data/old_loksabha_data.xlsx", term = "16")
        #lok.load_candidate_data()
        #15 th
        #url = "http://loksabhaph.nic.in/Members/lokaralpha.aspx?lsno=15&tab=1"
        #lok = OldLoksabhaParser(url=url)
        #lok.load_data()
        #pdf_text = bills_details_scraper()
        #print(pdf_text)
        OpenGovParser.load_bills_details(self)
