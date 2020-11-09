from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

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
        

class MemebersLatTerm(View):
    template_name = 'member_term.html'

    def get(self,request):
        term_id = Term.objects.get(term_name = "17th")
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


class MembersHouse(View):
    template_name = "member_term.html"

    def get(self,request):
        central_legislature = Central_Legislatures.objects.get(name = "Loksabha")
        term_id = Term.objects.filter(central_legislature_id = central_legislature)
        data = Candidature.objects.filter(term_id=term_id[0])
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
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
        central_legislature = Central_Legislatures.objects.get(name = house)
        term_id = Term.objects.filter(central_legislature_id = central_legislature)
        data = Candidature.objects.filter(term_id=term_id[0])
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

    def get(self,request):
        party_name = request.GET["party"]
        party_obj = Parties.objects.get(acronym=party_name)
        data = Candidature.objects.filter(party_id=party_obj)
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data})

class MembersByState(View):
    template_name = "member_term.html"

    def get(self,request):
        state_name = request.GET["state"]
        state_obj = States.objects.get(name=state_name)
        data = Candidature.objects.filter(state_id=state_obj)
        page = request.GET.get('page',1)
        paginator = Paginator(data,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return render(request,self.template_name, {'members':data})


class MembersByConstituency(View):
    template_name = "member_term.html"

    def get(self,request):
        const_name = request.GET["constituency"]
        constit_obj = Parliamentary_Constituencies.objects.filter(name__contains=const_name)
        data = []
        for i in constit_obj:
            data1 = Candidature.objects.filter(parliamentary_constituency_id=i)
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
        return render(request,self.template_name, {'members':data})


