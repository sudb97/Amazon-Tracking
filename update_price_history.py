import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_price(current_status,line_no,date):
	scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials_sheets.json', scope)

	gc= gspread.authorize(credentials)
	wks= gc.open('xxxxxxxxxxxxxxxxxxxxxx').get_worksheet(1)    #change the google sheets database name
    
	
	wks.update_acell('A'+line_no,str(date))
	wks.update_acell('B'+line_no,current_status)