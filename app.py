from flask import Flask, request, redirect, render_template
import os
from random import choice
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+19133784671": "Curious George",
    "+14244429724": "Boots",
    "+14158675309": "Jane Doe"
}
 
@app.route('/')
def index():
    return render_template('index.html')   

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)

@app.route('/sms', methods=['POST'])
def sms():
    r = twilio.twiml.Response()
    if request.form['Body'].upper() == "HELP":
        r.sms("Welcome to text reminder app.")
    else:
        r.sms(choice(callers))
    return str(r)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)