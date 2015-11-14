from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC113afccf0541efc1026e31779139cbdd"
auth_token  = "9081842f8680746a4976d76aa0453492"
client = TwilioRestClient(account_sid, auth_token)
 
# send a text every minute
message = client.messages.create(body="Have you written in your diary today?",
    to="+19133784671",    # Replace with your phone number
    from_="+19134897538") # Replace with your Twilio number
print message.sid