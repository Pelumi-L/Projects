from flask import Flask, jsonify, request
app = Flask(__name__)
# @app.route('/home', methods=['GET'])
# def sayHello():
#     return('hello world')

# @app.route('/register/user', methods=['GET'])
# def regUser():
#     fname = input('username: ')
#     return(fname)

# @app.route('/register/user', methods=['GET'])
# def regUsers():
#     collection = {'username': 'john', 'password' : 'eedge43', 'email': 'wertyu@gmail.com', 'telephone': '08123453267'}
#     return(collection)



# if (__name__=='__main__'):
#     app.run(debug=True)


#put the dictionary into a list and loop it 5 times, then use get, delete, put and post to modify the data

user = []
for i in range(1, 6):
    username = input("username: ")
    password = input("password: ")
    email = input("email: ")
    telephone = input("telephone: ")
    user.append({"username": username, "password": password, "email": email, "telephone": telephone})

@app.route('/register/user', methods=['GET'])
def regUser():
    return(user)

@app.route('/register/user', methods=['POST'])
def addUser():
    new_user = {
        "username": "awe",
        "password" : "32456",
        "email" : "gaqr@email.com",
        "telephone": "09125662542"
    }
    if new_user:
        user.append(new_user)
        return(user)
    
@app.route('/register/user', methods=['PUT'])
def updateUser():
    for users in user:
        if users['username'] == "Abb":
            #set one of the entries as Abb
            users['password'] = "445324"
            users['email'] = "werter@email.com"
            users['telephone'] = "08143335667"
            return(user)

@app.route('/register/user', methods=['DELETE'])
def deleteUser():
    for users in user:
        if users['username'] == "Pel":
            user.remove(users)
            return(user)


if (__name__=='__main__'):
    app.run(debug=True)