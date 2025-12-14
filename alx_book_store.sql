CREATE TABLE IF NOT EXISTS alx_book_store

["author_id ", "author_name"]
["Books"]
["Customers", "customer_id ", "customer_name VARCHAR(215)", "email VARCHAR(215)", "address TEXT"]
["Orders", "order_id INT", "customer_id INT", "order_date DATE", "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)"]
["Order_Details", "quantity DOUBLE", "FOREIGN KEY (order_id) REFERENCES Orders(order_id)", "FOREIGN KEY (book_id) REFERENCES Books(book_id)"]





CREATE DATABASE IF NOT EXISTS alx_book_store

CREATE TABLE IF NOT EXISTS Books (book_id (Primary Key) INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(130),FOREIGN KEY (author_id) REFERENCES Authors (author_id),price DOUBLE,publication_date DATE)

CREATE TABLE IF NOT EXISTS Authors (author_id (Primary Key) INT AUTO_INCREMENT PRIMARY KEY,
author_name VARCHAR(215)

CREATE TABLE IF NOT EXISTS Customers (customer_id (Primary Key) INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(215),email VARCHAR(215),address TEXT)

CREATE TABLE IF NOT EXISTS Orders (order_id (Primary Key) INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),order_date DATE)

CREATE TABLE IF NOT EXISTS Order_Details (orderdetailid (Primary Key) INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (order_id) REFERENCES Orders (order_id),FOREIGN KEY (book_id) REFERENCES Books (book_id),quantity DOUBLE)
