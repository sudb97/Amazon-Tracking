from Google import Create_Service

def get_mime_ids(msid):                     #to get message and thread id of the message sent with id of the message
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    ref_msgid= service.users().messages().get(userId='me',id=msid,format = 'metadata',metadataHeaders =['References','Message-ID']).execute()
    ids=ref_msgid["payload"]["headers"]
    if len(ids)==2:
        return [ref_msgid["payload"]["headers"][1]["value"],ref_msgid["payload"]["headers"][0]["value"]]
    if len(ids)==1:
        return [ref_msgid["payload"]["headers"][0]["value"],ref_msgid["payload"]["headers"][0]["value"]]