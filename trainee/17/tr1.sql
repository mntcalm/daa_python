BEGIN;
INSERT INTO Products (product_title, product_description, in_stock, price, category_id) VALUES ('Metla', 'prosto metla', 1, 199.99, 2);
INSERT INTO carts (Users_user_id, total, timestamp) VALUES (15, 140.50, '2021-03-13 07:53:43');
INSERT INTO cart_products (carts_cart_id, products_product_id) VALUES (currval('carts_cart_id_seq'), currval('products_product_id_seq'));
COMMIT;
