-- Customer Dimension

CREATE TABLE IF NOT EXISTS Dim_Customer (

    Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Customer_Name TEXT,

    Segment TEXT

);



-- Product Dimension

CREATE TABLE IF NOT EXISTS Dim_Product (

    Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Category TEXT,

    Sub_Category TEXT

);



-- Location Dimension

CREATE TABLE IF NOT EXISTS Dim_Location (

    Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Country TEXT,

    State TEXT,

    City TEXT,

    Region TEXT

);