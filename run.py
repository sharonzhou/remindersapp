import time
import random
from local_settings import *
from twilio.rest import TwilioRestClient

def sendsms():
	# Your Account Sid and Auth Token from twilio.com/user/account
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
	message = client.messages.create(body="Have you eaten breakfast? Reply with Yes or No.",
    to="+18605329948",    # Replace with your phone number
    from_="+12036897875") # Replace with your Twilio number
	print message.sid


def receivesms():
	# Your Account Sid and Auth Token from twilio.com/user/
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
	# A list of message objects with the properties described above
	messages = client.messages.list(from_="+18605329948")
	reply =  messages[0].body
	print reply
	return (reply)


def dataprocess(reply):
	if reply == 'Yes':
		print('The job is done')
	elif reply == 'No':
		sendsms()
	else:
		print('The response is not valid')

if __name__ == "__main__":
	sendsms()
	reply = receivesms()
	delay = random.randint(15,30)
	time.sleep(delay)
	dataprocess(reply)