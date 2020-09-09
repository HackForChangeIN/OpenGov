from django.contrib import admin
from .models import *


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class meta:
        model = States


admin.site.register(States, StateAdmin)


class Parliamentary_Constituencies_Admin(admin.ModelAdmin):
    list_display = ('name', 'constituency_number', 'state')

    class meta:
        model = Parliamentary_Constituencies


admin.site.register(Parliamentary_Constituencies,
                    Parliamentary_Constituencies_Admin)


class Assembly_Constituencies_Admin(admin.ModelAdmin):
    list_display = ('name', 'constituency_number', 'state')

    class meta:
        model = Assembly_Constituencies


admin.site.register(Assembly_Constituencies, Assembly_Constituencies_Admin)

class Parties_Admin(admin.ModelAdmin):
    list_display = ('party_name','acronym','type','founded','founder_name','president_name','website','symbol')

    class meta:
        model = Parties

admin.site.register(Parties,Parties_Admin)

class Central_Legislatures_Admin(admin.ModelAdmin):
    list_display = ('name','type')

    class meta:
        model = Central_Legislatures

admin.site.register(Central_Legislatures,Central_Legislatures_Admin)

class State_Legislatures_Admin(admin.ModelAdmin):
    list_display = ('name','type','state_id')

    class meta:
        model = State_Legislatures

admin.site.register(State_Legislatures,State_Legislatures_Admin)

class Term_Admin(admin.ModelAdmin):
    list_display = ('term_name','start_year','end_year','central_legislature_id')

    class meta:
        model = Term

admin.site.register(Term,Term_Admin)
