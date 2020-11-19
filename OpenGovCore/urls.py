from django.urls import path
from OpenGovCore.views import *
from django.conf.urls import include

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('members/',Members.as_view(),name='members'),
<<<<<<< HEAD
    path('members/<str:name>',MemberInfo.as_view(),name="member_name"),
    path('members/term/',MemebersLatTerm.as_view(),name='latest_term'),
    path('members/term/<str:term>',MemebersByTerm.as_view(),name='members_term'),
    path('members/house/',MembersHouse.as_view(), name="house"),
    path('members/house/<str:house>',MembersByHouse.as_view(),name="members_house"),
    path('members/party/',MembersByParty.as_view(),name="members_party"),
    path('members/state/',MembersByState.as_view(),name="members_state"),
    path('members/constituency/',MembersByConstituency.as_view(),name="members_const"),
    path('bills/',A_Bill.as_view()),
=======
    path('members/house/<house>/<name>/',MemberInfo.as_view(),name="member_name"),
    path('members/term/<term>/',MemebersByTerm.as_view(),name='members_term'),
    path('members/session/<session>/',MemberBySession.as_view(),name='members_session'),
    path('members/house/<house>/',MembersByHouse.as_view(),name="members_house"),
    path('members/house/<house>/party/',MembersByParty.as_view(),name="members_party"),
    path('members/house/<house>/state/',MembersByState.as_view(),name="members_state"),
    path('members/house/<house>/constituency/',MembersByConstituency.as_view(),name="members_const"),
    path('questions/',All_Questions.as_view(),name='all_questions'),
    path('questions/house/<house>/',QuestionsByHouse.as_view(),name='questions_house'),
    path('questions/year/<year>/',QuestionsByYear.as_view(),name='questions_year'),
    path('questions/type/<type>/',QuestionsByType.as_view(),name='questions_type'),
    path('questions/ministry/',QuestionsByMinistry.as_view(),name='questions_ministry'),
    path('questions/member/',QuestionsByMember.as_view(),name='questions_member'),
    path('debates/',All_Debates.as_view(),name='all_debates'),
    path('debates/year/<year>/',DebatesByYear.as_view(),name='debates_year'),
    path('debates/member/',DebatesByMember.as_view(),name='debates_member'),
    path('debates/type/',DebatesByType.as_view(),name='debates_type'),
    path('bills/',A_Bill.as_view()),
>>>>>>> origin/saurabh
]