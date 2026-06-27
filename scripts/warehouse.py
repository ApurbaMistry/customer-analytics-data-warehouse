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