from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .question_debate import ScrapeLokSabha
from .myneta import MyNetaParser

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
        #loksabha_parser.load_candidate_data()
        
        url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx"
        sc = ScrapeLokSabha(url)
        sc.load_questions()
        #url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_debates()
        url = "http://loksabhaph.nic.in/Legislation/NewAdvsearch.aspx"
        sc = ScrapeLokSabha(url)
        sc.load_bills()
        """url = "http://loksabhaph.nic.in/Members/SessionWiseAttn.aspx"
        sc = ScrapeLokSabha(url)
        sc.load_attendance()"""
        #myneta = MyNetaParser( url = "https://myneta.info/LokSabha2019/index.php?action=show_winners&sort=default")
        #myneta.load_asset_criminal_cases()
        """c_count = 0
        while True:
            try:
                loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
                loksabha_parser.load_candidate_data()
                break
            except:
                c_count += 1
                if c_count == 4:
                    break
                else:
                    continue
        q_count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx")
                sc.load_questions()
                break
            except:
                q_count += 1
                if q_count == 4:
                    break
                else:
                    continue
        d_count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx")
                sc.load_debates()
                break
            except:
                d_count += 1
                if d_count == 4:
                    break
                else:
                    continue
        a_count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Members/SessionWiseAttn.aspx")
                sc.load_attendance()
                break
            except:
                a_count += 1
                if a_count == 4:
                    break
                else:
                    continue
        b_count = 0
        while True:
            try:
                sc = ScrapeLokSabha(url = "http://loksabhaph.nic.in/Legislation/NewAdvsearch.aspx")
                sc.load_bills()
                break
            except:
                b_count += 1
                if b_count == 4:
                    break
                else:
                    continue"""