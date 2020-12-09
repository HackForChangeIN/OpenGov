from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gnewsclient import gnewsclient

# Create your views here.

class Home(View):
    template_name = 'home.html'

    def get(self,request):
        latest_bills = Bills.objects.filter(status='Passed').order_by('-date_of_introduction')[:5]
        latest_ques = Questions.objects.all().order_by('-date')[:5]
        latest_deb = Debates.objects.all().order_by('-date')[:5]
        return render(request,self.template_name,{'lat_bills':latest_bills,'lat_ques':latest_ques,'lat_deb':latest_deb})

class Members(View):
    template_name = 'members_data.html'
    def get(self,request):
        candidate_data = Candidate.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(candidate_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data})
        


class MemebersByTerm(View):
    template_name = 'member_term.html'

    def get(self,request,term):
        term_id = Term.objects.get(term_name = term)
        candidate_data = Candidature.objects.filter(term_id=term_id)
        page = request.GET.get('page',1)
        paginator = Paginator(candidate_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data,'term_id':term_id})


class MembersBySession(View):
    template_name = 'rajyasabha_session.html'

    def get(self,request,session):
        session_id = Parliamentary_Sessions.objects.get(type=session)
        attendance = Attendance.objects.filter(session_id=session_id)
        cand_data = []
        for i in attendance:
            candidate_data = Candidature.objects.filter(candidate_id=i.candidate_id)
            cand_data.append(i)

        page = request.GET.get('page',1)
        paginator = Paginator(cand_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data})



class MembersByHouse(View):
    template_name = "member_term.html"

    def get(self,request,house):
        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'
        
        central_legislature = Central_Legislatures.objects.get(name = house)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        data = Candidature.objects.filter(central_legislature_id=centrail_leg_id)
            
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data})

class MembersByParty(View):
    template_name = "member_term.html"

    def get(self,request,house,party):
        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'
        party_obj = Parties.objects.get(party_name=party)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        data = Candidature.objects.filter(party_id=party_obj, central_legislature_id=centrail_leg_id)
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data,'check':party,'urlvar':'party','party':party_obj})

class MembersByState(View):
    template_name = "member_term.html"

    def get(self,request,house,state):
        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'

        state_obj = States.objects.get(name=state)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        data = Candidature.objects.filter(state_id=state_obj,central_legislature_id=centrail_leg_id)
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data,'check':state,'urlvar':'state'})


class MembersByConstituency(View):
    template_name = "member_term.html"

    def get(self,request,house,constituency):
        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'

        constit_obj = Parliamentary_Constituencies.objects.filter(name=constituency)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        data = []
        for i in constit_obj:
            data1 = Candidature.objects.filter(parliamentary_constituency_id=i,central_legislature_id=centrail_leg_id)
            for j in data1:
                data.append(j)

        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data,'check':constituency,'urlvar':'constituency'})


class MemberInfo(View):
    template_name = "member.html"

    def get(self,request,house,name):
        client = gnewsclient.NewsClient(language='english', location='india', topic=name, max_results=3)
        news = {}
        news = (client.get_news())
        getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]
        g_news_title  = getValues('title', news)
        g_news_links  = getValues('link', news)

        candidate_obj = Candidate.objects.get(name=name)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        candidature_obj = Candidature.objects.filter(candidate_id=candidate_obj)
        attendance = Attendance.objects.filter(candidate_id=candidate_obj)
        return render(request,self.template_name, {'members':candidature_obj[0],'attendance':attendance,'house':house,
                        'g_news_title':g_news_title,'g_news_links':g_news_links})

class MemberDetail(View):
    template_name = "member.html"

    def get(self,request,member):
        candidate_obj = Candidate.objects.get(name=member)
        candidature_obj = Candidature.objects.filter(candidate_id=candidate_obj)
        attendance = Attendance.objects.filter(candidate_id=candidate_obj)
        house = candidature_obj[0].central_legislature_id
        return render(request,self.template_name, {'members':candidature_obj[0],'attendance':attendance,'house':house})

# Questions
class All_Questions(View):
    template_name = 'questions.html'

    def get(self,request):
        all_ques = Questions.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(all_ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data})

class QuestionDetail(View):
    template_name = 'questions_details.html'

    def get(self,request,member,date):
        cand_obj = Candidate.objects.get(name=member)
        data = Questions.objects.filter(candidate_id=cand_obj,date=date)
        participants = Questions.objects.filter(subject=data[0].subject)
        return render(request,self.template_name, {'questions':data[0],"particip":participants})

class QuestionsByHouse(View):
    template_name = 'questions.html'

    def get(self,request,house):
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        ques = Questions.objects.filter(central_legislature_id=centrail_leg_id)
        page = request.GET.get('page',1)
        paginator = Paginator(ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data})


class QuestionsByYear(View):
    template_name = 'questions.html'

    def get(self,request,year):
        ques = Questions.objects.filter(date__year=year)
        page = request.GET.get('page',1)
        paginator = Paginator(ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data,'check':year,'urlvar':'year'})


class QuestionsByType(View):
    template_name = 'questions.html'

    def get(self,request,type):
        ques = Questions.objects.filter(type=type)
        page = request.GET.get('page',1)
        paginator = Paginator(ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data,'check':type,'urlvar':'type','type':type})
        

class QuestionsByMinistry(View):
    template_name = 'questions_ministry.html'

    def get(self,request,ministry):
        ques = Questions.objects.filter(category=ministry)
        page = request.GET.get('page',1)
        paginator = Paginator(ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data,'check':ministry,'urlvar':'ministry'})


class QuestionsByMember(View):
    template_name = 'questions_mem_card.html'

    def get(self,request,member):
        c_id = Candidate.objects.get(name=member)
        candidature_obj = Candidature.objects.filter(candidate_id=c_id)
        if candidature_obj.count() >= 1:
            candidature_obj = candidature_obj[0]
        ques = Questions.objects.filter(candidate_id=c_id)
        ques_count = ques.count()
        page = request.GET.get('page',1)
        paginator = Paginator(ques,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'questions':data,'check':member,'urlvar':'member',
                     'member':candidature_obj, 'ques_count':ques_count})


# Debates
class All_Debates(View):
    template_name = 'debates.html'

    def get(self,request):
        deb = Debates.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(deb,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'debates':data})


class DebatesByType(View):
    template_name = 'debates_type.html'

    def get(self,request,type):
        deb = Debates.objects.filter(type=type)
        page = request.GET.get('page',1)
        paginator = Paginator(deb,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'debates':data,'check':type,'urlvar':'type'})


class DebatesByMember(View):
    template_name = 'debates_mem_card.html'

    def get(self,request,member):
        c_id = Candidate.objects.get(name=member)
        candidature_obj = Candidature.objects.filter(candidate_id=c_id)
        if candidature_obj.count() >= 1:
            candidature_obj = candidature_obj[0]
        deb = Debates.objects.filter(candidate_id=c_id)
        deb_count = deb.count()
        page = request.GET.get('page',1)
        paginator = Paginator(deb,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'debates':data,'check':member,'urlvar':'member',
                        'member':candidature_obj,'deb_count':deb_count})

class DebatesByYear(View):
    template_name = 'debates.html'

    def get(self,request,year):
        deb = Debates.objects.filter(date__year=year)
        page = request.GET.get('page',1)
        paginator = Paginator(deb,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'debates':data,'check':year,'urlvar':'year'})

class DebatesByHouse(View):
    template_name = 'debates.html'

    def get(self,request,house):
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        deb = Debates.objects.filter(central_legislature_id=centrail_leg_id)
        page = request.GET.get('page',1)
        paginator = Paginator(deb,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'debates':data})


#Bills
class A_Bill(View):
    template_name = "bills.html"

    def get(self, request):
        bills_data = Bills.objects.all()
        latest_bills = Bills.objects.filter(status='Passed').order_by('-date_of_introduction')[:5]
        page = request.GET.get('page',1)
        paginator = Paginator(bills_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'bills':data,'latest_bills':latest_bills})
    

class BillsByYear(View):
    template_name = "bills.html"

    def get(self,request,year):
        bills_data = Bills.objects.filter(date_of_introduction__year=year)
        page = request.GET.get('page',1)
        paginator = Paginator(bills_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'bills':data,'check':year,'urlvar':'year'})


class BillsByType(View):
    template_name = "bills.html"

    def get(self,request,type):
        bills_data = Bills.objects.filter(type=type)
        page = request.GET.get('page',1)
        paginator = Paginator(bills_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'bills':data,'check':type,'urlvar':'type'})


class BillsByStatus(View):
    template_name = "bills.html"

    def get(self,request,status):
        bills_data = Bills.objects.filter(status=status)
        page = request.GET.get('page',1)
        paginator = Paginator(bills_data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'bills':data,'check':status,'urlvar':'status'})
