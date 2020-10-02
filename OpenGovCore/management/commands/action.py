from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .question_debate import ScrapeLokSabha

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
        loksabha_parser.load_candidate_data()
        loksabha_parser.load_candidature_data()
        #url = "http://loksabhaph.nic.in/Questions/Qtextsearch.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_questions()
        #url = "http://loksabhaph.nic.in/Debates/Debatetextsearch16.aspx"
        #sc = ScrapeLokSabha(url)
        #sc.load_debates()