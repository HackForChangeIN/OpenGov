from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .question_debate import ScrapeLokSabha
from .myneta import MyNetaParser
from .oldloksabhaparser import OldLoksabhaParser
from .rajyasabhaparser import RajyaSabhaParser

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #17th term
        #loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx",term ="17th")
        #loksabha_parser.load_candidate_data()
        
        #url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx"
        #sc = ScrapeLokSabha(url,term ="17th")
        #sc.load_questions()

        #url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx"
        #sc = ScrapeLokSabha(url,term="17th")
        #sc.load_debates()

        #url = "http://loksabhaph.nic.in/Legislation/NewAdvsearch.aspx"
        #sc = ScrapeLokSabha(url,term="17th")
        #sc.load_bills()
        
        #url = "http://loksabhaph.nic.in/Members/SessionWiseAttn.aspx"
        #sc = ScrapeLokSabha(url,term="15th")
        #sc.load_attendance()
        
        #myneta = MyNetaParser( url = "https://myneta.info/LokSabha2019/index.php?action=show_winners&sort=default",term="17th")
        #myneta.load_asset_criminal_cases()
        
        #16th term #####

        #oldmp = OldLoksabhaParser(url = "OpenGovCore/data/raw_data/old_loksabha_data.xlsx",term ="16th")
        #oldmp.load_candidate_data()

        #url = "http://loksabhaph.nic.in/Questions/qsearch15.aspx?lsno=16"
        #sc = ScrapeLokSabha(url,term ="16th")
        #sc.load_questions()
        
        #url = "http://loksabhaph.nic.in/Debates/DebateAdvSearch16.aspx"
        #sc = ScrapeLokSabha(url,term ="16th")
        #sc.load_debates()

        ## 15th term#######
        #url = "http://loksabhaph.nic.in/Questions/qsearch15.aspx?lsno=15"
        #sc = ScrapeLokSabha(url,term ="15th")
        #sc.load_questions()
        
        #url = "http://loksabhaph.nic.in/Debates/DebateAdvSearch15.aspx"
        #sc = ScrapeLokSabha(url,term ="15th")
        #sc.load_debates()

        ##### Rajyasabha ###################
        #url = "https://rajyasabha.nic.in/rsnew/member_site/memberlist.aspx"
        #obj = RajyaSabhaParser(url ,term = "None")
        #obj.load_candidate_data()

        url = "https://rajyasabha.nic.in/rsnew/Questions/Search_SessionWise.aspx"
        obj = RajyaSabhaParser(url = url,term="None")
        obj.load_questions()

        '''url = "https://rajyasabha.nic.in/rsnew/member_site/sessionwiseresults.aspx?vsessionno=252"
        obj = RajyaSabhaParser(url = url,term ="None")
        obj.load_attendance()'''
        
        """url = "https://rajyasabha.nic.in/rsnew/member_site/newsessionwise_attendance.aspx"
        obj = RajyaSabhaParser(url = url,term =None)
        obj.load_attendance()"""

       
        
      
        
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