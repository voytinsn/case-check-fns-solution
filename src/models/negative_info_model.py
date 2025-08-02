import mysql.connector
from mysql.connector import errorcode

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
            partner_id INT NOT NULL,
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

