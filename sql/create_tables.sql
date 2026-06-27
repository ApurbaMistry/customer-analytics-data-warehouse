-- ===========================
-- Customer Dimension
-- ===========================

CREATE TABLE IF NOT EXISTS Dim_Customer (

    Customer_ID TEXT PRIMARY KEY,

    Customer_Name TEXT,

    Segment TEXT

);

-- ===========================
-- Product Dimension
-- ===========================

CREATE TABLE IF NOT EXISTS Dim_Product (

    Product_ID TEXT PRIMARY KEY,

    Category TEXT,

    Sub_Category TEXT,

    Product_Name TEXT

);

-- ===========================
-- Location Dimension
-- ===========================

CREATE TABLE IF NOT EXISTS Dim_Location (

    Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Country TEXT,

    State TEXT,

    City TEXT,

    Region TEXT

);

-- ===========================
-- Fact Table
-- ===========================

CREATE TABLE IF NOT EXISTS Fact_Sales (

    Order_ID TEXT,

    Customer_ID TEXT,

    Product_ID TEXT,

    Location_ID INTEGER,

    Sales REAL,

    Quantity INTEGER,

    Discount REAL,

    Profit REAL
);