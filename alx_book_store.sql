CREATE TABLE IF NOT EXISTS alx_book_store
 (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(130),FOREIGN KEY(author_id) REFERENCES Authors(id),price DOUBLE,publication_date DATE)