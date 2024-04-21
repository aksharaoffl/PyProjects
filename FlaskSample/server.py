import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    user='root',
    password='MySQL2024!',
    host='localhost',
    database='demo'
)


# Create a cursor object
cursor = cnx.cursor()

# Execute a query
cursor.execute('SELECT * FROM STUDENTDETAILS')

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()
