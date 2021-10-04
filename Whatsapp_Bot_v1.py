# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:17:05 2020

@author: Styrande
"""

import os
from twilio.rest import Client
import time

account_sid = 'ACfec5f72d2****'
auth_token = 'faca9b8****'
client = Client(account_sid, auth_token)




message = client.messages.create(
                                 body="Günaydın",
                                 from_='whatsapp:+14155238886',
                                 to='whatsapp:+90543*******')

time.sleep(120)
message = client.messages.create(
                                 body="Naber",
                                 from_='whatsapp:+14155238886',
                                 to='whatsapp:+90543*******')
time.sleep(120)
message = client.messages.create(
                                 body="Günün Nasıldı?",
                                 from_='whatsapp:+14155238886',
                                 to='whatsapp:+90543*******')
time.sleep(120)
message = client.messages.create(
                                 body="İyi Geceler",
                                 from_='whatsapp:+14155238886',
                                 to='whatsapp:+90543*******')

print(message.sid)
