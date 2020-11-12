from django.urls import path
from OpenGovCore.views import *
from django.conf.urls import include

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('members/',Members.as_view(),name='members'),
    path('members/<name>',MemberInfo.as_view(),name="member_name"),
    path('members/term/',MemebersLatTerm.as_view(),name='latest_term'),
    path('members/term/<term>',MemebersByTerm.as_view(),name='members_term'),
    path('members/house/',MembersHouse.as_view(), name="house"),
    path('members/house/<house>',MembersByHouse.as_view(),name="members_house"),
    path('members/party/',MembersByParty.as_view(),name="members_party"),
    path('members/state/',MembersByState.as_view(),name="members_state"),
    path('members/constituency/',MembersByConstituency.as_view(),name="members_const"),
]