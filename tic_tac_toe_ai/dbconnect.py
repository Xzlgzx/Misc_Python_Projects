import psycopg2
import json
from prefect import task, Flow, Parameter


class DatabaseConnection:
    PARAMS_JSON_FILE = 'aws_rds.json'
    TABLE_NAME = 'game_stat'

    def __init__(self):
        with open(self.PARAMS_JSON_FILE) as file:
            params = json.load(file)
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()
        if self.is_table_created():
            self.create_table()
            print("Table created.")
        print("Ready to execute SQL.")

    def is_table_created(self):
        self.cursor.execute("select exists(select * from information_schema."
                            "tables where table_name=%s)", (self.TABLE_NAME,))
        exist = self.cursor.fetchone()[0]
        if not exist:
            return True

    def create_table(self):
        self.cursor.execute("""CREATE TABLE game_stat(
            game_id SERIAL PRIMARY KEY,
            game_time float,
            user_location text,
            is_computer_winner boolean,
            is_user1_winner boolean,
            is_draw boolean,
            game_level integer,
            nbr_of_rounds integer)""")
        self.connection.commit()

    def get_latest_query(self):
        return query #

    def query_cur_game(self):
        pass # organize gamestat

    def update_query(self):
        pass # push query


class ETL:
    def __init__(self):
        # Connect to database, set up gamestat,
        pass

    @task
    def extract(self):
        pass

    @task
    def transform(self):
        pass

    @task
    def connect(self):
        pass


def build_flow():
    with Flow("My etl") as flow:
        path = Parameter(name="path", required=True)
        etl(path)
    return flow
