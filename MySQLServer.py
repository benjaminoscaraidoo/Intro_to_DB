import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )

    tbcursor = mydb.cursor()

    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

    tbcursor.execute(create_db_query)

    tbcursor.close()
    mydb.close()
except mysql.connector.Error as e:
        print(e)
