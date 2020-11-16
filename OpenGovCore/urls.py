from django.urls import path
from OpenGovCore.views import *
from django.conf.urls import include

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('members/',Members.as_view(),name='members'),
    path('members/house/<house>/<name>',MemberInfo.as_view(),name="member_name"),
    path('members/term/<term>',MemebersByTerm.as_view(),name='members_term'),
    path('members/session/<session>',MemberBySession.as_view(),name='members_session'),
    path('members/house/<house>',MembersByHouse.as_view(),name="members_house"),
    path('members/house/<house>/party/',MembersByParty.as_view(),name="members_party"),
    path('members/house/<house>/state/',MembersByState.as_view(),name="members_state"),
    path('members/house/<house>/constituency/',MembersByConstituency.as_view(),name="members_const"),
]