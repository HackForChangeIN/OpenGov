from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .question_debate import ScrapeLokSabha

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
        #loksabha_parser.load_candidate_data()
        
        #url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_questions()
        #url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_debates()
        #url = "http://loksabhaph.nic.in/Legislation/NewAdvsearch.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_bills()
        url = "http://loksabhaph.nic.in/Members/memberwisetotal.aspx"
        sc = ScrapeLokSabha(url)
        sc.load_attendance()
        """count = 0
        while True:
            try:
                loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
                loksabha_parser.load_candidate_data()
                break
            except:
                count += 1
                if count == 4:
                    break
                else:
                    continue
        count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx")
                sc.load_questions()
                break
            except:
                count += 1
                if count == 4:
                    break
                else:
                    continue
        count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx")
                sc.load_debates()
                break
            except:
                count += 1
                if count == 4:
                    break
                else:
                    continue"""