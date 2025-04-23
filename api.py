from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/data')
def get_data():
    db = mysql.connector.connect(

        host='localhost',
        user='root',
        password='root123',
        database='chatbot_db'
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM quotes")
    result = cursor.fetchall()
    db.close()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)