CREATE FUNCTION update_shipping_total (IN city_name VARCHAR(255))
RETURNS VARCHAR(255)
LANGUAGE SQL
AS $$
UPDATE "Order" SET shipping_total = 0
WHERE Carts_cart_id IN (
SELECT user_id FROM Users
WHERE city = city_name
)
RETURNING (SELECT city FROM Users WHERE city = city_name);
$$;