CREATE TABLE Authors (author_id INT AUTO_INCREMENT PRIMARY KEY, author_name VARCHAR(215))

CREATE TABLE Books (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(130),FOREIGN KEY (author_id) REFERENCES Authors(author_id),price DOUBLE, publication_date DATE)



["CREATE TABLE ", "Authors", "author_id ", "author_name"]