from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from OpenGovCore.models import States, Parliamentary_Constituencies, Parties, Candidate,Term,Candidature,Central_Legislatures

class OpenGovParser:

    url = ''

    def __init__(self, url, soup=None):
        self.url = url
        self.soup = soup

    def load_parser(self):
        Client = uReq(self.url)
        content = Client.read()
        self.soup = bs(content, "html.parser")
        return self.soup

    def load_candidate_data(self, *args):
        mp_name = args[0]
        constituency = args[1]
        state = args[2]
        party = args[3]
        email = args[4]
        dob = args[5]
        education = args[6]
        profession = args[7]
        permanent_address = args[8]
        present_address = args[9]
        mobile = args[10]
        image_name = args[11]
        state_obj = States.objects.get(name=state)
        constituency_obj = Parliamentary_Constituencies.objects.get(
            name=constituency)
        try:
            party_obj = Parties.objects.get(party_name=party)
        except Parties.DoesNotExist:
            party_obj = Parties.objects.create(party_name=party)
        candidate_obj = Candidate.objects.update_or_create(name=mp_name, dob=dob, qualification=education,
        contact_number=mobile, email=email, profession=profession, present_address=present_address, permanent_address=permanent_address,photo = image_name )
        
        try:
            candidate_obj = Candidate.objects.get(name=mp_name, dob=dob)
            term = Term.objects.get(term_name = "17th")
            central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
            candidature_obj = Candidature.objects.update_or_create(candidate_id = candidate_obj,party_id = party_obj
            ,state_id = state_obj ,type = "MP",parliamentary_constituency_id = constituency_obj  ,term_id = term ,central_legislature_id = central_legislature,
            )
        except Candidate.DoesNotExist:
            print("Candidate data not found")
        






    def load_questions(self):
        pass

    def load_bills(self):
        pass

    def load_debates(self):
        pass

    def load_attendance(self):
        pass
