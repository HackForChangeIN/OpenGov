from django.core.management.base import BaseCommand
from OpenGovCore.models import States, Parliamentary_Constituencies, Assembly_Constituencies
import xlrd

class Command(BaseCommand):
    help = 'Load initial data to database'

    def handle(self, *args, **kwargs):
        load_state()
        load_parliamentary_constituency()
        load_assembly_constituency()
        

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
    workbook = xlrd.open_workbook("OpenGovCore/data/raw_data/Parliamentary_constituencies_list.xlsx")
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



