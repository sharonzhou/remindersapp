from flask import Flask
from flask import request
from flask import render_template
import os
from random import choice


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    if request.form['Body'].upper() == "HELP":
        r.sms("Welcome to the text reminder app.  Text HELP" \
                "to get your reminders.")
    else:
        r.sms(choice(reminders))
    return str(r)

reminders = [
    'Have you taken your medication today?',
    'Have you written in your journal today?',
    'Have you called your parents lately?']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)