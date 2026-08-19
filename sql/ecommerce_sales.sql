CREATE DATABASE ecommerce_sales_analytics;

-- ===============================================
-- E-Commerce Sales Analytics SQL Queries
-- ===============================================

-- 1. View Dataset
SELECT *
FROM ecommerce_sales;

--------------------------------------------------

-- 2. Total Orders
SELECT COUNT(*) AS Total_Orders
FROM ecommerce_sales;

--------------------------------------------------

-- 3. Total Revenue
SELECT ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM ecommerce_sales;

--------------------------------------------------

-- 4. Average Order Value
SELECT ROUND(AVG(Revenue), 2) AS Average_Order_Value
FROM ecommerce_sales;

--------------------------------------------------

-- 5. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM ecommerce_sales;

--------------------------------------------------

-- 6. Revenue by Product Category
SELECT Product_Category,
       ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;

--------------------------------------------------

-- 7. Orders by Product Category
SELECT Product_Category,
       COUNT(*) AS Total_Orders
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Orders DESC;

--------------------------------------------------

-- 8. Revenue by Region
SELECT Region,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Region
ORDER BY Revenue DESC;

--------------------------------------------------

-- 9. Orders by Region
SELECT Region,
       COUNT(*) AS Orders
FROM ecommerce_sales
GROUP BY Region
ORDER BY Orders DESC;

--------------------------------------------------

-- 10. Revenue by Payment Method
SELECT Payment_Method,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Revenue DESC;

--------------------------------------------------

-- 11. Payment Method Usage
SELECT Payment_Method,
       COUNT(*) AS Total_Transactions
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Transactions DESC;

--------------------------------------------------

-- 12. Average Customer Rating
SELECT ROUND(AVG(Customer_Rating), 2) AS Avg_Rating
FROM ecommerce_sales;

--------------------------------------------------

-- 13. Average Delivery Time
SELECT ROUND(AVG(Delivery_Days), 2) AS Avg_Delivery_Days
FROM ecommerce_sales;

--------------------------------------------------

-- 14. Highest Revenue Order
SELECT *
FROM ecommerce_sales
ORDER BY Revenue DESC
LIMIT 1;

--------------------------------------------------

-- 15. Top 10 Customers by Revenue
SELECT Customer_ID,
       ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Customer_ID
ORDER BY Total_Revenue DESC
LIMIT 10;

--------------------------------------------------

-- 16. Top 10 Highest Discounts
SELECT Order_ID,
       Discount,
       Revenue
FROM ecommerce_sales
ORDER BY Discount DESC
LIMIT 10;

--------------------------------------------------

-- 17. Monthly Revenue
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;

--------------------------------------------------

-- 18. Yearly Revenue
SELECT YEAR(Order_Date) AS Year,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Year
ORDER BY Year;

--------------------------------------------------

-- 19. Monthly Orders
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
       COUNT(*) AS Orders
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;

--------------------------------------------------

-- 20. Average Revenue by Region
SELECT Region,
       ROUND(AVG(Revenue), 2) AS Avg_Revenue
FROM ecommerce_sales
GROUP BY Region
ORDER BY Avg_Revenue DESC;

--------------------------------------------------

-- 21. Revenue by Category and Region
SELECT Product_Category,
       Region,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Product_Category, Region
ORDER BY Product_Category, Revenue DESC;

--------------------------------------------------

-- 22. Average Discount by Category
SELECT Product_Category,
       ROUND(AVG(Discount), 2) AS Avg_Discount
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Avg_Discount DESC;

--------------------------------------------------

-- 23. Average Rating by Region
SELECT Region,
       ROUND(AVG(Customer_Rating), 2) AS Avg_Rating
FROM ecommerce_sales
GROUP BY Region
ORDER BY Avg_Rating DESC;

--------------------------------------------------

-- 24. Average Delivery Time by Region
SELECT Region,
       ROUND(AVG(Delivery_Days), 2) AS Avg_Delivery
FROM ecommerce_sales
GROUP BY Region
ORDER BY Avg_Delivery;

--------------------------------------------------

-- 25. Top 5 Revenue-Generating Categories
SELECT Product_Category,
       ROUND(SUM(Revenue), 2) AS Revenue
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Revenue DESC
LIMIT 5;
