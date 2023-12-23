SELECT category_title, COUNT(c.category_id) AS kolvo1 FROM Categories c JOIN Products p ON p.category_id=c.category_id GROUP BY category_title;
