from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'xyz@gmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender = 'xyz@gmail.com', recipients=['shah.rikesh007@gmail.com'])
    msg.body = "Hello Flask! This Message is sent from Flask-mail"
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run()