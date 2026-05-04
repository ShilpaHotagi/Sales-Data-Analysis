-- Total sales by region
SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region;

-- Top category
SELECT category, SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Monthly sales
SELECT MONTH(order_date) AS month, SUM(sales)
FROM sales
GROUP BY MONTH(order_date);