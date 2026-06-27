-- =====================================
-- Total Sales
-- =====================================

SELECT
SUM(Sales) AS Total_Sales
FROM Fact_Sales;


-- =====================================
-- Total Profit
-- =====================================

SELECT
SUM(Profit) AS Total_Profit
FROM Fact_Sales;


-- =====================================
-- Average Discount
-- =====================================

SELECT
AVG(Discount) AS Average_Discount
FROM Fact_Sales;


-- =====================================
-- Total Quantity Sold
-- =====================================

SELECT
SUM(Quantity) AS Total_Quantity
FROM Fact_Sales;