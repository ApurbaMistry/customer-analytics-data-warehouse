import logging


def explore_data(dataframe):

    logging.info("Exploring dataset...")

    print("\n========== DATASET OVERVIEW ==========")

    print(f"Rows    : {dataframe.shape[0]}")
    print(f"Columns : {dataframe.shape[1]}")

    print("\n========== COLUMN NAMES ==========")
    print(dataframe.columns.tolist())

    print("\n========== DATA TYPES ==========")
    print(dataframe.dtypes)

    logging.info("Dataset exploration completed.")

    return dataframe