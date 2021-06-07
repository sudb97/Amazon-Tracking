import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_info_status(current_status,thd_id,msg_id,first,line_no):         #updates the status of the product when tracking is done
    scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials_sheets.json', scope)

    gc= gspread.authorize(credentials)
    wks= gc.open('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').sheet1      #change the google sheets database name
    
    if first==str(1):
        wks.update_acell('B1',current_status)
        wks.update_acell('B2',thd_id)
        wks.update_acell('B3',msg_id)
        wks.update_acell('B4',0)
        wks.update_acell('B5',line_no)

    else:
        wks.update_acell('B1',current_status)
        wks.update_acell('B3',msg_id)
        wks.update_acell('B5',line_no)



def update_error_status(thd_id,msg_id,first):         #updates the status when error is encountered
    scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials_sheets.json', scope)

    gc= gspread.authorize(credentials)
    wks= gc.open('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').sheet1      #change the google sheets database name
    
    if first==str(1):
        #wks.update_acell('B1',current_status)
        wks.update_acell('B2',thd_id)
        wks.update_acell('B3',msg_id)
        wks.update_acell('B4',0)
        #wks.update_acell('B5',line_no)

    else:
        #wks.update_acell('B1',current_status)
        wks.update_acell('B3',msg_id)
        #wks.update_acell('B5',line_no)