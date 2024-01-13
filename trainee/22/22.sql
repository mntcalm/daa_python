SELECT c.category_title, p.product_title, p.price, AVG (p.price) OVER (PARTITION BY p.category_id) AS avg
FROM Products p
INNER JOIN Categories c ON p.category_id = c.category_id;