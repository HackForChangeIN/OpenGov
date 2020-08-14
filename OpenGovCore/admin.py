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
