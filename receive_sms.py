from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC113afccf0541efc1026e31779139cbdd"
auth_token  = "9081842f8680746a4976d76aa0453492"
client = TwilioRestClient(account_sid, auth_token)
 
# grab the most recent message
for message in client.messages.list():
    print message.body