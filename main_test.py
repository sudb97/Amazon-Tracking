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
            
            if Decimal(sub(r'[^\d.]', '',cur_stat)) <=xxxxxxxx:
                msg_id=send_mail.send_thread('xxxxxxxxxxxxxx'+cur_stat+' xxxxxxxxxxxxxxxx '+str(now),thd_id,msg_id,first)        #sending the mail with updated price if price above threshold
            
            update_price_history.update_price(cur_stat,line_no,now)                           #updating the excel sheet with the price to maintain price history                line_no=str(int(line_no)+1)
            line_no=str(int(line_no)+1)
            update_status.update_info_status(cur_stat,msg_id,msg_id,first,line_no)
                
                
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ",now)
        fails=0                          #after a success the fails counter is brought back to zero
        err_msg=0
        time.sleep(3600)
    except Exception as e:
        fails=fails+1
        if fails>=3 and err_msg==0:
            try:                                     #this part will send email message in case of there is any failure in tracking
                error_msg="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+str(now)+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                thd_id,msg_id,first,line_no=prev_status.read_msg_status()
                msg_id=send_mail.send_thread(error_msg,thd_id,msg_id,first)
                update_status.update_error_status(msg_id,msg_id,first)
                err_msg=1
            except Exception as err:
                pass
            
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+str(now)+" xxxxxxxxxxxxxxxxxxxxxxxxx "+str(e)+".xxxxxxxxxxxxxxxxxxxxxxxx")
        time.sleep(900)       

        



