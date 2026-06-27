import logging
import pandas as pd


def extract_data(file_path):

    logging.info("Reading customer dataset...")

    dataframe = pd.read_csv(file_path)

    logging.info("Dataset loaded successfully.")

    return dataframe