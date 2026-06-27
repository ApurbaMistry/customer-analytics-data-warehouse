import logging


def validate_data(dataframe):

    logging.info("Starting data validation...")

    print("\n========== DATA VALIDATION ==========")

    print(f"Rows : {dataframe.shape[0]}")
    print(f"Columns : {dataframe.shape[1]}")

    print("\nNull Value Report")
    print(dataframe.isnull().sum())

    duplicate_rows = dataframe.duplicated().sum()

    print(f"\nDuplicate Rows : {duplicate_rows}")

    print("\nData Types")
    print(dataframe.dtypes)

    logging.info("Data validation completed.")

    return dataframe