from celery import shared_task
from django.conf import settings
from OpenGov.celery import app
from OpenGovCore.management.commands.loksabhaparser import LoksabhaParser
from OpenGovCore.management.commands.question_debate import ScrapeLokSabha
from OpenGovCore.management.commands.myneta import MyNetaParser
from OpenGovCore.management.commands.oldloksabhaparser import OldLoksabhaParser
from OpenGovCore.management.commands.rajyasabhaparser import RajyaSabhaParser

@shared_task(name = 'candidate_data_17th_term_loksabha')
def candidate_scrapper_17th_term():
    loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx",term ="17th")
    loksabha_parser.load_candidate_data()

@shared_task(name = 'bills_data')
def bills_data_scraper():
    url = "http://loksabhaph.nic.in/Legislation/NewAdvsearch.aspx"
    sc = ScrapeLokSabha(url,term="17th")
    sc.load_bills()

@shared_task(name = 'debates_data')
def debate_data_scraper():
    url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx"
    sc = ScrapeLokSabha(url,term="17th")
    sc.load_debates()

@shared_task(name = 'Question_data_17th_term')
def question_scrapper_17th_term():
    url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx"
    sc = ScrapeLokSabha(url,term ="17th")
    sc.load_questions()

@shared_task(name = 'Attendance_data_17th_term')
def attendance_data_scrapper_17th_term():
    url = "http://loksabhaph.nic.in/Members/SessionWiseAttn.aspx"
    sc = ScrapeLokSabha(url,term="17th")
    sc.load_attendance()

@shared_task(name = 'Asset_data_17th_term')
def asset_criminal_scrapper_17th_term():
    url = "https://myneta.info/LokSabha2019/index.php?action=show_winners&sort=default"
    myneta = MyNetaParser(url,term="17th")
    myneta.load_asset_criminal_cases()

@shared_task(name = 'Candidate_data_16th_and_15th_term')
def candidate_scrapper_16th_15th_term():
    url = "OpenGovCore/data/raw_data/old_loksabha_data.xlsx"
    oldmp = OldLoksabhaParser(url,term ="16th")
    oldmp.load_candidate_data()

@shared_task(name = 'Question_data_16th term')
def question_scrapper_16th_term():
    url = "http://loksabhaph.nic.in/Questions/qsearch15.aspx?lsno=16"
    sc = ScrapeLokSabha(url,term ="16th")
    sc.load_questions()

@shared_task(name = 'Debates_data_16th_term')
def debates_scrapper_16th_term():
    url = "http://loksabhaph.nic.in/Debates/DebateAdvSearch16.aspx"
    sc = ScrapeLokSabha(url,term ="16th")
    sc.load_debates()

@shared_task(name = 'Question_data_15th_term')
def question_scrapper_15th_term():
    url = "http://loksabhaph.nic.in/Questions/qsearch15.aspx?lsno=15"
    sc = ScrapeLokSabha(url,term ="15th")
    sc.load_questions()

@shared_task(name = 'Debate_data_15th_term')
def debate_scrapper_15th_term():
    url = "http://loksabhaph.nic.in/Debates/DebateAdvSearch15.aspx"
    sc = ScrapeLokSabha(url,term ="15th")
    sc.load_debates()

@shared_task(name = 'Rajyasabha_candidate_data')
def debate_scrapper_rajyasabha():
    url = "https://rajyasabha.nic.in/rsnew/member_site/memberlist.aspx"
    obj = RajyaSabhaParser(url ,term = "None")
    obj.load_candidate_data()

@shared_task(name = 'Rajyasabha_question_data')
def question_scrapper_rajyasabha():
    url = "https://rajyasabha.nic.in/rsnew/Questions/Search_SessionWise.aspx"
    obj = RajyaSabhaParser(url = url,term="None")
    obj.load_questions()




