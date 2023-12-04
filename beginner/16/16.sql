SELECT * FROM Products WHERE price>80 AND price<=150;
SELECT * FROM "Order" WHERE created_at>'2020-10-01';
SELECT * FROM "Order" WHERE EXTRACT(year FROM created_at)=2020 AND EXTRACT(month FROM created_at)<=6;
SELECT * FROM Products WHERE category_id=7 OR category_id=11 OR category_id=18;
SELECT * FROM "Order" WHERE (Order_status_order_status_id!=4 OR Order_status_order_status_id!=5) AND updated_at<='2020-12-31';
SELECT * FROM Carts WHERE cart_id in (SELECT Carts_cart_id FROM "Order" WHERE Order_status_order_status_id=1 OR Order_status_order_status_id=2 OR Order_status_order_status_id=3);
