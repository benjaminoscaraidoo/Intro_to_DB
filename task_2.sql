CREATE TABLE Authors (author_id INT AUTO_INCREMENT PRIMARY KEY, author_name VARCHAR(215))

CREATE TABLE Books (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(130),FOREIGN KEY (author_id) REFERENCES Authors(author_id),price DOUBLE, publication_date DATE)


["Customers", "customer_id ", "customer_name VARCHAR(215)", "email VARCHAR(215)", "address TEXT"]

["Orders", "order_id INT", "customer_id INT", "order_date DATE", "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)"]

["CREATE TABLE ", "Authors", "author_id ", "author_name"]
