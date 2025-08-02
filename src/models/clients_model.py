from entities.client import Client
from typing import List
import mysql.connector
from models.base_model import BaseModel
from datetime import date


class ClientsModel(BaseModel):
    """Модель для работы с таблицей отчетов о проверке в ФНС в базе данных."""

    TABLE_NAME = "clients"

    def _is_table_altered(self) -> bool:
        """
        Проверяет наличие столбца 'fns_check_date' в таблице 'clients'.

        Returns:
            bool: True, если столбец существует, False - если нет.
        """
        query = """
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = %s
        AND COLUMN_NAME = 'fns_check_date';
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
        Добавляет столбец 'fns_check_date' в таблицу 'clients', если он не существует.
        """
        if self._is_table_altered():
            print("Столбец 'fns_check_date' уже существует.")
            return

        query = """
        ALTER TABLE clients
        ADD COLUMN fns_check_date DATE NULL,
        ADD COLUMN has_negative BOOLEAN NULL;
        """

        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        finally:
            cursor.close()
            self._close()

    def get_all(self) -> List[Client]:
        """
        Извлекает все записи из таблицы 'clients'

        Returns:
            List[Client]: Список объектов Client, представляющих записи из таблицы.
        """
        query = f"""
        SELECT *
        FROM {self.TABLE_NAME};
        """
        try:
            self._connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            rows = cursor.fetchall()
            clients = [Client(**row) for row in rows]
            return clients
        finally:
            cursor.close()
            self._close()

    def get_unverified_clients(self) -> List[Client]:
        """
        Извлекает из таблицы клиентов, для которых еще не были получены данные из ФНС (NULL в столбце fns_check_date).

        Returns:
            List[Client]: Список объектов Client, представляющих записи из таблицы.
        """
        query = f"""
        SELECT *
        FROM {self.TABLE_NAME}
        WHERE fns_check_date IS NULL;
        """
        try:
            self._connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            rows = cursor.fetchall()
            clients = [Client(**row) for row in rows]
            return clients
        finally:
            cursor.close()
            self._close()

    def update_fns_check_date(self, client_id: int, check_date: date) -> bool:
        """
        Обновляет столбец 'fns_check_date' для клиента с указанным ID.
        
        Args:
            client_id (int): ID клиента.
            check_date (date): Дата для записи в столбец fns_check_date.
    
        """
        query = f"""
        UPDATE {self.TABLE_NAME}
        SET fns_check_date = %s
        WHERE id = %s;
        """
        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(query, (check_date, client_id))
            self.connection.commit()
            if cursor.rowcount == 0:
                print(f"Клиент с ID {client_id} не найден.")
                return False
            print(f"Столбец 'fns_check_date' успешно обновлен для клиента с ID {client_id}.")
            return True
        finally:
            cursor.close()
            self._close()

    def update_has_negative(self, client_id: int, has_negative: bool) -> bool:
        """
        Обновляет столбец 'has_negative' для клиента с указанным ID.
        
        Args:
            client_id (int): ID клиента.
            has_negative (bool): Значение для записи в столбец has_negative.
        
        Returns:
            bool: True, если обновление успешно, False - в случае ошибки.
        """
        query = f"""
        UPDATE {self.TABLE_NAME}
        SET has_negative = %s
        WHERE id = %s;
        """
        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(query, (has_negative, client_id))
            self.connection.commit()
            if cursor.rowcount == 0:
                print(f"Клиент с ID {client_id} не найден.")
                return False
            print(f"Столбец 'has_negative' успешно обновлен для клиента с ID {client_id}.")
            return True
        finally:
            cursor.close()
            self._close()