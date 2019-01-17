from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC20b24e5541423af81a004d1c77bc6985"
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+4917916", 
    from_="+4917916",
    body="Hello from Benjamin!")

print(message.sid)
