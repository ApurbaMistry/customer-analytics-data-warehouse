import logging

from scripts.extract import extract_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    file_path = "data/raw/superstore.csv"

    dataframe = extract_data(file_path)

    print(dataframe.head())


if __name__ == "__main__":

    main()