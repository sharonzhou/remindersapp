from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
# grab the most recent message
for message in client.messages.list():
    print message.body