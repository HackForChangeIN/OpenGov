from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

class OpenGovParser:

    url = ''
    def __init__(self, url,soup=None):
        self.url = url
        self.soup = soup

    def load_parser(self):
        Client = uReq(self.url)
        content = Client.read()
        self.soup = bs(content, "html.parser")
        return self.soup

    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass

    def load_bills(self):
        pass

    def load_debates(self):
        pass

    def load_attendance(self):
        pass
