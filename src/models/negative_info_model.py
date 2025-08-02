from typing import Optional
from entities.negative_info import NegativeInfo
from models.base_model import BaseModel

class NegativeInfoModel (BaseModel):
    TABLE_NAME = "negative_info"

    def create_table(self):
        """
        Создает в БД таблицу negative_info если она не существует.
        """
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            client_id INT NOT NULL,
            status VARCHAR(256) DEFAULT NULL,
            removed_from_sme_registry VARCHAR(256) DEFAULT NULL,
            recently_registered VARCHAR(256) DEFAULT NULL,
            disqualified_director VARCHAR(256) DEFAULT NULL,
            disqualified_director_other VARCHAR(256) DEFAULT NULL,
            disqualified_director_other_no_inn VARCHAR(256) DEFAULT NULL,
            sme_mass_address_registry VARCHAR(256) DEFAULT NULL,
            mass_address VARCHAR(256) DEFAULT NULL,
            decision_change_address VARCHAR(256) DEFAULT NULL,
            invalid_address VARCHAR(256) DEFAULT NULL,
            region_change_last_year VARCHAR(256) DEFAULT NULL,
            mass_director_registry VARCHAR(256) DEFAULT NULL,
            mass_directors VARCHAR(256) DEFAULT NULL,
            mass_directors_no_inn VARCHAR(256) DEFAULT NULL,
            director_liquidated_companies VARCHAR(256) DEFAULT NULL,
            director_liquidated_companies_no_inn VARCHAR(256) DEFAULT NULL,
            invalid_director VARCHAR(256) DEFAULT NULL,
            mass_founder_registry VARCHAR(256) DEFAULT NULL,
            mass_director_founder_registry VARCHAR(256) DEFAULT NULL,
            disqualified_founder_other VARCHAR(256) DEFAULT NULL,
            disqualified_founder_other_no_inn VARCHAR(256) DEFAULT NULL,
            founder_liquidated_companies VARCHAR(256) DEFAULT NULL,
            founder_liquidated_companies_no_inn VARCHAR(256) DEFAULT NULL,
            simultaneous_change_director_founder VARCHAR(256) DEFAULT NULL,
            director_changes_per_year_more_than_two VARCHAR(256) DEFAULT NULL,
            director_is_sole_founder VARCHAR(256) DEFAULT NULL,
            invalid_founder VARCHAR(256) DEFAULT NULL,
            encumbrances VARCHAR(256) DEFAULT NULL,
            no_tax_reporting_over_year VARCHAR(256) DEFAULT NULL,
            tax_debt VARCHAR(256) DEFAULT NULL,
            decision_reduce_charter_capital VARCHAR(256) DEFAULT NULL,
            employee_count VARCHAR(256) DEFAULT NULL,
            account_blocked VARCHAR(256) DEFAULT NULL,
            bankrupt VARCHAR(256) DEFAULT NULL,
            bankruptcy_intent VARCHAR(256) DEFAULT NULL,
            tax_audit_risk VARCHAR(256) DEFAULT NULL,
            tax_arrears VARCHAR(256) DEFAULT NULL,
            summary_text TEXT DEFAULT NULL
        ) ENGINE=InnoDB;
        """

        try:
            self._connect()
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
        finally:
            cursor.close()
            self._close()

    def create(self, negative_info: NegativeInfo) -> int:
        """
        Создает запись в таблице negative_info на основе объекта NegativeInfo.

        Args:
            negative_info (NegativeInfo): Объект Pydantic с данными для вставки.

        Returns:
            Optional[int]: ID созданной записи.
        """
        query = f"""
        INSERT INTO {self.TABLE_NAME} (
            client_id, status, removed_from_sme_registry, recently_registered,
            disqualified_director, disqualified_director_other, disqualified_director_other_no_inn,
            sme_mass_address_registry, mass_address, decision_change_address, invalid_address,
            region_change_last_year, mass_director_registry, mass_directors, mass_directors_no_inn,
            director_liquidated_companies, director_liquidated_companies_no_inn, invalid_director,
            mass_founder_registry, mass_director_founder_registry, disqualified_founder_other,
            disqualified_founder_other_no_inn, founder_liquidated_companies,
            founder_liquidated_companies_no_inn, simultaneous_change_director_founder,
            director_changes_per_year_more_than_two, director_is_sole_founder, invalid_founder,
            encumbrances, no_tax_reporting_over_year, tax_debt, decision_reduce_charter_capital,
            employee_count, account_blocked, bankrupt, bankruptcy_intent, tax_audit_risk,
            tax_arrears, summary_text
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
        """
        cursor = None
        try:
            self._connect()
            cursor = self.connection.cursor()
            # Преобразуем объект NegativeInfo в словарь с именами полей (не алиасами)
            data = negative_info.dict(exclude={"id"})  # Исключаем id, так как он автоинкрементный
            # Формируем кортеж значений в порядке столбцов таблицы
            values = (
                data["client_id"],
                data["status"],
                data["removed_from_sme_registry"],
                data["recently_registered"],
                data["disqualified_director"],
                data["disqualified_director_other"],
                data["disqualified_director_other_no_inn"],
                data["sme_mass_address_registry"],
                data["mass_address"],
                data["decision_change_address"],
                data["invalid_address"],
                data["region_change_last_year"],
                data["mass_director_registry"],
                data["mass_directors"],
                data["mass_directors_no_inn"],
                data["director_liquidated_companies"],
                data["director_liquidated_companies_no_inn"],
                data["invalid_director"],
                data["mass_founder_registry"],
                data["mass_director_founder_registry"],
                data["disqualified_founder_other"],
                data["disqualified_founder_other_no_inn"],
                data["founder_liquidated_companies"],
                data["founder_liquidated_companies_no_inn"],
                data["simultaneous_change_director_founder"],
                data["director_changes_per_year_more_than_two"],
                data["director_is_sole_founder"],
                data["invalid_founder"],
                data["encumbrances"],
                data["no_tax_reporting_over_year"],
                data["tax_debt"],
                data["decision_reduce_charter_capital"],
                data["employee_count"],
                data["account_blocked"],
                data["bankrupt"],
                data["bankruptcy_intent"],
                data["tax_audit_risk"],
                data["tax_arrears"],
                data["summary_text"],
            )
            cursor.execute(query, values)
            self.connection.commit()
            # Возвращаем ID созданной записи
            return cursor.lastrowid
        finally:
            if cursor:
                cursor.close()
            self._close()