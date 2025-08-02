import json
from typing import Dict, List
from fns_api_client import FnsApiClient
import os
from dotenv import load_dotenv
from models.clients_model import ClientsModel
from models.negative_info_model import NegativeInfoModel
from entities.client import Client
from entities.negative_info import NegativeInfo
from datetime import date

load_dotenv()

negative_info_model: NegativeInfoModel
clients_model: ClientsModel
base_url: str
api_key: str


def main():
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
    
    prepare_tables()
    update_negative_info()

    clietns:List[Client] =  clients_model.get_all() 
    
    return

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
    clients: List[Client] = clients_model.get_unverified_clients()
    api_client = FnsApiClient(base_url, api_key)
    for client in clients:
        try:
            response: Dict = api_client.check(client.inn)
            negative_info: Dict = response["items"][0]["ЮЛ"]["Негатив"]
            if negative_info == {}:
                clients_model.update_has_negative(client.id, False)
                print(f"Нет негативной информации для ИНН {client.inn}.")
            else:
                negative_obj: NegativeInfo = NegativeInfo(**negative_info)
                clients_model.update_has_negative(client.id, True)
                negative_obj.client_id = client.id
                negative_info_model.create(negative_obj)

            clients_model.update_fns_check_date(client.id, date.today())
                
        except Exception as e:
                print(f"Ошибка при обновлении данных для клиента с ИНН {client.inn}: {e}")


if __name__ == "__main__":
    main()
