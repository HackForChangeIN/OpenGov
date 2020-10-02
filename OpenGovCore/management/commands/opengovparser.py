from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from OpenGovCore.models import States, Parliamentary_Constituencies, Parties, Candidate,Term,Candidature,Central_Legislatures,Questions,Debates

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
        mp_name,constituency,state,party,email,dob,education,profession,permanent_address,present_address,mobile,image_name= args
        try:
            candidate_obj = Candidate.objects.get(name__contains = mp_name)
            candidate_obj.name=mp_name
            candidate_obj.dob=dob
            candidate_obj.qualification=education
            candidate_obj.contact_number=mobile
            candidate_obj.email=email 
            candidate_obj.profession=profession 
            candidate_obj.present_address=present_address 
            candidate_obj.permanent_address=permanent_address
            candidate_obj.photo = image_name 
            candidate_obj.save()      
        except Candidate.DoesNotExist:
            candidate_obj = Candidate.objects.create(name=mp_name, dob=dob, qualification=education,
            contact_number=mobile, email=email, profession=profession, present_address=present_address, permanent_address=permanent_address,photo = image_name )

    
    def load_candidature_data(self,*args):
        mp_name,constituency,state,party,email,dob,education,profession,permanent_address,present_address,mobile,image_name= args
        try:
            state_obj = States.objects.get(name=state)
        except States.DoesNotExist:
            state_obj = States.objects.create(name = state) 
        try:
            constituency_obj = Parliamentary_Constituencies.objects.get(name=constituency,state = state_obj )
        except Parliamentary_Constituencies.DoesNotExist:
            constituency_obj = Parliamentary_Constituencies.objects.create(name = constituency,state = state_obj)

        try:
            party_obj = Parties.objects.get(party_name=party)
        except Parties.DoesNotExist:
            party_obj = Parties.objects.create(party_name=party)
        candidate_obj = Candidate.objects.get(name=mp_name, dob=dob)
        term = Term.objects.get(term_name = "17th")
        central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
        try:
            candidature_obj = Candidature.objects.update_or_create(candidate_id = candidate_obj,party_id = party_obj
            ,state_id = state_obj ,type = "MP",parliamentary_constituency_id = constituency_obj  ,term_id = term ,central_legislature_id = central_legislature)
        except Candidate.DoesNotExist:
            print("Candidate data not found")
    
    def load_questions(self,*args):
        date,category,candidates,subject,title,answer,link,type = args
        for candidate in candidates:
            print(candidate)
            try:
                candidate_id = Candidate.objects.get(name__contains = candidate)
            except Candidate.DoesNotExist:
                candidate_id = Candidate.objects.create(name=candidate)
            term = Term.objects.get(term_name = "17th")
            central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
            question_obj = Questions.objects.update_or_create(title = title,answer = answer,candidate_id = candidate_id, category = category,date =  date,subject = subject,term_id = term,central_legislature_id = central_legislature,link = link,type = type  )
        

    def load_debates(self,*args):
        title,type,date,candidates,link = args
        for candidate in candidates:
            print(candidate)
            try:
                candidate_id = Candidate.objects.get(name__contains = candidate)
            except Candidate.DoesNotExist:
                candidate_id = Candidate.objects.create(name=candidate)
            term = Term.objects.get(term_name = "17th")
            central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
            debate_obj = Debates.objects.update_or_create(title = title,type = type,candidate_id = candidate_id,date = date,link = link,term_id = term,central_legislature_id = central_legislature)
        


    def load_attendance(self):
        pass
    def load_bills(self):
        pass