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
       now = datetime.now()
        
       cur_stat=cur_status.tkt_status()

       if prev_status.read_tkt_status()!=cur_stat:
           thd_id,msg_id,first,line_no=prev_status.read_msg_status()
            
           if Decimal(sub(r'[^\d.]', '',cur_stat)) <= 10500.00:
                #msg_id=send_mail.send_thread('The price is '+cur_stat+' at '+str(now),thd_id,msg_id,first)        #sending the mail with updated price if price above threshold
               
           update_price_history.update_price(cur_stat,line_no,now)                           #updating the excel sheet with the price to maintain price history                line_no=str(int(line_no)+1)
           line_no=str(int(line_no)+1)
           update_status.update_info_status(cur_stat,msg_id,msg_id,first,line_no)
                
                
       print("Tracked File",now)
       fails=0                          #after a success the fails counter is brought back to zero
       err_msg=0
       time.sleep(3600)
