from typing import Dict, List
from fns_api_client import FnsApiClient
import os
from dotenv import load_dotenv
from models.clients_model import ClientsModel
from models.negative_info_model import NegativeInfoModel
from entities.client import Client
from entities.negative_info import NegativeInfo
from datetime import date
import logging

load_dotenv()

negative_info_model: NegativeInfoModel
clients_model: ClientsModel
base_url: str
api_key: str

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s\t%(levelname)s\t%(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

def main() -> None:
    logging.info("Запуск приложения")

    global negative_info_model
    global clients_model
    global base_url
    global api_key

    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    base_url=os.getenv("API_URL")
    api_key=os.getenv("API_KEY")

    negative_info_model = NegativeInfoModel(db_host, db_port, db_user, db_password, db_name)
    clients_model = ClientsModel(db_host, db_port, db_user, db_password, db_name)
    
    # Добавление недостающих в БД столбцов и таблиц
    prepare_tables()

    # Получение из ФНС данных о проверке контрагентов и запись их в БД
    update_negative_info()

def prepare_tables():
    """
    Подготавливает БД, создавая необходимые столбцы и таблицы.
    """
    negative_info_model.create_table()
    clients_model.prepare_table()

def update_negative_info():
    """
    Получает из ФНС данные о проверке контрагентов и записывает их в БД.
    """
    logging.info("Начало обновления данных о проверке контрагентов в ФНС")

    clients: List[Client] = clients_model.get_unverified_clients()
    logging.debug(f"Требуется запросить данные о {len(clients)} клиентах")

    api_client = FnsApiClient(base_url, api_key)
    
    for client in clients:
        logging.debug(f"Обработка клиента с ИНН {client.inn}")
        try:
            response: Dict = api_client.check(client.inn)
            negative_info: Dict = response["items"][0]["ЮЛ"]["Негатив"]
            if negative_info == {}:
                logging.info(f"Нет негативной информации для ИНН {client.inn}.")
                clients_model.update_has_negative(client.id, False)
            else:
                negative_obj: NegativeInfo = NegativeInfo(**negative_info)
                clients_model.update_has_negative(client.id, True)
                negative_obj.client_id = client.id
                negative_info_model.create(negative_obj)

            clients_model.update_fns_check_date(client.id, date.today())
                
        except Exception as e:
            logging.error(f"Ошибка при обработке клиента с ИНН {client.inn}: {e}")
    
    logging.info("Обновление данных о проверке контрагентов в ФНС завершено")


if __name__ == "__main__":
    main()
