import sqlite3
import pandas as pd
import logging


def generate_business_report():

    logging.info("Generating business report...")

    connection = sqlite3.connect(
        "database/customer_warehouse.db"
    )

    # ----------------------------
    # Total Sales
    # ----------------------------

    total_sales = pd.read_sql_query(
        """
        SELECT
        SUM(Sales) AS Total_Sales
        FROM Fact_Sales
        """,
        connection
    )

    # ----------------------------
    # Total Profit
    # ----------------------------

    total_profit = pd.read_sql_query(
        """
        SELECT
        SUM(Profit) AS Total_Profit
        FROM Fact_Sales
        """,
        connection
    )

    # ----------------------------
    # Average Discount
    # ----------------------------

    average_discount = pd.read_sql_query(
        """
        SELECT
        AVG(Discount) AS Average_Discount
        FROM Fact_Sales
        """,
        connection
    )

    # ----------------------------
    # Total Quantity
    # ----------------------------

    total_quantity = pd.read_sql_query(
        """
        SELECT
        SUM(Quantity) AS Total_Quantity
        FROM Fact_Sales
        """,
        connection
    )

    print("\n========== BUSINESS REPORT ==========\n")

    print(total_sales)

    print()

    print(total_profit)

    print()

    print(average_discount)

    print()

    print(total_quantity)

    report = pd.concat(
    [
        total_sales,
        total_profit,
        average_discount,
        total_quantity
    ],
    axis=1
)

report.to_csv(
    "data/exports/business_report.csv",
    index=False
)

connection.close()

logging.info("Business report exported successfully.")