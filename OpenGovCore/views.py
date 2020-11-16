from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class Home(View):
    template_name = 'home.html'

    def get(self,request):
        return render(request,self.template_name)

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
        return render(request,self.template_name, {'members':data})


class MemberBySession(View):
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

    def get(self,request,house):
        party_name = request.GET["party"]

        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'

        party_obj = Parties.objects.get(acronym=party_name)
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
        return render(request,self.template_name, {'members':data,'check':party_name,'urlvar':'party'})

class MembersByState(View):
    template_name = "member_term.html"

    def get(self,request,house):
        state_name = request.GET["state"]

        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'

        state_obj = States.objects.get(name=state_name)
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
        return render(request,self.template_name, {'members':data,'check':state_name,'urlvar':'state'})


class MembersByConstituency(View):
    template_name = "member_term.html"

    def get(self,request,house):
        const_name = request.GET["constituency"]

        if house == 'Rajyasabha':
            self.template_name = 'rajyasabha_session.html'

        constit_obj = Parliamentary_Constituencies.objects.filter(name__contains=const_name)
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
        return render(request,self.template_name, {'members':data,'check':const_name,'urlvar':'constituency'})


class MemberInfo(View):
    template_name = "member.html"

    def get(self,request,house,name):
        candidate_obj = Candidate.objects.get(name=name)
        centrail_leg_id = Central_Legislatures.objects.get(name=house)
        candidature_obj = Candidature.objects.filter(candidate_id=candidate_obj)
        questions = Questions.objects.filter(candidate_id=candidate_obj)
        debates = Debates.objects.filter(candidate_id=candidate_obj)
        attendance = Attendance.objects.filter(candidate_id=candidate_obj)
        return render(request,self.template_name, {'members':candidature_obj[0],'questions':questions,
                'debates':debates, 'attendance':attendance,'house':house})


