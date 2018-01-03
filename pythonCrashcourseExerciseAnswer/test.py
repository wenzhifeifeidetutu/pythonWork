
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC56dcd1daaf19db0800160fb42bde3e31"
# Your Auth Token from twilio.com/console
auth_token  = "250aa08476c3eaf06c2594363bbdee3d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18171270317", 
    from_="+12568587724",
    body="Hi ~this is a test from web")

print(message.sid)
