# remindersapp
=======
# Text Reminders App
SMS app periodically texting you to ask if you've completed a certain task. Built during Hack Harvard 2015.

Text (913)489-7538 to use the mobile experience.

## Getting Started

Feel free to personalize this project. 

1. Create a Twilio account if you do not already have one. 
2. Request a phone number from Twilio. 
3. Create a TwIML application. Associate your phone number with this appliation. 
4. In local_settings.py uncomment lines 8-11. Changes the variables to the ones you have set up on your Twilio account. 

You will see your ACCOUNT SID and your AUTH TOKEN on the top of your Twilio account Dashboard. The APP SID is the name of your TwIML application. 

And your SMS Request URL to Application_url/sms

For example

	http://app-name.herokuapp.com/sms


## Technology

I'm using a bunch of fun stuff here:

* [Flask](http://flask.pocoo.org/)
* [Heroku](http://www.heroku.com)
* [Twilio](http://www.twilio.com)
* [Skeleton](http://www.getskeleton.com)


## Credits
* Based off of [Making an SMS Birthday Card with Python and Flask](https://www.twilio.com/blog/2012/01/making-an-sms-birthday-card-with-python-and-flask.html) written by [Rob Spectre](http://www.brooklynhacker.com)
* License: [Mozilla Public License](http://www.mozilla.org/MPL/)

