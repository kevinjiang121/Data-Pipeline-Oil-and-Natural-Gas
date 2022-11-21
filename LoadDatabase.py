from sqlalchemy import create_engine
import pandas as pd


class LoadDatabase:

    def __init__(self):
        pass

    @staticmethod
    def load_database(path):
        """
            Loads the data scrap into a PostgresSQL database
            Arguments:
                path: location for CSV file
        """
        # gets SQL connection
        user = input("Database username: ")
        password = input("Password: ")
        host = input("Host: ")
        table = input("Table: ")
        conn_str = 'postgresql://' + user + ':' + password + '@' + host + '/' + table
        engine = create_engine(conn_str)
        conn = engine.connect()

        # Reads a CSV file and creates a dataframe to be loaded into a database
        data = pd.read_csv(path + '\\df_all_data.csv')
        df = pd.DataFrame(data)
        df.to_sql('Product', con=conn, if_exists='replace', index_label='Index')
