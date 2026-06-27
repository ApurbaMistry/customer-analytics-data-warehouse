import logging


def clean_data(dataframe):

    logging.info("Starting data cleaning...")

    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()

    # Remove extra spaces from text columns
    text_columns = dataframe.select_dtypes(include="object").columns

    dataframe[text_columns] = dataframe[text_columns].apply(
        lambda column: column.str.strip()
    )

    # Rename columns for Data Warehouse
    dataframe.rename(
        columns={
            "Customer.ID": "Customer_ID",
            "Customer.Name": "Customer_Name",
            "Product.ID": "Product_ID",
            "Product.Name": "Product_Name",
            "Order.ID": "Order_ID",
            "Order.Date": "Order_Date",
            "Ship.Date": "Ship_Date",
            "Ship.Mode": "Ship_Mode",
            "Sub.Category": "Sub_Category"
        },
        inplace=True
    )

    logging.info("Data cleaning completed.")

    return dataframe