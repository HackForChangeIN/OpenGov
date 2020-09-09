workbook = xlrd.open_workbook(
        "OpenGovCore/data/raw_data/State_assembly_constituencies_list.xlsx")
    for sheet in workbook.sheets():
        for row in range(1, sheet.nrows):