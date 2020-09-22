from opengovparser import OpenGovParser
class LoksabhaParser(OpenGovParser):
    def load_candidate_data(self):
        pass

    def load_questions(self):
        pass


loksabha_parser = LoksabhaParser(
    url="http://loksabhaph.nic.in/Members/AlphabeticalList.aspx")
loksabha_parser.load_candidate_data()
