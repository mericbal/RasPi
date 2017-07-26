from twilio.rest import Client
from credentials import sid, token, my_cell, my_twilio

client = Client(sid, token)

msg = 'I am the Pie !'

message = client.messages.create(to=my_cell, from_=my_twilio, body=msg)

print 'Message sent !'
