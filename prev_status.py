import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_tkt_status():
    scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials_sheets.json', scope)
    
    gc= gspread.authorize(credentials)
    wks= gc.open('FitBit Tracker').sheet1   #change the google sheets database name
    
    return wks.acell('B1').value

def read_msg_status():
    scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials_sheets.json', scope)
    
    gc= gspread.authorize(credentials)
    wks= gc.open('FitBit Tracker').sheet1   #change the google sheets database name
    
    return wks.acell('B2').value,wks.acell('B3').value,wks.acell('B4').value,wks.acell('B5').value