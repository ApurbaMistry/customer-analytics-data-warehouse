import logging
import os


def create_staging(dataframe):

    logging.info("Creating staging dataset...")

    os.makedirs("data/staging", exist_ok=True)


    print(os.getcwd())
    print(os.path.abspath("data/staging/staging_superstore.csv"))

    dataframe.to_csv(
        "data/staging/staging_superstore.csv",
        index=False
    )

    logging.info("Staging dataset created successfully.")

    return dataframe