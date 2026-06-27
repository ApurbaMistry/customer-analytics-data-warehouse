import logging

from scripts.extract import extract_data
from scripts.explore import explore_data
from scripts.validate import validate_data
from scripts.clean import clean_data
from scripts.staging import create_staging
from scripts.warehouse import create_warehouse
from scripts.warehouse import (
    create_warehouse,
    load_dimension_tables
)
from scripts.warehouse import (
    create_warehouse,
    load_dimension_tables,
    load_fact_table
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from scripts.analytics import generate_business_report


def main():

    file_path = "data/raw/superstore.csv"

    dataframe = extract_data(file_path)

    dataframe = explore_data(dataframe)

    dataframe = validate_data(dataframe)

    dataframe = clean_data(dataframe)

    dataframe = create_staging(dataframe)

    create_warehouse()

    dataframe = load_dimension_tables(dataframe)

    dataframe = load_fact_table(dataframe)

    generate_business_report()

    print(dataframe.head())


if __name__ == "__main__":

    main()