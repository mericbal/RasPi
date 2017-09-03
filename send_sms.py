from twilio.rest import Client
from credentials import sid, token, meric, nil,  my_twilio

client = Client(sid, token)

msg = 'I am the PIE !'

message_to_nil = client.messages.create(to=nil, from_=my_twilio, body=msg)
print 'Message sent to Nil !'
message_to_meric = client.messages.create(to=meric, from_=my_twilio, body=msg) 
print 'Message sent to Meric !'

print 'Messages sent to all users !'
