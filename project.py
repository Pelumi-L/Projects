import requests

url = 'http://localhost:5000/verify'  
user_email = input('Enter email: ')
data = {'email': user_email}  
response = requests.post(url, json=data)

if response.status_code == 200:
    print('Email sent successfully')
else:
    print('Failed to send email')