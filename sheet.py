import gspread
import os

sheet_id = os.environ['SHEET_ID']
worksheet_name = 'Billing'


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list) + 1)


def gs_service():
    return gspread.service_account('gsheet_cred.json')


def init_wks(s, wks_name):
    sheet = gs_service().open_by_key(s)
    return sheet.worksheet(wks_name)


def insert_data(date, cost):
    wks = init_wks(sheet_id, worksheet_name)
    index = str(next_available_row(wks))
    wks.update('A' + index, date)
    wks.update('B' + index, cost)
