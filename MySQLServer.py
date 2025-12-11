import mysql.connector


create_db_query = ["CREATE DATABASE IF NOT EXISTS alx_book_store"]
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
except mysql.connector.Error as e:
        print(e)



        create_tble_query = "CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY," \
        "title VARCHAR(255)," \
        "author VARCHAR(255)," \
        "ISBN VARCHAR(255))"
        tbcursor.execute(create_tble_query)
