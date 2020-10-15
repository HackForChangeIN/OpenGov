from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from django.core.files import File
from OpenGovCore.models import States, Parliamentary_Constituencies, Parties, Candidate,Term,Candidature,Central_Legislatures,Questions,Debates,Bills,Parliamentary_Sessions,Attendance

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
        mp_name,constituency,state,party,email,dob,education,profession,permanent_address,present_address,mobile,image_name,url,img_temp = args
        try:
            #state_obj = States.objects.get(name=state)
            #constituency_obj = Parliamentary_Constituencies.objects.get(name=constituency,state = state_obj )
            #candidature_obj = Candidature.objects.get(parliamentary_constituency_id = constituency_obj)
            #candidate_name = candidature_obj.name
            #if mp_name == candidate_name:
            candidate_obj = Candidate.objects.get(name = mp_name)
            candidate_obj.name = mp_name
            candidate_obj.dob = dob
            candidate_obj.qualification = education
            candidate_obj.contact_number = mobile
            candidate_obj.email = email
            candidate_obj.profession = profession
            candidate_obj.present_address = present_address
            candidate_obj.permanent_address = permanent_address
            candidate_obj.source = url
            if candidate_obj.photo != image_name:
                candidate_obj.photo.save(image_name,File(img_temp))
            else:
                print("candidate photo name",candidate_obj.photo," Not Updated")
            candidate_obj.save()
            """else:
                candidate_obj = Candidate.objects.create(name=mp_name, dob=dob, qualification=education,
                contact_number=mobile, email=email, profession=profession, present_address=present_address, permanent_address=permanent_address,source = url )
                candidate_obj.photo.save(image_name,File(img_temp))"""
        except Candidate.DoesNotExist:
            candidate_obj = Candidate.objects.create(name=mp_name, dob=dob, qualification=education,
            contact_number=mobile, email=email, profession=profession, present_address=present_address, permanent_address=permanent_address,source = url )
            candidate_obj.photo.save(image_name,File(img_temp))
            

    
    def load_candidature_data(self,*args):
        mp_name,constituency,state,party,email,dob,education,profession,permanent_address,present_address,mobile,image_name,url,img_temp= args
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
                candidate_id = Candidate.objects.get(name = candidate)
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
                candidate_id = Candidate.objects.get(name = candidate)
            except Candidate.DoesNotExist:
                candidate_id = Candidate.objects.create(name=candidate)
            term = Term.objects.get(term_name = "17th")
            central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
            debate_obj = Debates.objects.update_or_create(title = title,type = type,candidate_id = candidate_id,date = date,link = link,term_id = term,central_legislature_id = central_legislature)
    def load_bills(self,*args):
        title,type,status,date_of_introduction,debate_loksabha_date,debate_rajyasabha_date,source = args
        bill_obj = Bills.objects.update_or_create(title = title,type = type,status = status,date_of_introduction = date_of_introduction,
        debate_loksabha_date = debate_loksabha_date,debate_rajyasabha_date = debate_rajyasabha_date,source = source)




    def load_attendance(self,*args):
        session,candidate,constituency,attendance_signed_days = args
        try:
            constituency_obj = Parliamentary_Constituencies.objects.get(name = constituency )
            candidature_obj = Candidature.objects.get(parliamentary_constituency_id = constituency_obj )
            candidate_obj = candidature_obj.candidate_id
        except:
            print("Constituency name",constituency,"is not in Database")
            candidate_obj =Candidate.objects.get(name__contains = candidate)
        term = Term.objects.get(term_name = "17th")
        try:
            session_id = Parliamentary_Sessions.objects.get(type = session)
            attendance_obj = Attendance.objects.update_or_create(candidate_id = candidate_obj,term_id= term,session_id= session_id,attendance_signed_days=attendance_signed_days)
        except:
            session_id = Parliamentary_Sessions.objects.create(type = session,term_id = term)
            attendance_obj = Attendance.objects.create(candidate_id = candidate_obj,term_id= term,session_id= session_id,attendance_signed_days=attendance_signed_days)


        
        
    