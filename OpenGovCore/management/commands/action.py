from django.core.management.base import BaseCommand
from .loksabhaparser import LoksabhaParser
from .opengovparser import OpenGovParser

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        loksabha_parser = LoksabhaParser(url = "http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
        loksabha_parser.load_candidate_data()