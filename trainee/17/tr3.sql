BEGIN;
DELETE FROM carts WHERE cart_id = (SELECT carts_cart_id FROM cart_products WHERE products_product_id = (SELECT product_id FROM Products WHERE product_title = 'Metla' LIMIT 1) LIMIT 1 );
DELETE FROM cart_products WHERE products_product_id = (SELECT product_id FROM Products WHERE product_title = 'Metla' LIMIT 1);
DELETE FROM Products WHERE product_title = 'Metla';
COMMIT;
