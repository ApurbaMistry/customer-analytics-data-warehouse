import logging

from scripts.extract import extract_data
from scripts.explore import explore_data
from scripts.staging import create_staging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    file_path = "data/raw/superstore.csv"

    dataframe = extract_data(file_path)

    dataframe = explore_data(dataframe)

    dataframe = create_staging(dataframe)

    print(dataframe.head())


if __name__ == "__main__":

    main()