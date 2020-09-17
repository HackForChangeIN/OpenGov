class OpenGovParser:
    url = ''

    def __init__(self, url):
        self.url = url

    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass

    def load_bills(self):
        pass


class LoksabhaParser(OpenGovParser):
    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass


class PRSIndiaParser(OpenGovParser):
    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass


class MynetaParser(OpenGovParser):
    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass


loksabha_parser = LoksabhaParser(
    url="http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
loksabha_parser.load_candidate_data()
