from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'end_db'
mail = Mail(app)
mysql = MySQL(app)

@app.route('/create', methods=['POST'])
def dataSet():
    cur = mysql.connection.cursor()
    cur.execute(f"""CREATE DATABASE `end_db`""")
    mysql.connection.commit()
    return "database created"
@app.route('/create/tab', methods=['POST'])
def tableCreate():
    cur = mysql.connection.cursor()
    cur.execute(f"""USE `end_db`""")
    cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS `create_note`(
                     `id` INT PRIMARY KEY AUTO_INCREMENT,
                      `note_title` VARCHAR(100) NOT NULL,
                       `note_content` LONGTEXT,
                        `author` VARCHAR(50),
                         `date_created` timestamp DEFAULT current_time
                    );
                """)
    mysql.connection.commit()
    return("table created")

@app.route('/create/insert', methods=["POST", "GET", "PUT", "DELETE"])
def createNote():
    cur = mysql.connection.cursor()
    cur.execute("""USE `end_db`""")
    if request.method == 'POST':
        id = request.json['id']
        note_title = request.json['note_title']
        note_content = request.json['note_content']
        author = request.json['author']
        date_created = request.json['date_created']
        cur.execute(f"""INSERT INTO `create_note` VALUES (%s, %s, %s, %s, %s)""",
                    (id, note_title, note_content, author, date_created))
        mysql.connection.commit()
        return jsonify(id, note_title, note_content, author, date_created)
    elif request.method == 'GET':
        id = request.json['id']
        cur.execute(f"""SELECT * FROM `Create_note` WHERE id = %s""",(id))
        feedback = cur.fetchall()
        mysql.connection.commit()
        return jsonify(feedback)
    elif request.method == 'PUT':
        id = request.json['id']
        note_title = request.json['note_title']    
        cur.execute(f"""UPDATE `Create_note` SET Note_Title = %s WHERE id = %s """,(note_title, id))
        mysql.connection.commit()
        return jsonify(id, note_title)
    elif request.method == 'DELETE':
        id = request.json['id']
        cur.execute(f"""DELETE FROM `Create_note` WHERE id = %s""",(id))
        mysql.connection.commit()
        return "Successful"
    else:
        return "Syntax malfunction"
    
if (__name__=='__main__'):
    app.run(debug=True)