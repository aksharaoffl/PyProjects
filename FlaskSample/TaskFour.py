from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Establish a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL2024!",
    database="demo"
)


# API to get all student details
@app.route('/students', methods=['GET'])
def get_students():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENTDETAILS")
    students = cursor.fetchall()
    cursor.close()
    return jsonify([{'rollNo': s[0], 'sname': s[1], 'grade': float(s[2]), 'mobileNumber': s[3]} for s in students])


# API to get student details by roll number
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


if __name__ == '__main__':
    app.run(debug=True)
