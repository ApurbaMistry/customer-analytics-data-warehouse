import logging
import sqlite3


def create_warehouse():

    logging.info("Creating warehouse database...")

    connection = sqlite3.connect(
        "database/customer_warehouse.db"
    )

    cursor = connection.cursor()

    with open("sql/create_tables.sql", "r") as sql_file:
        cursor.executescript(sql_file.read())

    connection.commit()
    connection.close()

    logging.info("Warehouse created successfully.")


def load_dimension_tables(dataframe):

    logging.info("Loading Dimension Tables...")

    connection = sqlite3.connect(
        "database/customer_warehouse.db"
    )

    # -----------------------------
    # Customer Dimension
    # -----------------------------
    dim_customer = dataframe[
        ["Customer_ID", "Customer_Name", "Segment"]
    ].drop_duplicates()

    dim_customer.to_sql(
        "Dim_Customer",
        connection,
        if_exists="replace",
        index=False
    )

    # -----------------------------
    # Product Dimension
    # -----------------------------
    dim_product = dataframe[
        [
            "Product_ID",
            "Category",
            "Sub_Category",
            "Product_Name"
        ]
    ].drop_duplicates()

    dim_product.to_sql(
        "Dim_Product",
        connection,
        if_exists="replace",
        index=False
    )

    # -----------------------------
    # Location Dimension
    # -----------------------------
    dim_location = dataframe[
        [
            "Country",
            "State",
            "City",
            "Region"
        ]
    ].drop_duplicates()

    dim_location.to_sql(
        "Dim_Location",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    logging.info("Dimension Tables Loaded Successfully.")

    return dataframe


def load_fact_table(dataframe):

    logging.info("Loading Fact Table...")

    connection = sqlite3.connect(
        "database/customer_warehouse.db"
    )

    # -----------------------------
    # Create Location Lookup Table
    # -----------------------------
    location_lookup = dataframe[
        [
            "Country",
            "State",
            "City",
            "Region"
        ]
    ].drop_duplicates().reset_index(drop=True)

    location_lookup["Location_ID"] = location_lookup.index + 1

    # -----------------------------
    # Fact Table
    # -----------------------------
    fact_sales = dataframe[
        [
            "Order_ID",
            "Customer_ID",
            "Product_ID",
            "Country",
            "State",
            "City",
            "Region",
            "Sales",
            "Quantity",
            "Discount",
            "Profit"
        ]
    ].copy()

    fact_sales = fact_sales.merge(
        location_lookup,
        on=["Country", "State", "City", "Region"],
        how="left"
    )

    fact_sales = fact_sales[
        [
            "Order_ID",
            "Customer_ID",
            "Product_ID",
            "Location_ID",
            "Sales",
            "Quantity",
            "Discount",
            "Profit"
        ]
    ]

    fact_sales.to_sql(
        "Fact_Sales",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    logging.info("Fact Table Loaded Successfully.")

    return dataframe