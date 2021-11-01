from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin


class StateAdmin(VersionAdmin):
    list_display = ('name',)

    class meta:
        model = States


admin.site.register(States, StateAdmin)


class Parliamentary_Constituencies_Admin(VersionAdmin):
    list_display = ('name', 'constituency_number', 'state')

    class meta:
        model = Parliamentary_Constituencies


admin.site.register(Parliamentary_Constituencies,
                    Parliamentary_Constituencies_Admin)


class Assembly_Constituencies_Admin(VersionAdmin):
    list_display = ('name', 'constituency_number', 'state')

    class meta:
        model = Assembly_Constituencies


admin.site.register(Assembly_Constituencies, Assembly_Constituencies_Admin)


class Parties_Admin(VersionAdmin):
    list_display = ('acronym','party_name',  'type', 'founded',
                    'founder_name', 'president_name', 'website', 'symbol')

    class meta:
        model = Parties


admin.site.register(Parties, Parties_Admin)


class Central_Legislatures_Admin(VersionAdmin):
    list_display = ('name', 'type')

    class meta:
        model = Central_Legislatures


admin.site.register(Central_Legislatures, Central_Legislatures_Admin)


class State_Legislatures_Admin(VersionAdmin):
    list_display = ('name', 'type', 'state_id')

    class meta:
        model = State_Legislatures


admin.site.register(State_Legislatures, State_Legislatures_Admin)


class Term_Admin(VersionAdmin):
    list_display = ('term_name', 'start_year',
                    'end_year', 'central_legislature_id')

    class meta:
        model = Term


admin.site.register(Term, Term_Admin)


class Sittings_Admin(VersionAdmin):
    list_display = ('sitting_name', 'start_year',
                    'end_year', 'state_legislature_id')

    class meta:
        model = Sittings


admin.site.register(Sittings, Sittings_Admin)


class Candidate_Admin(VersionAdmin):
    list_display = ('name', 'dob', 'qualification', 'gender', 'contact_number', 'email',
                    'profession', 'criminal_cases', 'present_address', 'permanent_address','total_assets','total_liabilities', 'photo','source','name_slug')
    search_fields = ['name',]
    class meta:
        model = Candidate


admin.site.register(Candidate, Candidate_Admin)


class Candidature_Admin(VersionAdmin):
    list_display = ('candidate_id', 'party_id', 'state_id', 'type',
                    'parliamentary_constituency_id', 'term_id', 'central_legislature_id')
    search_fields = ['candidate_id__name','party_id__acronym','state_id__name','parliamentary_constituency_id__name','term_id__term_name']
    
    class meta:
        model = Candidature


admin.site.register(Candidature, Candidature_Admin)


class Parliamentary_Sessions_Admin(VersionAdmin):
    list_display = ('type', 'term_id', 'start_date',
                    'end_date', 'central_legislature_id')

    class meta:
        model = Parliamentary_Sessions


admin.site.register(Parliamentary_Sessions, Parliamentary_Sessions_Admin)


class Assembly_Sessions_Admin(VersionAdmin):
    list_display = ('type', 'sitting_id', 'start_date',
                    'end_date', 'state_legislature_id')

    class meta:
        model = Assembly_Sessions


admin.site.register(Assembly_Sessions, Assembly_Sessions_Admin)


class Question_Admin(VersionAdmin):
    list_display = ('title', 'type', 'candidate_id', 'category', 'date', 'subject',
                    'term_id', 'parliamentary_session_id', 'central_legislature_id','source')

    class meta:
        model = Questions


admin.site.register(Questions, Question_Admin)

class Debate_Admin(VersionAdmin):
    list_display = ('title','type','candidate_id','central_legislature_id','term_id','date','source')

    class meta:
        model = Debates

admin.site.register(Debates,Debate_Admin)

class Bill_Admin(VersionAdmin):
    list_display = ('title','type','status','candidate_id','date_of_introduction','debate_loksabha_date','debate_rajyasabha_date','term_id','central_legislature_id','source')

    class meta:
        model = Bills
admin.site.register(Bills,Bill_Admin)

class Attendance_Admin(VersionAdmin):
    list_display = ('candidate_id','term_id','session_id','attendance_signed_days','source')

    class meta:
        model = Attendance
admin.site.register(Attendance,Attendance_Admin)
