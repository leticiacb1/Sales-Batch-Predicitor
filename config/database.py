import psycopg2
from environment import EnvironmentVariables


class ConfigureDatabase():

    def __init__(self):
        self.env = EnvironmentVariables()
        self.connection = None
        self.cursor = None

    def get_environment_variables(self) -> None:
        self.env.get()

    def get_connection(self) -> psycopg2.extensions.connection:

        print(self.env.DATABASE)
        print(self.env.USERNAME)
        print(self.env.PASSWORD)
        print(self.env.HOST)
        print(self.env.PORT)

        self.connection = psycopg2.connect(
            database=self.env.DATABASE, 
            user=self.env.USERNAME,
            password=self.env.PASSWORD,
            host=self.env.HOST,
            port=self.env.PORT
        )

        return self.connection

    def get_cursor(self) -> psycopg2.extensions.cursor:
        self.cursor = self.connection.cursor()
        return self.cursor


if __name__ == "__main__":

    configure_database = ConfigureDatabase()
    configure_database.get_environment_variables()
    configure_database.get_connection()
    configure_database.get_cursor()