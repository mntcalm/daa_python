EXPLAIN SELECT * FROM Users ORDER BY email;
EXPLAIN SELECT * FROM Users ORDER BY last_name, first_name;
EXPLAIN SELECT * FROM Products ORDER BY category_id, product_title;
CREATE INDEX email_idx ON Users (email);
CREATE INDEX lastfirst_idx ON Users (last_name, first_name);
CREATE INDEX categ_titl_idx ON Products (category_id, product_title);
