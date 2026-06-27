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

    logging.info("Data cleaning completed.")

    return dataframe