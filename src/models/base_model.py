import mysql.connector

class BaseModel:
    def __init__(
        self, db_host: str, db_port: int, db_user: str, db_password: str, db_name: str
    ):
        self.connection = None
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name


    def _connect(self):
        """Устанавливает соединение с базой данных."""
        self.connection = mysql.connector.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name,
        )

    def _close(self):
        """Закрывает соединение с базой данных."""
        if self.connection:
            self.connection.close()