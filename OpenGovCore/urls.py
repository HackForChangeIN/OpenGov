from django.urls import path
from OpenGovCore.views import *
from django.conf.urls import include

urlpatterns = [
    path('members/',Members.as_view(),name='members'),
    path('members/<str:name>',MemberInfo.as_view(),name="member_name"),
    path('members/term/',MemebersLatTerm.as_view(),name='latest_term'),
    path('members/term/<str:term>',MemebersByTerm.as_view(),name='members_term'),
    path('members/house/',MembersHouse.as_view(), name="house"),
    path('members/house/<str:house>',MembersByHouse.as_view(),name="members_house"),
    path('members/party/',MembersByParty.as_view(),name="members_party"),
    path('members/state/',MembersByState.as_view(),name="members_state"),
    path('members/constituency/',MembersByConstituency.as_view(),name="members_const"),
]