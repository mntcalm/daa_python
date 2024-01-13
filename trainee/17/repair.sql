SELECT setval(pg_get_serial_sequence('carts', 'cart_id'), (SELECT MAX(cart_id) FROM carts));
