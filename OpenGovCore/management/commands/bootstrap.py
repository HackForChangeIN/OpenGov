from django.core.management.base import BaseCommand
from OpenGovCore.models import States, Parliamentary_Constituencies, Assembly_Constituencies, Parties
import xlrd
from opengovparser import OpenGovParser
from loksabhaparser import LoksabhaParser

class Command(BaseCommand):
    help = 'Load initial data to database'

    def handle(self, *args, **kwargs):
        #load_state()
        #load_parliamentary_constituency()
        #load_assembly_constituency()
        #load_party_information()


def load_state():
    workbook = xlrd.open_workbook("OpenGovCore/data/raw_data/State_list.xlsx")
    worksheet = workbook.sheet_by_index(0)

    rows = worksheet.nrows
    cols = worksheet.ncols
    for row in range(1, rows):
        for col in range(cols):
            try:
                state_obj = States.objects.get_or_create(
                    name=worksheet.cell(row, col).value)
            except:
                print("Error in loading state list")

            #print(worksheet.cell(row,col).value)
        row += 1
    print("State data loaded")


def load_parliamentary_constituency():
    workbook = xlrd.open_workbook(
        "OpenGovCore/data/raw_data/Parliamentary_constituencies_list.xlsx")
    for sheet in workbook.sheets():
        for row in range(1, sheet.nrows):
            name = sheet.cell_value(row, 0)
            constituency_number = int(sheet.cell_value(row, 1))
            state = sheet.name
            try:
                state_obj = States.objects.get(name=state)
                parliamentary_constituency_obj = Parliamentary_Constituencies.objects.get_or_create(name=name, constituency_number=constituency_number,
                                                                                                    state=state_obj)
                row += 1
            except:
                print("error")
    print("Parliamentary Constituencies are loaded")


def load_assembly_constituency():
    workbook = xlrd.open_workbook(
        "OpenGovCore/data/raw_data/State_assembly_constituencies_list.xlsx")
    for sheet in workbook.sheets():
        for row in range(1, sheet.nrows):
            name = sheet.cell_value(row, 0)
            constituency_number = int(sheet.cell_value(row, 1))
            state = sheet.name
            try:
                state_obj = States.objects.get(name=state)
                assembly_constituency_obj = Assembly_Constituencies.objects.get_or_create(name=name,
                                                                                          constituency_number=constituency_number, state=state_obj)
                row += 1
            except:
                print("error in", state)
    print("Assembly Constituencies are loaded")


def load_party_information():
    workbook = xlrd.open_workbook(
        "OpenGovCore/data/raw_data/Political party information.xlsx")
    for sheet in workbook.sheets():
        for row in range(1, sheet.nrows):
            party_name = sheet.cell_value(row, 0)
            acronym = sheet.cell_value(row, 1)
            type = sheet.cell_value(row, 2)
            founded = int(sheet.cell_value(row, 3))
            founder_name = sheet.cell_value(row, 4)
            president_name = sheet.cell_value(row, 5)
            website = sheet.cell_value(row, 6)
            #print(party_name,acronym,type,founded,founder_name,president_name,website)
            try:
                party_obj = Parties.objects.get_or_create(party_name=party_name, acronym=acronym, type=type,
                                                          founded=founded, founder_name=founder_name, president_name=president_name, website=website)
                row += 1
            except:
                print("Error in ", row)
    print("Party informations are loaded")
