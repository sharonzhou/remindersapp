from flask import Flask
from flask import request
from flask import render_template
import os
from random import choice


app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+19133784671": "Yuqi"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/sms", methods=['GET', 'POST'])
def hello_word():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)