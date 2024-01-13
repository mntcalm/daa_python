BEGIN;
UPDATE Products SET product_description = 'SUPER-metla', price = 249.99 WHERE product_title = 'Metla';
UPDATE carts SET total = 201.50 WHERE cart_id = (SELECT carts_cart_id FROM cart_products WHERE products_product_id = (SELECT product_id FROM Products WHERE product_title = 'Metla' LIMIT 1) LIMIT 1);
COMMIT;
