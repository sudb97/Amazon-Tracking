from Google import Create_Service
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import six
import retrive_ids

def send_thread(current_status,thd_id,msid,first):           #sending email reply as on the same thread
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    if first==str(1):
        emailMsg='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxx'+current_status+'\n'+'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.'          #change the body here for first mail
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'                                #change the recipient of the mail
        mimeMessage['subject'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'         #Change the subject for the 1st mail
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

        return message["id"]

    else:
        msg_id,ref_id=retrive_ids.get_mime_ids(msid)
        message = MIMEText('xxxxxxxxxxxxxxxxxxxxxxxx'+current_status+'\n'+'Please visit https://www.amazon.in/Fitbit-Charge-Fitness-Tracker-Non-NFC/dp/B084CQ41M2/ref=sr_1_8?dchild=1&keywords=fitbit%2Bcharge%2B3&qid=1608032936&sr=8-8&th=1 for more details.')  #change the body of the threaded mail
        message['to'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'                                                #change the recipient of the thread mail
        message['subject'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'                         #Change the subject of the threaded mail
        message['In-Reply-To'] = msg_id
        message['References'] = ref_id
        sz_message = message.as_string()
        raw_msg_byte =base64.urlsafe_b64encode(six.ensure_binary(sz_message))
        raw_msg = six.ensure_str(raw_msg_byte)
        new_email = {'raw': raw_msg}
        new_email['threadId'] = thd_id

        sent=service.users().messages().send(userId='me', body=new_email).execute()
        return sent["id"]



    #Note : In place of XXXXXXXXXXXXXXXXXXXXXX   please writ according to your requirement
