import mysql.connector
from mysql.connector import errorcode
from models.base_model import BaseModel

class ClientsModel(BaseModel):
    """Модель для работы с таблицей отчетов о проверке в ФСС в базе данных."""

    TABLE_NAME = "clients"

    def _is_table_altered(self) -> bool:
        """
        Проверяет наличие столбца 'fss_check_date' в таблице 'clients'.
        
        Returns:
            bool: True, если столбец существует, False - если нет.
        """
        query = """
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = %s
        AND COLUMN_NAME = 'fss_check_date';
        """

        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(query, (self.TABLE_NAME,))
            result = cursor.fetchone()
        finally:
            cursor.close()
            self._close()

        return result[0] > 0

    def prepare_table(self):
        """
        Добавляет столбец 'fss_check_date' в таблицу 'clients', если он не существует.
        """
        if self._is_table_altered():
            print("Столбец 'fss_check_date' уже существует.")
            return

        query = """
        ALTER TABLE clients
        ADD COLUMN fss_check_date DATE NULL AFTER date_reg;
        """

        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        finally:
            cursor.close()
            self._close()