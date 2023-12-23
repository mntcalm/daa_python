SELECT AVG(total) AS average_total FROM "Order" WHERE Order_status_order_status_id=4;
SELECT MAX(total) AS max_total FROM "Order" WHERE updated_at>'2020-06-30' AND updated_at<'2020-10-01';
