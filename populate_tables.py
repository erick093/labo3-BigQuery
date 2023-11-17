import logging
import pandas as pd
import sys
import argparse
import configparser
import pyarrow.parquet as pq
from sqlalchemy import create_engine


# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def populate_tables(dataframe, conn, table_name):
    logging.info(f"Populating the {table_name} table")
    # Save the dataframe to the database
    dataframe.to_sql(table_name, con=conn, schema="public", index=False, if_exists="replace", chunksize=1000)
    conn.commit()


def create_database_connection(connection_string):
    logging.info("Creating the database connection")
    # Create a database engine
    engine = create_engine(connection_string)
    conn = engine.connect()
    return conn

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Path to the config file", required=True)
    parser.add_argument("-d", "--data-path", type=str, help="Path to the data", required=True)
    parser.add_argument("-t", "--table-name", type=str, help="Name of the table", required=True)
    args = parser.parse_args()

    # Read the config file
    config = configparser.ConfigParser()
    config.read(args.config)

    # Logging welcome message
    logging.info(f"Reading data from {args.data_path}")

    # Create a dataframe
    if args.data_path.endswith(".parquet"):
        df = pq.read_table(args.data_path).to_pandas()
    else:
        df = pd.read_csv(args.data_path)

    # Define connection string
    connection_string = f"postgresql://{config['postgres']['username']}:{config['postgres']['password']}" \
                        f"@{config['postgres']['host']}:{config['postgres']['port']}/{config['postgres']['database']}"

    # Create a database connection
    conn = create_database_connection(connection_string)

    # Save the dataframe to the database
    populate_tables(df, conn, table_name=args.table_name)


if __name__ == "__main__":
    main()