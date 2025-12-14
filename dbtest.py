from getpass import getpass
from mysql.connector import connect, Error



def create_connection(user, password, host, database=None):


   # return 
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        if connection.is_connected():
                return connection
    except Error as e:
        print(e)


def create_database(dbname):
    HOST = db_host
    USER = input_user
    PASSWORD = input_password
    DATABASE = input_dbname

    try:
        conn_db = create_connection(USER, PASSWORD, HOST)

        print(conn_db)
        dbcrcursor = conn_db.cursor()

        create_db_query = "CREATE DATABASE IF NOT EXISTS " + DATABASE
        dbcrcursor.execute(create_db_query)

        dbcrcursor.close()
        conn_db.close()
    except Error as e:
        print(e)


def create_tables():
    HOST = db_host
    USER = input_user
    PASSWORD = input_password
    DATABASE = input_dbname

    try:
        conn_db = create_connection(USER, PASSWORD, HOST, DATABASE)

        tbcursor = conn_db.cursor()

        create_tble_query = "CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY," \
        "title VARCHAR(255)," \
        "author VARCHAR(255)," \
        "ISBN VARCHAR(255))"
        tbcursor.execute(create_tble_query)

        tbcursor.close()
        conn_db.close()
    except Error as e:
        print(e)


def insert_table():
    HOST = db_host
    USER = input_user
    PASSWORD = input_password
    DATABASE = input_dbname

    try:
        conn_db = create_connection(USER, PASSWORD, HOST, DATABASE)

        tbcursor = conn_db.cursor()

        get_book_details()
        db_author = book_details["author"]
        db_title = book_details["title"]
        db_ISBN = book_details["ISBN"]

        print(f"{book_details}")

        create_tble_query = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
        values = (db_title, db_author, db_ISBN)
        tbcursor.execute(create_tble_query, values)
        conn_db.commit()
        print(f"{db_title} inserted into books table.")




        tbcursor.close()
        conn_db.close()
    except Error as e:
        print(e)



def search_table():
    HOST = db_host
    USER = input_user
    PASSWORD = input_password
    DATABASE = input_dbname

    try:
        conn_db = create_connection(USER, PASSWORD, HOST, DATABASE)

        tbcursor = conn_db.cursor()

        search_for_book_title()

        db_title = "%"+search_title+"%"

        print(f"Searching for : {db_title}")

        create_tble_query = "SELECT * FROM books WHERE title LIKE %s"
        #values = (db_title)
        tbcursor.execute(create_tble_query, (db_title,))

        rows = tbcursor.fetchall()

        print("\n=== BOOKS LIST ===")
        for row in rows:
            print(row)

        tbcursor.close()
        conn_db.close()
    except Error as e:
        print(e)


def get_book_details():
    input_title = input("Enter Book Title: ")
    input_author = input("Enter Book Author: ")   
    input_isbn = input("Enter Book ISBN: ")

    global book_details

    book_details = {"title" : input_title, "author" : input_author, "ISBN" : input_isbn }

    return book_details


def search_for_book_title():

    global search_title   

    search_title = input("Enter Book Title: ")

    return search_title


def main():
    global input_user,input_password,input_dbname,db_host
    input_user = input("Enter username: ")
    input_password=getpass("Enter password: ")
    input_dbname=input("Enter database: ")
    db_host = "localhost"

    create_database(input_dbname)
    create_tables()
    add_books = 'Y'

    while add_books == "Y":
        add_books_input = input("Do you want to add a new Books Y/N?: ")
        if add_books_input == add_books and add_books_input == "Y"  :
            insert_table()

        else:
            print(f"See you next time, No books to be added")

        add_books = add_books_input


    search_table()


        

        

        
    


        
    

#    conn = create_connection(input_user, input_password, db_host, input_dbname)
#
 #   print(f"Conn connection is {conn}")
    show_db_query = "SHOW DATABASES"
#
 #   print("Is connection open? ", conn.is_connected())
#
 ##   if conn is None:
   #     return "Database connection error!"
#
 #   try:
  #      cursor = conn.cursor()
#
 #       cursor.execute(show_db_query)
  #      #rows = cursor.fetchall()
   #     for db in cursor:
    #        print(db)

   # except Error as e:
   #     print(f"❌ Query error: {e}")
    #    return None

   # finally:
        # Always close
    #    if conn.is_connected():
     #       cursor.close()
      #      conn.close()
    #

if __name__ == "__main__":
    main()