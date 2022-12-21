import pymysql.cursors
from flask import Flask, jsonify


app = Flask(__name__)

connection = pymysql.connect(host="chalbroker.cs1122.engineering.nyu.edu",
                             user="student",
                             password="student",
                             db="cs1122")

@app.route('/')
def index():
    try:
        with connection.cursor() as cursor:
            
            
            
        #  sql="SHOW TABLES"
         #   cursor.execute(sql)
         # print(cursor.fetchall())
         
          #  sql="SHOW COLUMNS FROM 'students' FROM cs1122"
         #   cursor.execute(sql)
         # print(cursor.fetchall())
         
        
            sql="SELECT * FROM students WHERE net_id='yz4184'"
            cursor.execute(sql)
            result=cursor.fetchone()
            
                
    
            
    finally:
        connection.close()
    
    return jsonify(result)




    

if __name__ == "__main__":
    app.run(debug=True)
    