from flask import Flask, request
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'farklelanoe@gmail.com'  
app.config['MAIL_PASSWORD'] = 'hrgirbdsjtxguoar'         
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/verify', methods=['POST'])
def emailer():
    characters = "ABCDEFdg4y3863462fHEUT"
    verification = ''.join(random.choice(characters) for _ in range(5))
    
    # data = request.get_json()  
    user_mail = request.json["email"]  

    verification_message = Message(
        'Verification',
        sender='farklelanoe@gmail.com',  
        recipients=[user_mail]          
    )
    verification_message.body = verification
    mail.send(verification_message)
    return 'Sent'

if __name__ == '__main__':
    app.run(debug=True)
