
        create_tble_query = "CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY," \
        "title VARCHAR(255)," \
        "author VARCHAR(255)," \
        "ISBN VARCHAR(255))"
        tbcursor.execute(create_tble_query)
