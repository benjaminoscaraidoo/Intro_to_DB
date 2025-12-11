["CREATE TABLE IF NOT EXISTS alx_book_store"]
["author_id ", "author_name"]
["Books"]
["Customers", "customer_id ", "customer_name VARCHAR(215)", "email VARCHAR(215)", "address TEXT"]
["Orders", "order_id INT", "customer_id INT", "order_date DATE", "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)"]


alx_book_store.sql doesn't contain: ["CREATE DATABASE IF NOT EXISTS alx_book_store"]

 (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(130),FOREIGN KEY(author_id) REFERENCES Authors(id),price DOUBLE,publication_date DATE)]