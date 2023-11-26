create database korziny;
\c korziny;

CREATE TABLE cart_products (Id SERIAL PRIMARY KEY, carts_cart_id INT, products_product_id INT);
CREATE TABLE carts (cart_id SERIAL PRIMARY KEY, Users_user_id INT, subtotal DECIMAL, total DECIMAL, timestamp (2));
CREATE TABLE categories (category_id SERIAL PRIMARY KEY, category_title VARCHAR(255), category_description TEXT);
CREATE TABLE "Order" (order_id SERIAL PRIMARY KEY, Carts_cart_id INT, Order_status_order_status_id INT, shipping_total DECIMAL, total DECIMAL, created_at TIMESTAMP(2), updated_at TIMESTAMP(2));
CREATE TABLE Order_status (order_status_id SERIAL PRIMARY KEY, status_name VARCHAR(255));
CREATE TABLE Products (product_id SERIAL PRIMARY KEY, product_title VARCHAR(255), product_description TEXT, in_stock INT, price FLOAT8, slug VARCHAR(45), category_id INT);
CREATE TABLE Users (user_id SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), middle_name VARCHAR(255), is_staff SMALLINT, country VARCHAR(255), city VARCHAR(255), address TEXT);

ALTER TABLE "Order" ADD CONSTRAINT ordering FOREIGN KEY (Order_status_order_status_id) REFERENCES Order_status (order_status_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE cart_products ADD CONSTRAINT carting FOREIGN KEY (carts_cart_id) REFERENCES carts (cart_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE cart_products ADD CONSTRAINT producting FOREIGN KEY (products_product_id) REFERENCES Products (product_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Products ADD CONSTRAINT producting FOREIGN KEY (category_id) REFERENCES categories (category_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE carts ADD CONSTRAINT usering FOREIGN KEY (Users_user_id) REFERENCES Users (user_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "Order" ADD CONSTRAINT carting2 FOREIGN KEY (Carts_cart_id) REFERENCES carts (cart_id) ON DELETE CASCADE ON UPDATE CASCADE;
