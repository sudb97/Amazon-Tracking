#Build 1- 09-12-2020: Regular updates about amazon product price via mail with updates on a thread
import prev_status
import send_mail
import update_status
import cur_status
import update_price_history
import time
from datetime import datetime
from re import sub
from decimal import Decimal

fails=0             #tracks the number of times consecutive failures happen
err_msg=0           #tracks if error email msg is sent or not    

print("The app started")
while True:
    try:
        now = datetime.now()
        
        cur_stat=cur_status.tkt_status()

        if prev_status.read_tkt_status()!=cur_stat:
            thd_id,msg_id,first,line_no=prev_status.read_msg_status()
            
            if Decimal(sub(r'[^\d.]', '',cur_stat)) <= xxxxxxxx or first== str(1):
                msg_id=send_mail.send_thread('Price'+cur_stat+str(now),thd_id,msg_id,first)        #trigger mail with updated price if price above given "XXXXXXXXX"*(int)
            
            update_price_history.update_price(cur_stat,line_no,now)                           #google sheet updated with the price
            line_no=str(int(line_no)+1)
            update_status.update_info_status(cur_stat,msg_id,msg_id,first,line_no)
                
                
        print("Tracked File",now)
        fails=0                          #after a success the fails counter is brought back to zero
        err_msg=0
        time.sleep(3600)
        #this part tracks if problem occurs in sending email
    except Exception as e:
        fails=fails+1
        if fails>=3 and err_msg==0:
            try:
                error_msg="Alert.......................... "+str(now)
                thd_id,msg_id,first,line_no=prev_status.read_msg_status()
                msg_id=send_mail.send_thread(error_msg,thd_id,msg_id,first)
                update_status.update_error_status(msg_id,msg_id,first)
                err_msg=1
            except Exception as err:
                pass
            
        print("Cannot track ............."+str(now)+str(e)+" Please Trying again...")
        time.sleep(900)       

        



