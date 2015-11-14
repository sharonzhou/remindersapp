from twilio.rest import TwilioRestClient
from local_settings import *

# Your Account Sid and Auth Token from twilio.com/user/account
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
# send a text every minute
message = client.messages.create(body="Have you written in your diary today?",
    to=MY_NUMBER,    # Replace with your phone number
    from_="+19134897538") # Replace with your Twilio number
print message.sid