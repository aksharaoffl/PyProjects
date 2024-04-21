import json
from flask import Flask, jsonify  #flask - creating web application. jsonify for returning json responces.
import mysql.connector # for connecting to the MySQL database

app = Flask(__name__) #creates a new Flask application instance, and assigns it to the variable app.
#This instance represents the web application that will handle requests and responses.

# Connect to the database establish a connection to the database using the mysql.connector module
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL2024!",
    database="demo"
)


@app.route('/students', methods=['GET']) #@app.route('<url_path>', methods=['<http_method>'])
def getStudents():
    try:
        #A cursor is a control structure that enables traversal over the database records
        #obejct = database connection object.method that creates a new cursor object
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENTDETAILS")
        students = cursor.fetchall()
        cursor.close()
        return jsonify([{'rollNo': s[0], 'sname': s[1], 'grade': float(s[2]), 'mobileNumber': s[3]} for s in students])
    except Exception as e:
        cursor.close()
        return jsonify({'error': str(e)}), 500

#TaskTwo
@app.route('/students/<roll_no>', methods=['GET'])
def getStudentDetails(roll_no=None):
    if roll_no is None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENTDETAILS")
        students = cursor.fetchall()
        cursor.close()
        return jsonify([{'rollNo': s[0], 'sname': s[1], 'grade': float(s[2]), 'mobileNumber': s[3]} for s in students])
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENTDETAILS WHERE rollNo = %s", (roll_no,))
        student = cursor.fetchone()
        cursor.close()
        if student is None:
            return jsonify({'error': 'Student not found'}), 404
        else:
            return jsonify(
                {'rollNo': student[0], 'sname': student[1], 'grade': float(student[2]), 'mobileNumber': student[3]})

# Task Three
@app.route('/students/getStudentDetailsBelowCO', methods=['GET'])
@app.route('/students/getStudentDetailsBelowCO/<co>', methods=['GET'])
def getStudentDetailsBelowCO(co=None):
	if co is None:
		return jsonify([])
	else:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM STUDENTDETAILS WHERE grade < %s", (co,))
		students = cursor.fetchall()
		cursor.close()
		return jsonify([{'rollNo': s[0], 'sname': s[1], 'grade': float(s[2]), 'mobileNumber': s[3]} for s in students])

@app.route('/students/getStudentDetailsAboveCO', methods=['GET'])
@app.route('/students/getStudentDetailsAboveCO/<co>', methods=['GET'])
def getStudentDetailsAboveCO(co=None):
    if co is None:
        return getStudents()
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENTDETAILS WHERE grade > %s", (co,))
        students = cursor.fetchall()
        cursor.close()
        return jsonify([{'rollNo':s[0], 'sname': s[1], 'grade': float(s[2]),'mobileNumber' :s[3]} for s in students])

@app.route('/students/getStudentGradeWithNamePattern/<pattern>', methods = ['GET'])
def getStudentGradeWithNamePattern(pattern):
    cursor = conn.cursor()
    cursor.execute("SELECT sname, grade FROM  STUDENTDETAILS WHERE sname LIKE %s", ('%'+pattern+'%',))

    students = cursor.fetchall()
    cursor.close()
    return jsonify([{'sname': s[0], 'grade': float(s[1])} for s in students])

if __name__ == '__main__':
    app.run(debug=True)

